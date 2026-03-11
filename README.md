# The Sales Insight Automator

An AI-powered web application that analyzes uploaded sales data and automatically generates insights using an LLM. The generated summary is then sent to a specified email address.

## Tech Stack

Frontend: React  
Backend: FastAPI (Python)  
LLM: Groq (Llama 3 / Llama 3.1)  
Email: SMTP (Gmail App Password)  
Deployment: Vercel (Frontend) + Render (Backend)

---

# Features

- Upload CSV or Excel sales datasets
- AI-generated insights
- Sales trend analysis
- Top-performing products detection
- Regional performance insights
- Automated email delivery
- Simple web interface

---

# Project Structure

```
sales-insight-automator
│
├── backend
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend
│   ├── package.json
│   ├── public
│   │   └── index.html
│   └── src
│       ├── App.js
│       └── index.js
│
├── .gitignore
└── README.md
```

---

# Prerequisites

Install before running the project:

- Python 3.10+
- Node.js
- npm
- Groq API Key
- Gmail account with App Password enabled

---

# Environment Variables

Create file:

```
backend/.env
```

Example:

```
GROQ_API_KEY=your_groq_api_key

SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_app_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

---

# Backend Setup

Navigate to backend folder:

```
cd backend
```

Create virtual environment:

```
python -m venv venv
```

Activate environment (Windows):

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run backend server:

```
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

Swagger docs:

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Open new terminal.

Navigate to frontend:

```
cd frontend
```

Install dependencies:

```
npm install
```

Run frontend:

```
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

# Example CSV Dataset

```
Product,Region,Revenue,Units_Sold
Phone,North,120000,120
Laptop,West,90000,40
Headset,East,12000,80
Charger,North,8000,400
```

Upload this file through the interface.

---

# Application Workflow

```
User uploads CSV/XLSX
        ↓
React Frontend sends file to API
        ↓
FastAPI backend processes dataset
        ↓
Dataset summary sent to Groq LLM
        ↓
AI generates sales insights
        ↓
Backend emails the report
```

---

# Deployment

## Backend (Render)

Build command

```
pip install -r requirements.txt
```

Start command

```
uvicorn main:app --host 0.0.0.0 --port 10000
```

Add environment variables in Render dashboard.

---

## Frontend (Vercel)

1. Import GitHub repository
2. Select frontend directory
3. Deploy

Update API URL in `App.js` to the Render backend URL.

---

# Example Output Email

```
Sales Insight Report

Key Trends
Electronics category dominates revenue
North region shows highest sales performance

Top Products
Phone
Laptop

Recommendations
Increase inventory of electronics
Expand marketing in West region
Analyze low-performing categories
```

---

# Security

- `.env` excluded via `.gitignore`
- API keys stored as environment variables
- No secrets committed to repository
- Gmail App Password used instead of account password

---

# Future Improvements

- Dashboard charts
- Authentication
- File upload progress
- Database integration
- Scheduled reports
- Advanced analytics

---

# Author

Arshit Kataria

---

# License

Educational and demonstration project.