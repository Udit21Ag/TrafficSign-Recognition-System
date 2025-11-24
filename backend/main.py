from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from PIL import Image
import tensorflow as tf
from classes import class_names

app = FastAPI()

# Allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = tf.keras.models.load_model("../best_cnn_model.keras")

def preprocess(image: Image.Image):
    image = image.resize((48, 48))
    img_array = np.array(image)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    img = preprocess(image)

    predictions = model.predict(img)
    class_id = np.argmax(predictions[0])
    class_name = class_names[class_id]

    return {"class_id": int(class_id), "class_name": class_name}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)