import os

from fastapi import FastAPI
from Services.FileService import FileService

app = FastAPI()
Fileserv = FileService(os.getcwd())

# -- FILE AND FOLDER RETRIEVAL ENDPOINTS --
@app.get("/api/v1/file")
def get_file():
    return Fileserv.getfiles()

@app.get("/api/v1/folder")
def get_folder():
    return Fileserv.getfolders()

@app.get("/api/v1/file/{file_id}/meta")
def get_file_meta(file_id: str):
    return {"message": f"This is a placeholder for file {file_id} metadata retrieval."}

@app.get("/api/v1/folder/{folder_id}/meta")
def get_folder_meta(folder_id: str):
    return {"message": f"This is a placeholder for folder {folder_id} metadata retrieval."}

@app.get("/api/v1/folder/{folder_id}/content")
def get_folder_content(folder_id: str):
    return {"message": f"This is a placeholder for folder {folder_id} content retrieval."}



# -- FILE AND FOLDER CREATION ENDPOINTS --
@app.post("/api/v1/file")
def create_file():
    return {"message": "This is a placeholder for file creation."}

@app.post("/api/v1/folder")
def create_folder():
    return {"message": "This is a placeholder for folder creation."}


# -- FILE AND FOLDER UPDATE ENDPOINTS --
@app.put("/api/v1/file/{file_id}")
def update_file(file_id: str):
    return {"message": f"This is a placeholder for updating file {file_id}."}

@app.put("/api/v1/folder/{folder_id}")
def update_folder(folder_id: str):
    return {"message": f"This is a placeholder for updating folder {folder_id}."}


# -- FILE AND FOLDER DELETION ENDPOINTS --
@app.delete("/api/v1/file/{file_id}")
def delete_file(file_id: str):
    return {"message": f"This is a placeholder for deleting file {file_id}."}

@app.delete("/api/v1/folder/{folder_id}")
def delete_folder(folder_id: str):
    return {"message": f"This is a placeholder for deleting folder {folder_id}."}