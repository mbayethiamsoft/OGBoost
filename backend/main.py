from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from graph import graph

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en dev OK
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate(data: dict):
    print("DATA REÇUE:", data)  # 👈 debug

    result = graph.invoke({
        "input": data.get("text", "")
    })

    return result