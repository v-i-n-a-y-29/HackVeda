from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pydantic import BaseModel

# ML logic imports
from predict import predict_chlorophyll
from sst_predict import forecast_sst_from_csv

# -----------------------------
# App Initialization
# -----------------------------
app = FastAPI(title="Ocean Intelligence ML API")

# Allow frontend access (React/Vite)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Input Models
# -----------------------------
class ChlorophyllInput(BaseModel):
    depth: float
    salinity: float
    ph: float

# -----------------------------
# Routes
# -----------------------------

# 1️⃣ Chlorophyll Prediction – Single Input
@app.post("/predict")
def predict_single(data: ChlorophyllInput):
    prediction = predict_chlorophyll(
        data.depth,
        data.salinity,
        data.ph
    )
    return {
        "predicted_chlorophyll": prediction
    }


# 2️⃣ Chlorophyll Prediction – CSV Upload
@app.post("/predict/csv")
async def predict_chlorophyll_csv(file: UploadFile = File(...)):
    """
    CSV must contain columns:
    depth, salinity, ph
    Optional: chlorophyll (for comparison)
    """
    df = pd.read_csv(file.file)
    df.columns = df.columns.str.lower().str.strip()

    required_cols = {"depth", "salinity", "ph"}
    if not required_cols.issubset(df.columns):
        return {
            "error": f"CSV must contain columns: {required_cols}. Found: {list(df.columns)}"
        }

    predictions = [
        predict_chlorophyll(row["depth"], row["salinity"], row["ph"])
        for _, row in df.iterrows()
    ]

    response = {
        "depth": df["depth"].tolist(),
        "salinity": df["salinity"].tolist(),
        "ph": df["ph"].tolist(),
        "predicted_chlorophyll": predictions
    }

    # Optional: compare with actual chlorophyll if provided
    if "chlorophyll" in df.columns:
        response["actual_chlorophyll"] = df["chlorophyll"].tolist()

    return response


# 3️⃣ SST Forecasting – CSV Upload (OPTION 2 ✅)
@app.post("/predict/sst/csv")
async def predict_sst_csv(file: UploadFile = File(...)):
    """
    SST CSV must contain columns:
    date,value

    Example:
    date,value
    1991-07-01,3.52
    1991-08-01,3.18
    """
    df = pd.read_csv(file.file)
    df.columns = df.columns.str.lower().str.strip()

    required_cols = {"date", "value"}
    if not required_cols.issubset(df.columns):
        return {
            "error": f"SST CSV must contain columns: {required_cols}. Found: {list(df.columns)}"
        }

    result = forecast_sst_from_csv(df)
    return result


# 4️⃣ Helper Endpoint (for frontend clarity)
@app.get("/predict/sst")
def sst_info():
    return {
        "message": "Upload SST CSV to /predict/sst/csv with columns: date,value"
    }


# 5️⃣ Overfishing Monitor - GET (Mock Data)
@app.get("/overfishing_monitor")
def get_overfishing_data():
    """
    Returns sample overfishing monitoring data for testing.
    In production, use POST endpoint with CSV upload.
    """
    # Load sample CSV data
    try:
        import os
        csv_path = os.path.join(os.path.dirname(__file__), 'sample_overfishing.csv')
        print(f"Loading CSV from: {csv_path}")
        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.lower().str.strip()

        dates = df["date"].tolist()
        stock_volumes = df["stock_volume"].tolist()
        catch_volumes = df["catch_volume"].tolist()
        print(f"✅ CSV loaded successfully: {len(dates)} records")
    except Exception as e:
        print(f"❌ CSV load error: {e}, using fallback data")
        # Fallback to hardcoded data
        dates = [
            '2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06',
            '2023-07', '2023-08', '2023-09', '2023-10', '2023-11', '2023-12',
            '2024-01', '2024-02', '2024-03', '2024-04', '2024-05', '2024-06',
            '2024-07', '2024-08', '2024-09', '2024-10', '2024-11', '2024-12'
        ]
        stock_volumes = [20946, 20972, 20974, 21032, 21313, 21177, 21295, 21184, 21187, 21346, 21402, 21344, 21323, 21441, 21418, 21489, 21544, 21529, 21793, 21907, 21754, 21823, 21807, 21942]
        catch_volumes = [3832, 3244, 2333, 5740, 5596, 6351, 6374, 4471, 5377, 6168, 5777, 3190, 4053, 2698, 6228, 4754, 3139, 5045, 4873, 3759, 2669, 5113, 4449, 5583]

    # Calculate overfishing threshold (20% of stock)
    thresholds = [stock * 0.2 for stock in stock_volumes]

    # Determine overfishing periods (catch > 20% of stock)
    overfishing_indices = [
        i for i, (catch, threshold) in enumerate(zip(catch_volumes, thresholds))
        if catch > threshold
    ]

    # Create shapes for overfishing alerts
    shapes = []
    for i in overfishing_indices:
        if i < len(dates):
            shapes.append({
                "type": "rect",
                "xref": "x",
                "yref": "paper",
                "x0": dates[i],
                "y0": 0,
                "x1": dates[i],
                "y1": 1,
                "fillcolor": "rgba(255, 107, 107, 0.2)",
                "opacity": 0.3,
                "line": {"width": 0}
            })

    return {
        "data": [
            {
                "x": dates,
                "y": stock_volumes,
                "type": "scatter",
                "mode": "lines",
                "name": "Stock Volume",
                "line": {"color": "#2ECC71", "width": 3}
            },
            {
                "x": dates,
                "y": catch_volumes,
                "type": "scatter",
                "mode": "lines",
                "name": "Catch Volume",
                "line": {"color": "#FF6B6B", "width": 3}
            },
            {
                "x": dates,
                "y": thresholds,
                "type": "scatter",
                "mode": "lines",
                "name": "Overfishing Threshold (20%)",
                "line": {"color": "#F1C40F", "width": 2, "dash": "dash"}
            }
        ],
        "layout": {
            "title": {"text": "Overfishing Monitoring - Stock vs Catch Analysis", "font": {"color": "white", "size": 18}},
            "xaxis": {
                "title": "Date",
                "color": "white",
                "gridcolor": "rgba(255,255,255,0.15)",
                "tickangle": -45
            },
            "yaxis": {
                "title": "Volume",
                "color": "white",
                "gridcolor": "rgba(255,255,255,0.15)"
            },
            "plot_bgcolor": "rgba(0,0,0,0)",
            "paper_bgcolor": "rgba(0,0,0,0)",
            "font": {"color": "white"},
            "legend": {"bgcolor": "rgba(255,255,255,0.1)", "bordercolor": "rgba(255,255,255,0.2)"},
            "shapes": shapes
        }
    }


