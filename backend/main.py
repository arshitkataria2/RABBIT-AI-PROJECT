from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from groq import Groq
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_summary(data):

    prompt = f"""
    Analyze this sales dataset summary and give insights:

    {data}

    Provide:
    - Key trends
    - Top performing products
    - Best regions
    - Suggestions to improve sales
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    return completion.choices[0].message.content


def send_email(recipient, summary):

    msg = EmailMessage()
    msg["Subject"] = "Sales Insights Report"
    msg["From"] = os.getenv("SMTP_EMAIL")
    msg["To"] = recipient
    msg.set_content(summary)

    with smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT"))) as server:
        server.starttls()
        server.login(os.getenv("SMTP_EMAIL"), os.getenv("SMTP_PASSWORD"))
        server.send_message(msg)


@app.post("/upload")
async def upload(file: UploadFile = File(...), email: str = Form(...)):

    if file.filename.endswith(".csv"):
        df = pd.read_csv(file.file)
    else:
        df = pd.read_excel(file.file)

    summary_data = df.describe(include='all').to_string()

    ai_summary = generate_summary(summary_data)

    send_email(email, ai_summary)

    return {
        "message": "Summary generated and emailed",
        "summary": ai_summary
    }