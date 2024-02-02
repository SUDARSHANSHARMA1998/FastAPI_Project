from fastapi import FastAPI
from routes.route import router
from database import db
app = FastAPI()

app.include_router(router, tags=["CosmoCloud"], prefix="/ecommerce")

@app.get("/")
def root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

