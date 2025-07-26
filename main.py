from bitcoinprice import run_fetch_job
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is running"}

@app.get("/run")
def run_job():
    try:
        run_fetch_job()
        return {"message": "Bitcoin price fetch job executed successfully."}
    except Exception as e:
        return {"error": str(e)}

