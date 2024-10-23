from fastapi import FastAPI
from app.routes import router
from app.services import init_redis

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await init_redis()


@app.get("/")
async def read_root():
    return {"message": "This is creative frontend!"}

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
