import pytest
import json

def test_about_route(client):
    response = client.get('/api/about')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['name'] == "Jai Dhiman"
    assert data['title'] == "Full-Stack Web Developer"

def test_experience_route(client):
    response = client.get('/api/experience')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data) > 0
    assert 'company' in data[0]

def test_skills_route(client):
    response = client.get('/api/skills')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'technical' in data
    assert 'certifications' in data

def test_contact_route(client):
    test_data = {
        "name": "Test User",
        "email": "test@test.com",
        "message": "Test message"
    }
    response = client.post('/api/contact', 
                          json=test_data)  
    assert response.status_code == 200
    assert response.json['message'] == "Message received successfully"

def test_contact_route_invalid_data(client):
    test_data = {
        "name": "Test User",
    }
    response = client.post('/api/contact', 
                          json=test_data)
    assert response.status_code == 400
    assert 'error' in response.json