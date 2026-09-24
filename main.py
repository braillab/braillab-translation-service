import json
from fastapi import FastAPI, Response
from schemas import InitLangRequest, TranslateRequest
from utils import load_json_map

app = FastAPI(title="Braillab Translation Service")
app.state.current_language = None
app.state.current_braille_map = None

@app.post("/init_lang")
def init_language(request: InitLangRequest):
    language_id = request.language_id.lower()

    app.state.current_language = language_id

    app.state.current_braille_map = load_json_map(language_id)

    print(app.state.current_language)
    print(app.state.current_braille_map)

    return {"status_code": 200, "current_language": app.state.current_language, "current_mapping": app.state.current_braille_map}

@app.post("/translate")
def translate(request: TranslateRequest):
    # you can turn that into character if activated, where the mapping is done into dot positions > characters
    print(f"current language es {app.state.current_language}")
    print(f"current text es {request.text}")

@app.post("/create_lang")
def create_language():
    

@app.get("/health")
def health():
    return {"status": "ok", "current language": app.state.current_language}