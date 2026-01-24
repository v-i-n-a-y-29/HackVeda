from fastapi import FastAPI, UploadFile, File
import pandas as pd
from pydantic import BaseModel
from backend.predict import predict_chlorophyll

app = FastAPI(title="Ocean Intelligence ML API")

class ChlorophyllInput(BaseModel):
    depth: float
    salinity: float
    ph: float

@app.post("/predict")
def predict(data: ChlorophyllInput):
    result = predict_chlorophyll(
        data.depth,
        data.salinity,
        data.ph
    )
    return {
        "predicted_chlorophyll": result
    }

#NEW endpoint to handle batch predictions via file upload
@app.post("/predict/csv")
async def predict_from_csv(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    required_cols = {"depth", "salinity", "ph"}
    if not required_cols.issubset(df.columns):
        return {"error": "CSV must contain depth, salinity, and ph columns"}

    predictions = []

    for _, row in df.iterrows():
        pred = predict_chlorophyll(
            row["depth"],
            row["salinity"],
            row["ph"]
        )
        predictions.append(pred)

    response = {
        "depth": df["depth"].tolist(),
        "salinity": df["salinity"].tolist(),
        "ph": df["ph"].tolist(),
        "predicted_chlorophyll": predictions
    }

    # Optional: include actual chlorophyll if present
    if "chlorophyll" in df.columns:
        response["actual_chlorophyll"] = df["chlorophyll"].tolist()

    return response