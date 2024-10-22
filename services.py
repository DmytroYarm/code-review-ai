import aiohttp
import openai
from fastapi import HTTPException
import os


async def fetch_github_repo(github_url: str, github_token: str):
    headers = {"Authorization": f"token {github_token}"}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(f"{github_url}/contents") as response:
            if response.status != 200:
                raise HTTPException(status_code=500, detail="Error fetching repository.")
            return await response.json()


async def analyze_code_with_openai(prompt: str):
    try:
        response = await openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error analyzing code.")
