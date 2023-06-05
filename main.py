from fastapi import FastAPI


app = FastAPI()

@app.get('/{user}')
def index(user : int):
    return {"data" : {"name" : user}}