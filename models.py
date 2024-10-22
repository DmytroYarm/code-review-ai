from pydantic import BaseModel, HttpUrl
from enum import Enum

# Определение уровней кандидатов
class CandidateLevel(str, Enum):
    junior = "Junior"
    middle = "Middle"
    senior = "Senior"

# Модель для входных данных
class ReviewRequest(BaseModel):
    assignment_description: str
    github_repo_url: HttpUrl
    candidate_level: CandidateLevel
