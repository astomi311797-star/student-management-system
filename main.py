from fastapi import FastAPI
import user
from database import engine
from routes import user_controller1
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.responses import FileResponse


BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / "static"
user.base.metadata.create_all(bind= engine)



app = FastAPI(title= "Student Management System")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html") 


app.include_router(user_controller1.router)


# app.include_router(user_controller1.router_new)