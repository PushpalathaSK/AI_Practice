from fastapi import FastAPI

api=FastAPI()

@api.get("/")
def read_root():
    return {"message" : "This is my first API"}


@api.get("/name")
def read_root():
    return {"name" : "I am Pushpalatha"}
