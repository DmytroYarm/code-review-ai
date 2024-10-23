TEST_DATA = {
    "main": {
        "url": "/",
        "exp_text": "This is creative frontend!"
    },
    "review_code": {
        "github_url": "https://api.github.com/repos/DmytroYarm/abs-bot",
        "candidate_level": "Junior",
        "description": "Lorem ipsum test"
    },
    "fetch_github_repo_success": {
        "github_url": "https://api.github.com/repos/DmytroYarm/abs-bot",
    },
    "fetch_github_repo_wrong_token": {
        "github_url": "https://api.github.com/repos/DmytroYarm/abs-bot",
        "wrong_token": "111qqqqwwwweeerrrtttyyy222",
        "error_trext": '{"message":"Bad credentials","documentation_url":"https://docs.github.com/rest","status":"401"}'
    },
    "fetch_github_repo_wrong_url": {
        "github_url": "https://api.github.com/repos/DmytroYarm/abs-boot",
        "error_trext": '{"message":"Not Found","documentation_url":"https://docs.github.com/rest/repos/repos#get-a-repository","status":"404"}'
    }
}
