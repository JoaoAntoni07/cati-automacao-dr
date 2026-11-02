from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
import uvicorn
import uuid

app = FastAPI(title="Gerador DRS - CATI Jr.")

@app.post("/jobs")
async def receber_trabalho(request: Request):
    # Recebe o JSON enviado pelo Apps Script
    payload = await request.json()
    
    projeto_id = payload.get("projeto_id")
    fontes = payload.get("fontes", [])
    
    print(f"\n[+] Novo trabalho recebido!")
    print(f"Projeto ID: {projeto_id}")
    print(f"Arquivos recebidos: {len(fontes)}")
    
    # Gera um ID único para este trabalho
    job_id = str(uuid.uuid4())
    
    # Devolve o HTTP 202 (Aceito) com o job_id, conforme a especificação da CATI Jr.
    return JSONResponse(
        status_code=status.HTTP_202_ACCEPTED,
        content={"job_id": job_id, "status": "na fila"}
    )

if __name__ == "__main__":
    # Roda o servidor localmente na porta 8000
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)