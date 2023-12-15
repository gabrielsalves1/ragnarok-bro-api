from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.models import Base
from app.main import app
from app.routes import get_db
import os
import pytest

@pytest.fixture
def client() -> TestClient:
    SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ['TEST_POSTGRES_USER']}:{os.environ['TEST_POSTGRES_PASSWORD']}@{os.environ['TEST_POSTGRES_HOST']}:{os.environ['TEST_POSTGRES_PORT']}/{os.environ['TEST_POSTGRES_DB_NAME']}"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    try:
        Base.metadata.drop_all(bind=engine)
    except:
        pass

    Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    return TestClient(app)

def test_read_main(client):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "Ok", "code": "200", "message": "Ragnarok BRO API - Database https://playragnarokonlinebr.com/database", "result": []}
