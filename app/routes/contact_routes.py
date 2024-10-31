from flask import Blueprint, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..config import Config

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/api/contact', methods=['POST'])
def submit_contact():
    try:
        data = request.get_json()
        
        required_fields = ['name', 'email', 'message']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        send_email_notification(data)
        
        return jsonify({"message": "Message sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def send_email_notification(data):
    msg = MIMEMultipart()
    msg['From'] = Config.SMTP_USERNAME
    msg['To'] = Config.NOTIFICATION_EMAIL
    msg['Subject'] = f"Portfolio Contact: {data['name']}"
    
    body = f"""
    New contact form submission:
    
    Name: {data['name']}
    Email: {data['email']}
    Message: {data['message']}
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT) as server:
        server.starttls()
        server.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
        server.send_message(msg)