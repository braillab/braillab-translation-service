from pydantic import BaseModel
    
class TranslateRequest(BaseModel):
    text: str

class InitLangRequest(BaseModel):
    language_id: str

class LanguageInfo(BaseModel):
  code: str
  name: str
  native_name: str
  grade_supported: int

class Indicators(BaseModel):
  number: List[str]
  mayus: List[str]

class LanguageSchema(BaseModel):
  language: LanguageInfo
  indicators: Indicators
  letters: Dict[str, str]
  numbers: Dict[str, str]
  punctuation: Dict[str, str]
  contractions: Dict[str, str]