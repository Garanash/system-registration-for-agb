import uvicorn
from fastapi import FastAPI

from contextlib import asynccontextmanager
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    print('dispose engine')
    await db_helper.dispose()

app = FastAPI(description='system registration and authorization for alamzgeobur llc',
              title='ALMAZGEOBUR SystemRegAndAuth',
              content='',
              lifespan=lifespan)


@app.get('/')
def main_page():
    return 'hello on main page'

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)