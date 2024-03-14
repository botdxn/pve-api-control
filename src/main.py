# main.py
from fastapi import FastAPI, HTTPException
from starlette.background import BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pveApi import PVEApi

app = FastAPI()

# Template dir
templates = Jinja2Templates(directory="templates")

# PVE API Creds
PROXMOX_HOST = "https://pve-url:8006/api2/json"
TOKEN_ID = "user@pve!tokenname"
TOKEN_SECRET = "secret"
NODE = "node"
VM_ID = "100"

pve_api = PVEApi(PROXMOX_HOST, TOKEN_ID, TOKEN_SECRET)

@app.get("/")
async def read_root(request):
    """Serve HTML"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/start-vm")
async def api_start_vm(background_tasks: BackgroundTasks):
    """Endpoint for VM Start"""
    try:
        result = pve_api.start_vm(NODE, VM_ID)
        if result:
            return {"detail": "VM start initiated."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
