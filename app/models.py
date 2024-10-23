from pydantic import BaseModel, HttpUrl
from enum import Enum


class CandidateLevel(str, Enum):
    junior = "Junior"
    middle = "Middle"
    senior = "Senior"


class ReviewRequest(BaseModel):
    assignment_description: str
    github_repo_url: HttpUrl
    candidate_level: CandidateLevel
