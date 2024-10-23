import aiohttp
import redis.asyncio as aioredis
from openai import OpenAI
from fastapi import HTTPException
import json

from app.config import Config


redis = None

async def init_redis():
    global redis
    redis = await aioredis.from_url(Config.REDIS_URL)


async def fetch_github_repo(github_url: str, github_token: str):
    cache_key = f"github_repo:{github_url}"
    cached_data = await redis.get(cache_key)

    if cached_data:
        return json.loads(cached_data)

    headers = {"Authorization": f"token {github_token}"}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(f"{github_url}/contents", ssl=False) as response:
            if response.status != 200:
                raise HTTPException(status_code=500, detail="Error fetching repository.")    #TODO add other errors
            repo_data = await response.json()
            await redis.set(cache_key, json.dumps(repo_data), ex=3600)
            return repo_data


async def analyze_code_with_openai(prompt: str, openai_api_key: str):
    client = OpenAI()
    client.api_key = openai_api_key
    try:
        completion = client.chat.completions.create(
            model="gpt-4-0613",    #TODO check model
            messages=[{"role": "system", "content": prompt}]
        )
        return completion.choices[0].message
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing code. {e}")   #TODO add other errors
