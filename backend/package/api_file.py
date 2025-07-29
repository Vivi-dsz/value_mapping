from fastapi import FastAPI
import pickle

from backend.package.dummy import calculate_function

# FastAPI instance
app = FastAPI()

# Root endpoint
@app.get("/")
def root():
    return {'greeting':"hello"}

# Prediction endpoint
@app.get("/calculate")
def predict(bankname):
    # Use the function in our package to run the prediction
    df = calculate_function(bankname)

    # Return figure
    return {'pred': float(df)}
