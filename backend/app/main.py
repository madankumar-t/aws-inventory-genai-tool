from fastapi import FastAPI
from app.agent.agent import run_agent
app=FastAPI()
@app.get('/')
def h(): return {'status':'ok'}
@app.post('/query')
def q(p:dict): return run_agent(p.get('prompt',''))