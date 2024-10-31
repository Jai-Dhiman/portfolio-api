from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# app/routes/main_routes.py
from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/api/about', methods=['GET'])
def get_about():
    about_data = {
        "name": "Jai Dhiman",
        "title": "Full-Stack Web Developer",
        "location": "San Francisco, CA",
        "summary": "Full-Stack Web Developer transitioning from a background in data analysis and music...",
        "key_skills": [
            "Full Stack Development",
            "Data Analytics",
            "UI/UX Design",
            "Process Optimization",
            "Software Quality Assurance"
        ]
    }
    return jsonify(about_data)

@main_bp.route('/api/experience', methods=['GET'])
def get_experience():
    experience_data = [
        {
            "company": "Actualize Coding Bootcamp",
            "position": "Full-Stack Web Development",
            "period": "2024",
            "achievements": [
                "Mastered a comprehensive tech stack including JavaScript, React.js, Ruby, and SQL",
                "Developed and deployed full-stack web applications",
                "Utilized version control systems like Git and GitHub"
            ]
        },
        {
            "company": "Clover Food Lab",
            "position": "Operations Specialist",
            "period": "2023 - 2024",
            "achievements": [
                "Managed daily operations in a high-volume food service environment",
                "Collaborated with a team of 8 to optimize food preparation processes",
                "Trained and mentored 5 new team members"
            ]
        }
    ]
    return jsonify(experience_data)

@main_bp.route('/api/skills', methods=['GET'])
def get_skills():
    skills_data = {
        "technical": {
            "languages_frameworks": ["JavaScript", "React.js", "Ruby", "Ruby on Rails", "HTML", "CSS", "SQL"],
            "data": ["PostgreSQL", "Power BI"],
            "tools": ["Visual Studio Code", "Git", "GitHub", "Power Platform"]
        },
        "certifications": [
            "Microsoft Certified: PL-300 Power BI Data Analyst Associate",
            "Microsoft Certified: PL-900 Power Platform Fundamentals"
        ]
    }
    return jsonify(skills_data)

@main_bp.route('/api/projects', methods=['GET'])
def get_projects():
    projects = [
        {
            "id": 1,
            "title": "PDF/JPG to MusicXML Converter",
            "description": "Web application that converts PDF or JPG sheet music files into MusicXML format",
            "technologies": ["React", "Ruby on Rails", "Audiveris", "OCR"],
            "github_link": "YOUR_GITHUB_LINK",
            "live_link": "YOUR_LIVE_LINK"
        },
        {
            "id": 2,
            "title": "Sales Performance Dashboard",
            "description": "Comprehensive sales performance dashboard using Power BI",
            "technologies": ["Power BI", "DAX", "M", "SQL"],
            "github_link": "YOUR_GITHUB_LINK",
            "live_link": "YOUR_LIVE_LINK"
        }
    ]
    return jsonify(projects), 200