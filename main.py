import uvicorn
from fastapi import FastAPI
from scraper import get_price

app = FastAPI()


@app.get("/price")
def search_price():
    return get_price()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)