from flask import Blueprint, jsonify
from datetime import datetime
from ..models import Project

main_bp = Blueprint('main', __name__)

@main_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }), 200

@main_bp.route('/api/about', methods=['GET'])
def get_about():
    about_data = {
        "name": "Jai Dhiman",
        "title": "Full-Stack Web Developer",
        "location": "San Francisco, CA",
        "summary": "Full-Stack Web Developer with strong foundations in JavaScript, React, Ruby on Rails, and Python Flask. Successfully completed 500+ hours of intensive software development training at Actualize Coding Bootcamp, building multiple full-stack applications. Demonstrates exceptional ability to master new technologies, evidenced by Microsoft certifications in data analytics. Combines analytical thinking with creative problem-solving skills developed through a Bachelor's in Music Performance to deliver efficient, user-centric web solutions.",
        "key_skills": [
            "Full Stack Problem Solving",
            "Data Driven Development",
            "Attention to Detail",
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
        },
        {
            "company": "Santa Rosa Symphony",
            "position": "Teaching Assistant",
            "period": "2017 - 2020",
            "achievements": [
                "Served as a teaching assistant for youth music programs, supporting the musical development of over 50 students aged 8-16 annually.",
                "Coordinated logistics for 4 annual performances, ensuring smooth execution of events attended by up to 1,000 patrons."
            ]
        }
    ]
    return jsonify(experience_data)

@main_bp.route('/api/skills', methods=['GET'])
def get_skills():
    skills_data = {
        "technical": {
            "languages_frameworks": ["JavaScript", "React.js", "Ruby", "Ruby on Rails", "HTML", "CSS", "SQL", "Python", "Flask"],
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
            "github_link": "https://github.com/Jai-Dhiman/ScoreSnap-api",
            # "live_link": "YOUR_LIVE_LINK",
            "image_url": "/static/uploads/ScoreSnap.png"
        },
        # {
        #     "id": 2,
        #     "title": "Sales Performance Dashboard",
        #     "description": "Comprehensive sales performance dashboard using Power BI",
        #     "technologies": ["Power BI", "DAX", "M", "SQL"],
        #     "github_link": "YOUR_GITHUB_LINK",
        #     # "live_link": "YOUR_LIVE_LINK"
        # }
    ]
    return jsonify(projects), 200

@main_bp.route('/api/projects/<int:project_id>', methods=['GET'])
def get_project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify({
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'technologies': project.technologies,
        'github_link': project.github_link,
        # 'live_link': project.live_link,
        'image_url': project.image_url
    })