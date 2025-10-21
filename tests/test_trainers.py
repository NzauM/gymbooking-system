import pytest
from app import app, db, Trainer

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_gym.db'

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Flask App Running Smoothly' in response.data

def test_create_trainer(client):
    test_trainer = {
        "name": "Mercy Nzau",
        "bio": "Certified fitness trainer and yoga instructor.",
        "specialization": "Yoga",
        "phone_number": "0712345678"
    }
    resp = client.post('/create_trainer', json=test_trainer)
    assert resp.status_code == 201
    assert resp.get_json()['success'] == "Trainer Created"
    print("Trainer can be created successfully")