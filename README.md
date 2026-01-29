# Web-Based Facial Authentication System (Dockerized)

## Overview
This project implements a **web-based facial authentication system** using a webcam and facial recognition techniques. The system captures live images from a user’s webcam, extracts facial features using **dlib-based embeddings**, and verifies identity against enrolled faces. To enhance security, **rate limiting** is applied to prevent brute-force attempts.

The application is fully **containerized using Docker (Podman compatible)** to ensure dependency isolation and system stability, especially on security-focused operating systems like **Kali Linux**.

---

## Key Features
- Webcam-based facial login
- Face recognition using **dlib + face_recognition**
- Real-time image capture via browser
- Brute-force protection using rate limiting
- Dockerized deployment (no host dependency pollution)
- Privacy-aware design (biometric data excluded from GitHub)

---

## System Architecture

Browser (Webcam)  
↓  
JavaScript (getUserMedia)  
↓  
Flask Web Server (Docker)  
↓  
OpenCV + dlib (Face Encoding)  
↓  
Face Matching  
↓  
Authentication Result  

---

## Technology Stack

| Component | Technology |
|---------|-----------|
| Backend | Python, Flask |
| Face Recognition | dlib, face_recognition |
| Image Processing | OpenCV |
| Frontend | HTML, JavaScript |
| Security | Flask-Limiter |
| Containerization | Docker / Podman |
| OS Tested | Kali Linux (VM) |

---


