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
        "summary": "Full-Stack Developer with strong foundations in JavaScript, React, Ruby on Rails, and Python Flask, combining analytical thinking with creative problem-solving to deliver efficient web solutions. Leveraging intensive bootcamp training and prior data analysis experience to build scalable, user-centric software applications.",
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
                "Completed 500+ hours of intensive coding practice and project-based learning.", "Participated in daily code reviews and pair programming sessions with peers.", "Contributed to collaborative projects using git workflow and agile methodologies.", "Developed and presented three full-stack applications during the program."
            ]
        },
        {
            "company": "Clover Food Lab",
            "position": "Operations Specialist",
            "period": "2023 - 2024",
            "achievements": [
                "Served as shift lead, effectively delegating daily tasks and responsibilities to team members.", "Demonstrated strong leadership and problem-solving abilities through effective team communication and operational decision-making."
            ]
        },
        {
            "company": "Berklee College of Music",
            "position": "Bachelor of Music",
            "period": "2020 - 2023",
            "achievements": [
                "Developed strong analytical thinking, attention to detail, and project management skills through complex musical analysis and ensemble work.", "Developed collaboration and adaptability skills through diverse ensemble performances and cross-cultural musical projects."
            ]
        },
        {
            "company": "Santa Rosa Symphony",
            "position": "Teaching Assistant",
            "period": "2017 - 2020",
            "achievements": [
                "Managed educational program data and coordinated digital resources for 50+ students.", "Developed clear communication skills through teaching complex musical concepts."
            ]
        }
    ]
    return jsonify(experience_data)

@main_bp.route('/api/skills', methods=['GET'])
def get_skills():
    skills_data = {
        "technical": {
            "languages_frameworks": [ "React.js", "Vue.js", "Next.js", "TypeScript", "Redux", "Tailwind CSS", "HTML", "Chart.js"],
            "data": ["Node.js", "Ruby on Rails", "Python Flask"],
            "tools": ["PostgreSQL", "Redis", "Docker", "Git", "JWT", "Jest", "RSPec", "Swagger", "Railway", "CI/CD"]
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
        {"id": 1,
            "title": "Music Artist Analytics Dashboard",
            "description": "Analytics dashboard integrating Spotify and YouTube APIs with Redis caching and rate limiting, featuring responsive artist search with auto-complete, and cross-platform statistics comparison.",
            "technologies": ["Next.js", "Node.js", "Typescript", "Redis", "React Query", "Recharts"],
            "frontend_github_link": "https://github.com/Jai-Dhiman/resonance-frontend",
            "backend_github_link": "https://github.com/Jai-Dhiman/resonance-api",
            "live_link": "https://artistanalytics.up.railway.app/",
            "image_url": "/static/uploads/ArtistAnalytics.png"
        },
        {
            "id": 2,
            "title": "Legacy Stories Blog Platform",
            "description": "Accessible blogging platform with rich text editing made for my grandpa’s life stories. Containerized with Docker, deployed on Railway and has comprehensive test coverage.",
            "technologies": ["Vue.js", "Ruby on Rails", "TypeScript", "Docker", "PostgreSQL", "Tailwind CSS"],
            "frontend_github_link": "https://github.com/Jai-Dhiman/badeblog-frontend",
            "backend_github_link": "https://github.com/Jai-Dhiman/badeblog-api",
            "live_link": "https://myideasmywords.up.railway.app/",
            "image_url": "/static/uploads/BadeBlog.png"
        },
        {
            "id": 3,
            "title": "Personal Portfolio Website",
            "description": "Responsive portfolio website with Flask REST API backend, containerized deployment, and automated build processes.",
            "technologies": [ "React.js", "Python Flask", "RESTful API", "Responsive Design", "Docker"],
            "frontend_github_link": "https://github.com/Jai-Dhiman/portfolio-frontend",
            "backend_github_link": "https://github.com/Jai-Dhiman/portfolio-api", "live_link": "https://jaidhimanportfolio.up.railway.app",
            "image_url": "/static/uploads/PortfolioImage.png"
        }
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
        'frontend_github_link': project.frontend_github_link,
        'backend_github_link': project.backend_github_link,
        'live_link': project.live_link,
        'image_url': project.image_url
    })