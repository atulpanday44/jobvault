import pytest
from my_app import create_app, db as _db

@pytest.fixture(scope='session')
def app():
    app = create_app('testing')
    with app.app_context():
        yield app

@pytest.fixture(scope='session')
def db():
    with app().app_context():
        _db.create_all()
        yield _db
        _db.drop_all()

@pytest.fixture()
def client():
    app_instance = app()
    with app_instance.test_client() as client:
        yield client

@pytest.fixture()
def test_user():
    user = User(username='testuser', email='testuser@example.com')
    db.session.add(user)
    db.session.commit()
    yield user
    db.session.delete(user)
    db.session.commit()