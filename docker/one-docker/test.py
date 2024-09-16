from fastapi import FastAPI

app = FastAPI()

@app.get("/app1")
async def root():
    return {"code": 200, "result": "App"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
