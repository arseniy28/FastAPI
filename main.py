from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import Optional
import pytesseract
from PIL import Image
import io

app = FastAPI()

# Модель для запроса перевода текста
class TranslationRequest(BaseModel):
    text: str
    target_language: str

@app.post("/translate")
async def translate(request: TranslationRequest):
    
    translated_text = f"Translated '{request.text}' to {request.target_language}"
    return {"translated_text": translated_text}

@app.post("/translate/image")
async def translate_image(file: UploadFile = File(...), target_language: str = "en"):
    image = Image.open(io.BytesIO(await file.read()))
    extracted_text = pytesseract.image_to_string(image)

    # Здесь должен быть код для выполнения перевода
    translated_text = f"Translated '{extracted_text}' to {target_language}"
    return {"translated_text": translated_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
