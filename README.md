# GitHub Repository Activity Monitor

This project is a **Flask-based web application** that listens to GitHub webhook events and displays real-time repository activities like **pushes**, **pull requests**, and **merges**.  
Events are stored in **MongoDB** and displayed on a simple web dashboard with automatic updates.

---

## 📌 **Features**

- ✅ Receives GitHub webhook events (Push, Pull Request, Merge)
- ✅ Stores events in MongoDB with relevant details
- ✅ Displays repository activity in real time
- ✅ Polls every 15 seconds for new updates
- ✅ Uses ngrok to expose local Flask server for webhook delivery

---

## 🗂️ **Tech Stack**

- **Python 3.x**
- **Flask**
- **pymongo** (MongoDB driver)
- **MongoDB** (local or Atlas)
- **ngrok** (for local tunnel)
- **HTML, CSS, JavaScript** (for UI polling)

---

## 🚀 **Getting Started**

### 1️⃣ **Clone the repository**
```bash
git clone https://github.com/shamira01/webhook-repo.git
cd webhook-repo
