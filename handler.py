import json
from email.mime.text import MIMEText
import smtplib
import os
from urllib.parse import parse_qs
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Serve HTML form
def home(event, context):
    html_form = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Send Email</title>
    </head>
    <body>
        <h2>Send Email</h2>
        <form action="/dev/send-email" method="POST">
            <label for="receiver_email">To:</label><br>
            <input type="" name="receiver_email" ><br><br>
            
            <label for="subject">Subject:</label><br>
            <input type="text" name="subject" ><br><br>
            
            <label for="body_text">Message:</label><br>
            <textarea name="body_text" ></textarea><br><br>
            
            <button type="submit">Send</button>
        </form>
    </body>
    </html>
    """
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html"},
        "body": html_form
    }

# Handle form submission
def send_email(event, context):
    try:
        body = event.get("body")

        if not body:
            return {"statusCode": 400, "body": json.dumps({"error": "No data received"})}

        # Parse form-data (browser sends it as query string)
        parsed = parse_qs(body)
        receiver_email = parsed.get("receiver_email", [""])[0]
        subject = parsed.get("subject", [""])[0]
        body_text = parsed.get("body_text", [""])[0]

        if not receiver_email or not subject or not body_text:
            return {"statusCode": 400, "body": json.dumps({"error": "All fields are required"})}

        # SMTP settings from .env
        sender_email = os.getenv("EMAIL_USER")
        password = os.getenv("EMAIL_PASS")

        if not sender_email or not password:
            return {"statusCode": 500, "body": json.dumps({"error": "Email credentials not set in .env"})}

        msg = MIMEText(body_text)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = receiver_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.send_message(msg)

        return {"statusCode": 200, "body": json.dumps({"message": f"Email sent to {receiver_email} successfully!"})}

    except smtplib.SMTPAuthenticationError:
        return {"statusCode": 401, "body": json.dumps({"error": "Authentication failed. Check your EMAIL_USER and EMAIL_PASS."})}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
