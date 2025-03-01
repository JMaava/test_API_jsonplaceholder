import httpx
import pytest
import os
from dotenv import load_dotenv
from schemas.post_schema import Post

# загрузка переменных окружения
load_dotenv()


@pytest.fixture(scope='session')
def base_url():
    return os.getenv('BASE_URL')


@pytest.fixture(scope='session')
def http_client():
    with httpx.Client() as client:
        yield client


@pytest.fixture(scope='function')
def create_post(base_url, http_client):
    data = {
        "userId": 1,
        "title": "Test Title",
        "body": "Test Body"
    }
    response = http_client.post(f"{base_url}/posts", json=data)
    assert response.status_code == 201
    post = Post(**response.json())
    yield post

    response = http_client.delete(f"{base_url}/posts/{post.id}")
    assert response.status_code == 200
    # проверить, что пост удален (не работает на тестовом ресурсе)
    # get_response = http_client.get(f"{base_url}/posts/{post.id}")
    # assert get_response.status_code == 404
