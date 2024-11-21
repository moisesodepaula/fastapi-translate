from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from deep_translator import GoogleTranslator

app = FastAPI()

# Definição do modelo de entrada
class TranslationRequest(BaseModel):
    source_language: str
    target_language: str
    text: str

@app.post("/translate")
async def translate_text(request: TranslationRequest):
    """
    Endpoint para traduzir texto usando o deep-translator.
    """
    try:
        # Cria uma instância do GoogleTranslator com os idiomas definidos
        translator = GoogleTranslator(
            source=request.source_language,
            target=request.target_language
        )
        
        # Realiza a tradução
        translated_text = translator.translate(request.text)
        
        # Retorna o texto traduzido
        return {"translatedText": translated_text}

    except Exception as e:
        # Captura erros e retorna uma mensagem de falha
        raise HTTPException(status_code=500, detail=f"Erro ao traduzir: {str(e)}")
