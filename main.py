import fastapi as api
from src.routes import router as apis


app = api.FastAPI()

app.include_router(apis)


@app.get('/')
async def helloWorld():
    return 'helloWorld'
