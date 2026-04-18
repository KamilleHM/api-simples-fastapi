from fastapi import FastAPI
from typing import Optional
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/sum")
def sum_numbers(a: float, b: float):
	try:
		a = float(a)
		b = float(b)  
	except Exception as e:
		return JSONResponse(content={"error": "Invalid input. Please provide numeric values for a and b."}, status_code=400)
	
	result = a + b
	return {"result": result}


@app.get("/subtract")
def subtract_numbers(a: float, b: float):
	try:
		a = float(a)
		b = float(b)
	except Exception as e:
		return JSONResponse(content={"error": "Invalid input. Please provide numeric values for a and b."}, status_code=422)

	result = a - b
	return {"result": result}

# To run: uvicorn main:app --reload

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)