from fastapi import APIRouter, HTTPException
from models import ReviewRequest
from services import fetch_github_repo, analyze_code_with_openai
import os

router = APIRouter()


@router.post("/review")
async def review_code(review_request: ReviewRequest):
    github_token = os.getenv("GITHUB_TOKEN")

    if not github_token:
        raise HTTPException(status_code=500, detail="GitHub token not configured.")

    repo_data = await fetch_github_repo(review_request.github_repo_url, github_token)

    file_list = [f['name'] for f in repo_data if f['type'] == 'file']
    prompt = (f"Analyze the following files for a {review_request.candidate_level} "
              f"candidate: {file_list}. Describe code quality, potential issues, and improvements.")

    gpt_response = await analyze_code_with_openai(prompt)

    return {
        "found_files": file_list,
        "downsides_comments": gpt_response,
        "rating": "To be implemented based on analysis"
    }
