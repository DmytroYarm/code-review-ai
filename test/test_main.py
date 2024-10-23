import pytest
import httpx

from app.config import Config
from test.setting_local import BASE_URL

from test.methods import AllMethod


class TestMain:

    @pytest.mark.main
    def test_main_page(self):
        url, exp_text = AllMethod.extract_test_data("main")
        """Main page testing FastAPI."""
        response = httpx.get(f"{BASE_URL}/")
        AllMethod.check_response(response, 200)
        assert response.json() == {"message": f"{exp_text}"}


    @pytest.mark.config
    def test_github_token(self):
        """Check GITHUB_TOKEN variable is correct."""
        assert Config.GITHUB_TOKEN is not None, "GITHUB_TOKEN is not exist"
        assert Config.GITHUB_TOKEN != "", "GITHUB_TOKEN is empty"


    @pytest.mark.config
    def test_openai_api_key(self):
        """Check OPENAI_API_KEY variable is correct."""
        assert Config.OPENAI_API_KEY is not None, "OPENAI_API_KEY is not exist"
        assert Config.OPENAI_API_KEY != "", "OPENAI_API_KEY is empty"


    @pytest.mark.integration
    def test_review_code(self):
        github_url, candidate_level, description = AllMethod.extract_test_data("review_code")
        """POST. Check /review response"""
        request_data = {
            "assignment_description": description,
            "github_repo_url": github_url,
            "candidate_level": candidate_level
        }

        response = httpx.post(f"{BASE_URL}/review", json=request_data)

        AllMethod.check_response(response, 200)

        json_data = response.json()

        assert "found_files" in json_data
        assert "downsides_comments" in json_data
        assert "rating" in json_data
        assert isinstance(json_data["found_files"], list)
        assert isinstance(json_data["downsides_comments"], str)
        assert isinstance(json_data["rating"], str)


    @pytest.mark.integration
    def test_fetch_github_repo_success(self):
        """Check GitHub API response"""
        github_url, = AllMethod.extract_test_data("fetch_github_repo_success")
        headers = {"Authorization": f"token {Config.GITHUB_TOKEN}"}
        response = httpx.get(github_url, headers=headers)

        AllMethod.check_response(response, 200)

        json_data = response.json()

        assert isinstance(json_data, dict), f"Expected a list but got {type(json_data)}. Response: {json_data}"
        assert len(json_data) > 0
        assert "full_name" in json_data
        assert "owner" in json_data

        #TODO check all required keys


    @pytest.mark.integration
    def test_fetch_github_repo_wrong_token(self):
        """Check GitHub API response by wrong token"""
        github_url, wrong_token, error_trext = AllMethod.extract_test_data("fetch_github_repo_wrong_token")
        headers = {"Authorization": f"token {wrong_token}"}
        response = httpx.get(github_url, headers=headers)

        AllMethod.check_response(response, 401)
        assert response.text == error_trext


    @pytest.mark.integration
    def test_fetch_github_repo_wrong_url(self):
        """Check GitHub API response by wrong url"""
        github_url, error_trext = AllMethod.extract_test_data("fetch_github_repo_wrong_url")
        headers = {"Authorization": f"token {Config.GITHUB_TOKEN}"}
        response = httpx.get(github_url, headers=headers)

        AllMethod.check_response(response, 404)
        assert response.text == error_trext
        print(response.text)
