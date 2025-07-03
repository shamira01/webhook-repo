from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB connection
client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
db = client['github_events']
collection = db['events']

def parse_webhook_data(payload, event_type):
    """Parse GitHub webhook payload and extract relevant information."""
    try:
        if event_type == 'push':
            return {
                'id': payload.get('after', '')[:8],
                'author': payload['pusher']['name'],
                'action': 'push',
                'from_branch': None,
                'to_branch': payload['ref'].split('/')[-1],
                'timestamp': datetime.utcnow()
            }
        
        elif event_type == 'pull_request':
            pr = payload['pull_request']
            action = payload.get('action')

            if action == 'opened':
                return {
                    'id': f"pr_{pr['number']}",
                    'author': pr['user']['login'],
                    'action': 'pull_request',
                    'from_branch': pr['head']['ref'],
                    'to_branch': pr['base']['ref'],
                    'timestamp': datetime.utcnow()
                }
            elif action == 'closed' and pr.get('merged'):
                return {
                    'id': f"merge_{pr['number']}",
                    'author': pr['merged_by']['login'] if pr.get('merged_by') else pr['user']['login'],
                    'action': 'merge',
                    'from_branch': pr['head']['ref'],
                    'to_branch': pr['base']['ref'],
                    'timestamp': datetime.utcnow()
                }
            else:
                return None  # Ignore other pull_request actions

        return None  # Ignore other events

    except Exception as e:
        print(f"Error parsing webhook: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        event_type = request.headers.get('X-GitHub-Event')
        payload = request.get_json()

        print(f"✅ Received {event_type} event")

        event_data = parse_webhook_data(payload, event_type)

        if event_data:
            collection.insert_one(event_data)
            print(f"✅ Stored event: {event_data}")
            return jsonify({'status': 'success', 'message': 'Event stored'}), 200
        else:
            print("⚠️ Ignored event")
            return jsonify({'status': 'ignored', 'message': 'Event not relevant'}), 200

    except Exception as e:
        print(f"❌ Webhook error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/events')
def get_events():
    try:
        events = list(collection.find().sort('timestamp', -1).limit(20))

        for event in events:
            event['_id'] = str(event['_id'])
            formatted_ts = event['timestamp'].strftime('%d %B %Y - %I:%M %p UTC')
            if event['action'] == 'push':
                event['message'] = f"{event['author']} pushed to {event['to_branch']} on {formatted_ts}"
            elif event['action'] == 'pull_request':
                event['message'] = f"{event['author']} submitted a pull request from {event['from_branch']} to {event['to_branch']} on {formatted_ts}"
            elif event['action'] == 'merge':
                event['message'] = f"{event['author']} merged branch {event['from_branch']} to {event['to_branch']} on {formatted_ts}"
            else:
                event['message'] = "Unknown event"
            event['timestamp'] = formatted_ts

        return jsonify(events), 200

    except Exception as e:
        print(f"❌ API error: {e}")
        return jsonify([]), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
