# pveApi.py
import requests


""" 
## ENV VARIABLES ##
ENV_NODE = "node-name"
ENV_HOST = "https://proxmox-url:8006"
ENV_AUTH_URL = ENV_HOST + "/api2/json"

ENV_TOKEN_ID = "user@pve!tokenname"
ENV_TOKEN_SECRET = "value"

ENV_HEADER = f"PVEAPIToken={ENV_TOKEN_ID}={ENV_TOKEN_SECRET}"
"""

class PVEApi:
    """Class to handle API stuff"""
    def __init__(self, host, node, auth_url, token_id, token_secret):
        self.host = host
        self.token_id = token_id
        self.token_secret = token_secret
        self.header = {'Authorization': f'PVEAPIToken={self.token_id}={self.token_secret}'}

    def start_vm(self, node, vmid):
        """Start a VM given its node and VMID."""
        vm_start_url = f"{self.host}/nodes/{node}/qemu/{vmid}/status/start"
        try:
            response = requests.post(vm_start_url, headers=self.headers)
            response.status_code == 200
        except:
            response.raise_for_status()