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

#Output Screenshots

![image](https://github.com/user-attachments/assets/840e252e-75d3-4861-9c5e-6b9e529c0bee)

![image](https://github.com/user-attachments/assets/2e889dda-e37c-4cf0-b754-2eebb4f58907)

![image](https://github.com/user-attachments/assets/8a174542-df6f-45bb-9588-09b02841d1e7)

![image](https://github.com/user-attachments/assets/53deb0f4-0705-42b4-a70e-c14801b844ef)

![image](https://github.com/user-attachments/assets/2cbd99b3-3997-4f1a-9e6e-9a217eb2ecab)



## 🚀 **Getting Started**

### 1️⃣ **Clone the repository**
```bash
git clone https://github.com/shamira01/webhook-repo.git
cd webhook-repo
