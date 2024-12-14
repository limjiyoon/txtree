"""Basic FastAPI app."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def test() -> dict:
    """Tmp test endpoint."""
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
