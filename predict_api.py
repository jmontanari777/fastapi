from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from PIL import Image
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert('RGB')

    # Aquí iría la inferencia con tu modelo
    # Por ahora, retornamos un mock
    return {
        "prediction": "Moderate Diabetic Retinopathy",
        "confidence": 87.5
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
