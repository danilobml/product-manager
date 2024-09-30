from fastapi import FastAPI

app = FastAPI()


@app.get('/hello')
def hello():
    return {
        'status_code': 200,
        'message': 'Hello, malaco!'
    }
