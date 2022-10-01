from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def home(request: Request):
    return {"msg":"NASA SpaceApp Challenge!"}