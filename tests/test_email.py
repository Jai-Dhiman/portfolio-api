import pytest
from app.config import Config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def test_email_connection():
    """Test basic email connection and sending"""
    try:
        print(f"\nTesting connection to {Config.SMTP_SERVER}:{Config.SMTP_PORT}")
        
        msg = MIMEMultipart()
        msg['From'] = Config.SMTP_USERNAME
        msg['To'] = Config.NOTIFICATION_EMAIL
        msg['Subject'] = "Test Email"
        msg.attach(MIMEText("This is a test email from pytest", 'plain'))

        with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT, timeout=30) as server:
            print("Connected to server")
            server.set_debuglevel(1)  # This will show the SMTP conversation
            server.starttls()
            print("STARTTLS successful")
            server.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
            print("Login successful")
            server.send_message(msg)
            print("Test email sent successfully!")
            assert True  # If we get here, the test passed

    except Exception as e:
        print(f"Error: {str(e)}")
        pytest.fail(f"Email test failed: {str(e)}")

def test_smtp_connection():
    """Test just the SMTP connection without sending email"""
    try:
        with smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT, timeout=30) as server:
            server.starttls()
            server.login(Config.SMTP_USERNAME, Config.SMTP_PASSWORD)
            assert True
    except Exception as e:
        pytest.fail(f"SMTP connection test failed: {str(e)}")

def test_config_values():
    """Test that all required config values are present"""
    assert Config.SMTP_SERVER, "SMTP_SERVER not configured"
    assert Config.SMTP_PORT, "SMTP_PORT not configured"
    assert Config.SMTP_USERNAME, "SMTP_USERNAME not configured"
    assert Config.SMTP_PASSWORD, "SMTP_PASSWORD not configured"
    assert Config.NOTIFICATION_EMAIL, "NOTIFICATION_EMAIL not configured"