from fastapi import FastAPI, Request


app = FastAPI()


@app.get("/{name}")
def hello(request: Request, name: str) -> dict[str, str]:
    return {"Hello": f"How are you, {name}?"}
