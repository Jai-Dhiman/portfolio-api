import pytest
from app.models import Project, db
from datetime import datetime

def test_project_model(app):
    with app.app_context():

        project = Project(
            title="Test Project",
            description="Test Description",
            technologies=["Python", "Flask"],
            github_link="https://github.com/test",
            live_link="https://test.com",
            image_url="test.jpg"
        )
        
        db.session.add(project)
        db.session.commit()
        
        saved_project = Project.query.filter_by(title="Test Project").first()
        assert saved_project is not None
        assert saved_project.description == "Test Description"
        assert "Python" in saved_project.technologies
