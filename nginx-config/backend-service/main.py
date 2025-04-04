from fastapi import FastAPI, Header, HTTPException
from typing import Optional

app = FastAPI()

@app.get("/")
async def read_root(mode: Optional[str] = Header(None)):
    if mode != "autopilot":
        raise HTTPException(
            status_code=400,
            detail="Missing or invalid 'mode' header. Must be set to 'autopilot'"
        )
    
    return {"message": "Hello from backend-service!", "mode": mode}