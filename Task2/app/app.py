from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re
import numpy as np
from spell_stream import ar_spelling_checker
app = FastAPI()

class InputText(BaseModel):
    text: str

class OutputResult(BaseModel):
    output: str

@app.post("/spelling_checker", response_model=OutputResult)
async def spelling_checker(input_text: InputText):
    text = input_text.text
    output = ar_spelling_checker(text)
    return {"output": output}


