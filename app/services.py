import aiohttp
from openai import OpenAI
from fastapi import HTTPException
import os


async def fetch_github_repo(github_url: str, github_token: str):
    headers = {"Authorization": f"token {github_token}"}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(f"{github_url}/contents", ssl=False) as response:
            if response.status != 200:
                raise HTTPException(status_code=500, detail="Error fetching repository.")
            return await response.json()


async def analyze_code_with_openai(prompt: str, openai_api_key: str):
    client = OpenAI()
    client.api_key = openai_api_key
    try:
        completion = client.chat.completions.create(
            model="gpt-4-0613",
            messages=[{"role": "system", "content": prompt}]
        )
        return completion.choices[0].message
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing code. {e}")
