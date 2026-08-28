# 🩸 BloodLink AI

<div align="center">

### AI-Powered Blood Donor Matching & Emergency Response Platform

*Connecting lifesavers with those who need them most.*

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web_App-black)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Frontend-38BDF8)
![AI Powered](https://img.shields.io/badge/AI-Powered-red)

</div>

---

## Overview

BloodLink AI is an intelligent blood donor matching and emergency response platform designed to connect blood donors, patients, and hospitals during critical situations.

Instead of manually searching for donors, users can simply describe their blood requirements in natural language. The AI agent automatically understands the request, extracts important information, identifies compatible blood groups, finds nearby donors, ranks them by distance, and sends emergency notifications.

The goal of BloodLink AI is to reduce the time required to locate blood donors and make emergency blood coordination faster, smarter, and more accessible.

---

## Features

### AI Blood Request Understanding

Users can request blood using natural language.

Example:

```text
Need A+ blood urgently at Apollo Hospital Chennai.
```

The AI automatically extracts:

* Blood Group
* Hospital Name
* Location
* Urgency Level

---

### Smart Donor Matching

BloodLink AI automatically:

* Identifies compatible blood groups
* Searches nearby donors
* Filters available donors
* Ranks donors by distance

Example:

```text
1. Ravi Kumar — 1.2 km
2. Priya S — 2.4 km
3. Arun K — 4.8 km
```

---

### Blood Compatibility Engine

The platform automatically determines compatible donors based on blood type.

Example:

```text
Patient Blood Group: A+

Compatible Donors:
A+
A-
O+
O-
```

---

### Location-Based Search

Using geolocation services, BloodLink AI:

* Detects hospital coordinates
* Calculates donor distances
* Finds nearest available donors
* Displays results sorted by proximity

---

### Emergency Notification System

The platform automatically sends alerts to compatible donors.

Example:

```text
BLOOD REQUEST

Blood Group: A+

Hospital: Apollo Hospital Chennai

Contact Number: 9876543210

Please respond if available.
```

Notifications can be delivered through:

* SMS
* Email
* WhatsApp (Future Enhancement)

---

### Direct Donor Contact

Recipients can:

* View nearby donors
* See donor distance from the hospital
* Contact donors directly
* Track donor responses

---

### Live Request Tracking

Monitor requests in real time.

Example:

```text
Notifications Sent : 20

Accepted : 4

Pending : 16

Nearest Donor :
Ravi Kumar (1.2 km)
```

---

## AI Agent Workflow

```text
User Request
      │
      ▼

Need O+ blood urgently at Apollo Hospital

      │
      ▼

NLP Agent Extracts Information

      │
      ▼

Compatibility Agent Finds Valid Donors

      │
      ▼

Distance Agent Calculates Nearby Matches

      │
      ▼

Donors Ranked By Distance

      │
      ▼

Notification Agent Sends Alerts

      │
      ▼

User Receives Donor List & Responses
```

---

## System Architecture

```text
                     Users
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼

      Donors        Patients       Hospitals

        └───────────────┬───────────────┘
                        │

                 Flask Web Application
                        │

                  BloodLink AI
                        │

      ┌──────────┬──────────┬──────────┬──────────┐
      │          │          │          │

 NLP Agent  Compatibility  Distance  Notification
              Agent         Agent      Agent

      └──────────┴──────────┴──────────┴──────────┘
                        │

                  MySQL Database
                        │

              Maps • SMS • Email
```

---

## Tech Stack

### Frontend

* HTML5
* Tailwind CSS
* JavaScript

### Backend

* Python
* Flask

### Database

* MySQL

### AI Components

* OpenAI API / Ollama
* Natural Language Processing
* Blood Compatibility Engine
* Distance-Based Donor Ranking

### Location Services

* Geopy
* Nominatim

### Notifications

* Twilio SMS
* SMTP Email Service

---

## Project Structure

```text
bloodlink-ai/
│
├── app.py
│
├── routes/
│   ├── auth.py
│   ├── donor.py
│   ├── request.py
│
├── agents/
│   ├── nlp_agent.py
│   ├── compatibility_agent.py
│   ├── distance_agent.py
│   ├── notification_agent.py
│
├── models/
│
├── templates/
│
├── static/
│
├── database/
│
└── README.md
```

---

## Future Enhancements

* Voice-Based Blood Requests
* WhatsApp Integration
* Interactive Donor Maps
* AI Availability Prediction
* Hospital Dashboard
* Blood Demand Analytics
* Multi-Agent Coordination
* Real-Time Emergency Monitoring

---

## Mission

Every second matters during a medical emergency.

BloodLink AI aims to bridge the gap between blood donors and recipients using Artificial Intelligence, helping patients find compatible donors faster and making blood donation more efficient for everyone.

---

<div align="center">

### Donate Blood • Save Lives • Empower Communities

Built with Flask, MySQL, Tailwind CSS, and Artificial Intelligence.

</div>
