from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Birthday Wisher Backend Running"}