from fastapi.testclient import TestClient

from app.config import Config
from app.main import app
from test.methods import AllMethod
import pytest
import httpx
from fastapi import HTTPException
from app.services import fetch_github_repo

# from test.step_check import StepCheck


class TestMain:
    github_token = Config.GITHUB_TOKEN
    openai_api_key = Config.OPENAI_API_KEY
    github_url = review_request.github_repo_url

    @pytest.fixture(autouse=True)
    def client(self):
        """Создаем тестовый клиент FastAPI для всех тестов."""
        self.client = TestClient(app)

    @pytest.mark.main
    def test_main_page(self):
        """Main page testing."""
        url, exp_text = AllMethod.extract_test_data("main")
        response = self.client.get(url)
        assert response.status_code == 200
        assert response.json() == {"message": f"{exp_text}"}

    @pytest.mark.asyncio
    async def test_fetch_github_repo_success(self):
        response = await fetch_github_repo(github_url, self.github_token)

        # Проверка структуры JSON-ответа
        assert isinstance(response, list)
        assert len(response) > 0  # Проверяем, что получен не пустой список
        assert "name" in response[0]
        assert "path" in response[0]
        assert "sha" in response[0]
        assert "size" in response[0]
        assert "url" in response[0]
        assert "type" in response[0]

    @pytest.mark.asyncio
    async def test_fetch_github_repo_failure(self):
        # Подготовка
        github_url = "https://api.github.com/repos/username/repo"  # замените на ваш репозиторий
        github_token = "invalid_token"  # некорректный токен для тестирования

        # Выполнение тестируемого метода и проверка исключения
        with pytest.raises(HTTPException) as exc_info:
            await fetch_github_repo(github_url, github_token)

        assert exc_info.value.status_code == 500
        assert exc_info.value.detail == "Error fetching repository."
