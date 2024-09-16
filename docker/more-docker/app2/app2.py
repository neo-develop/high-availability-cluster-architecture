from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/app1")
async def root():
    return {"code": 200, "result": "App 2-1"}
    
@app.get("/app2")
async def root():
    return {"code": 200, "result": "App 2-2"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
