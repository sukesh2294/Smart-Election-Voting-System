
# 🗳️ Smart Election Voting System

A secure, facial-recognition-based online voting platform built using **Flask**, **React**, **SQLite**, and **OpenCV**, designed to improve transparency, accessibility, and trust in the electoral process.



## 📌 Project Overview

**Smart Election Voting System** is a digital voting solution that provides secure, real-time election management with multi-step voter authentication, including:

- Voter Registration (with face capture)
- OTP + Password + Face-based Login
- Admin Panel for Election & Candidate Management
- Secure Vote Casting and Result Publication

---

## 🔐 Key Features

### ✅ Voter Side
- 🧍‍♂️ **Multi-step Registration** (Email, OTP, Face Recognition)
- 🔐 **Secure Login** (ID + Password + OTP + Face)
- 🗳️ **Vote Casting with Face Verification**
- 📊 **View Results** for published elections

### 🧑‍💼 Admin Side
- 🗂️ **Manage Elections** (Create, Edit, Schedule, Publish Results)
- 🧑‍🤝‍🧑 **Manage Voters** (Add, View, Delete, Export CSV)
- 👨‍💼 **Manage Candidates** (Add, Remove, Assign to Election)
- ⏳ **Schedule Voting Time Window**
- 🔍 **Live Status Monitoring** & Result Analytics

---

## 🧑‍💻 Technologies Used

| Stack        | Tools/Frameworks |
|--------------|------------------|
| **Frontend** | React.js, HTML/CSS, JavaScript |
| **Backend**  | Flask (Python), Flask-SQLAlchemy |
| **Database** | SQLite |
| **Face Auth**| OpenCV, `face_recognition` library |
| **Security** | OTP Verification, bcrypt Password Hashing |

---

## 🧠 System Architecture

```mermaid
graph LR
A[Voter/Admin UI] --> B[Flask API]
B --> C[SQLite DB]
B --> D[Face Recognition Module]
