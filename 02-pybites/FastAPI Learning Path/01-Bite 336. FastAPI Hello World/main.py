import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def root():
    msg = "Welcome to FastAPI Learning Path 🐍 🎉"
    return {"message": msg}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
