from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/app1")
async def root():
    return {"code": 200, "result": "App 1-1"}

@app.get("/app2")
async def root():
    return {"code": 200, "result": "App 1-2"}

@app.get("/app3")
async def root():
    return {"code": 200, "result": "App 1-3"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