# 6️⃣ Overfishing Monitor - CSV Upload
@app.post("/overfishing_monitor")
async def analyze_overfishing_csv(file: UploadFile = File(...)):
    """
    Analyze overfishing from CSV data.
    CSV must contain columns: Date, Stock_Volume, Catch_Volume
    """
    df = pd.read_csv(file.file)
    df.columns = df.columns.str.lower().str.strip()

    required_cols = {"date", "stock_volume", "catch_volume"}
    if not required_cols.issubset(df.columns):
        return {
            "error": f"CSV must contain columns: {required_cols}. Found: {list(df.columns)}"
        }

    # Extract data
    dates = df["date"].tolist()
    stock_volumes = df["stock_volume"].tolist()
    catch_volumes = df["catch_volume"].tolist()

    # Calculate overfishing threshold (20% of stock)
    thresholds = [stock * 0.2 for stock in stock_volumes]

    # Determine overfishing periods (catch > 20% of stock)
    overfishing_indices = [
        i for i, (catch, threshold) in enumerate(zip(catch_volumes, thresholds))
        if catch > threshold
    ]

    # Create shapes for overfishing alerts
    shapes = []
    for i in overfishing_indices:
        if i < len(dates):  # Safety check
            shapes.append({
                "type": "rect",
                "xref": "x",
                "yref": "paper",
                "x0": dates[i],
                "y0": 0,
                "x1": dates[i],
                "y1": 1,
                "fillcolor": "rgba(255, 107, 107, 0.2)",
                "opacity": 0.3,
                "line": {"width": 0}
            })

    return {
        "data": [
            {
                "x": dates,
                "y": stock_volumes,
                "type": "scatter",
                "mode": "lines",
                "name": "Stock Volume",
                "line": {"color": "#2ECC71", "width": 3}
            },
            {
                "x": dates,
                "y": catch_volumes,
                "type": "scatter",
                "mode": "lines",
                "name": "Catch Volume",
                "line": {"color": "#FF6B6B", "width": 3}
            },
            {
                "x": dates,
                "y": thresholds,
                "type": "scatter",
                "mode": "lines",
                "name": "Overfishing Threshold (20%)",
                "line": {"color": "#F1C40F", "width": 2, "dash": "dash"}
            }
        ],
        "layout": {
            "title": {"text": "Overfishing Monitoring - Stock vs Catch Analysis", "font": {"color": "white", "size": 18}},
            "xaxis": {
                "title": "Date",
                "color": "white",
                "gridcolor": "rgba(255,255,255,0.15)",
                "tickangle": -45
            },
            "yaxis": {
                "title": "Volume",
                "color": "white",
                "gridcolor": "rgba(255,255,255,0.15)"
            },
            "plot_bgcolor": "rgba(0,0,0,0)",
            "paper_bgcolor": "rgba(0,0,0,0)",
            "font": {"color": "white"},
            "legend": {"bgcolor": "rgba(255,255,255,0.1)", "bordercolor": "rgba(255,255,255,0.2)"},
            "shapes": shapes
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)