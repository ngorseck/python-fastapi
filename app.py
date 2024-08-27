from fastapi import FastAPI
from routers import todo_router

app = FastAPI()

app.include_router(todo_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", port=3000, host="0.0.0.0", reload=True)