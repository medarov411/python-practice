from fastapi import FastAPI
from fastapi import Form
from fastapi.responses import FileResponse
app= FastAPI()
@app.get("/")
def root():
    return FileResponse("index.html")
@app.post("/postdata")
def postdata(username:str = Form(),
languages:list = Form()):
    return {"name": username, "languages": languages}
