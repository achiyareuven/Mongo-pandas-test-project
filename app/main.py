from fastapi import FastAPI
from app.manager import Manager
import uvicorn
app=FastAPI()
manager =Manager(r"C:\Users\achiy\PycharmProjects\Mongo-pandas-test-project\data\weapon_list.txt")

@app.get("/")
def home():
    return {"message": "hello"}


@app.get("/get_json_result")
def get_data():
    a =manager.run()
    return a


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8003)
