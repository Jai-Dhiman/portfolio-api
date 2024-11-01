from flask import Blueprint, request, jsonify, current_app
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..config import Config
import logging

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/api/contact', methods=['POST'])
def submit_contact():
    try:
        data = request.get_json()
        
        required_fields = ['name', 'email', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({"error": f"Missing required field: {field}"}), 400

        if not current_app.config.get('TESTING'):
            try:
                send_email_notification(data)
            except Exception as e:
                logging.error(f"Email sending failed: {str(e)}")
                
        return jsonify({"message": "Message received successfully"}), 200
        
    except Exception as e:
        logging.error(f"Contact submission error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

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