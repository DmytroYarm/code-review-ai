from fastapi import APIRouter, HTTPException

from app.config import Config
from app.models import ReviewRequest
from app.services import fetch_github_repo, analyze_code_with_openai

router = APIRouter()


@router.post("/review")
async def review_code(review_request: ReviewRequest):
    github_token = Config.GITHUB_TOKEN
    openai_api_key = Config.OPENAI_API_KEY

    if not github_token:
        raise HTTPException(status_code=500, detail="GitHub token not configured.")

    repo_data = await fetch_github_repo(review_request.github_repo_url, github_token)

    file_list = [f['name'] for f in repo_data if f['type'] == 'file']
    prompt = (f"Analyze the following files for a {review_request.candidate_level} "
              f"candidate: {file_list}. Describe code quality, potential issues, and improvements.")

    gpt_response = await analyze_code_with_openai(prompt, openai_api_key)

    return {
        "found_files": file_list,
        "downsides_comments": gpt_response,
        "rating": "To be implemented based on analysis"
    }
