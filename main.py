from typing import Annotated

from fastapi import FastAPI, Depends

from studentsAction.Student import StudentAdd

app = FastAPI()

sts = []
@app.post("/student")
async def student(student: Annotated[StudentAdd, Depends()]):
    sts.append(student)
    return {"ok": True}

@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
