from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel, EmailStr
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = FastAPI()

class EmailNotification(BaseModel):
    recipient: EmailStr
    subject: str
    message: str

SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME", "default_user")
SMTP_PASSWORD_PATH = "/run/secrets/smtp_password"

def send_email(recipient: str, subject: str, message: str):
    with open(SMTP_PASSWORD_PATH, "r", encoding="utf-8") as file:
        smtp_password = file.read().strip()

    try:
        # Настройка MIME сообщения
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Подключение к серверу
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Шифруем соединение
            server.login(SMTP_USERNAME, smtp_password)  # Логинимся на сервере
            server.sendmail(SMTP_USERNAME, recipient, msg.as_string())  # Отправляем письмо
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

@app.post("/notify/")
async def notify(notification: EmailNotification, background_tasks: BackgroundTasks):
    background_tasks.add_task(
        send_email,
        notification.recipient,
        notification.subject,
        notification.message,
    )
    return {"message": "Notification sent in background"}
