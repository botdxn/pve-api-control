FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn jinja2 requests

EXPOSE 8000

ENV PROXMOX_HOST=https://your-proxmox-ve-host:8006/api2/json
ENV TOKEN_ID=user@pve!tokenname
ENV TOKEN_SECRET=secret-generated-by-proxmox
ENV NODE=your-node-name
ENV VM_ID=100

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
