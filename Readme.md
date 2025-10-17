# 🗨️ Python Socket Chat App

A simple **real-time chat application** built using Python’s `socket` and `threading` modules.  
It allows **bidirectional** (simultaneous) communication between client and server.

---

## 🚀 Features
- Full-duplex communication (both sides can chat at once)
- Clean terminal interface with sender labels
- Multi-client support (server can handle multiple connections)
- Minimal code — great for learning socket programming!

---

## 🧩 How It Works
- The **server** listens on a port (e.g. 9000)
- The **client** connects using the same host and port
- Separate threads handle **sending** and **receiving** messages
- Connection closes when either side sends an empty message

---

## 🧠 Prerequisites
- Python 3.8 or above

---

## ⚙️ Run Instructions

### 1️⃣ Start the server
```bash
python server.py
```
### 2️⃣ Start the client
```bash
python client.py
```
### 3️⃣ Chat freely 🎉

### 🧰 Tech Stack

    Python socket

    Python threading

### 🌟 Future Improvements

    Add usernames and timestamps

    Use colorama for colored terminal UI

    Add message encryption

### 🧑‍💻 Author

    Paramhans Mishra

