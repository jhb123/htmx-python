import tempfile
from typing import Annotated
from fastapi import FastAPI, Form, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="./templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="download_file.html", context={}
    )

@app.post("/download-file")
async def download_file(request: Request, name: Annotated[str, Form(...)]):

    with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False) as f:
        f.write(name.encode('utf-8')) 
        f.seek(0)
        return FileResponse(f.name)



if __name__ == "__main__":
    uvicorn.run(app, port=7777)