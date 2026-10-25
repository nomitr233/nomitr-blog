
import fastapi


app = fastapi.FastAPI()
@app.get("/")
async def root():
    return {"message": "你好"}
