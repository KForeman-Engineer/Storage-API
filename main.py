
import os

from fastapi import FastAPI
from Services.FileService import FileService

app = FastAPI()
Fileserv = FileService(os.getcwd())

# -- FILE AND FOLDER RETRIEVAL ENDPOINTS --
@app.get("/api/v1/file")
def get_file():
    return Fileserv.getfiles()

@app.get("/api/v1/all")
def get_all():
    return Fileserv.GetAll()

@app.get("/api/v1/folder")
def get_folder():
    return Fileserv.getfolders()

