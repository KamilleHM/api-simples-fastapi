from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/sum")
def sum_numbers(a: float, b: float):
	result = a + b
	return {"result": result}

# To run: uvicorn main:app --reload

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)