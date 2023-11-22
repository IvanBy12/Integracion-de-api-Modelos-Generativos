import os
import openai
from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {
        "service": "Integracion back openia"
        }


@app.post("/chat")
def chat(pregunta: dict):
    
    
    print(pregunta)
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": pregunta["pregunta"]
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return {
        
        response["choices"][0]["message"]["content"]
         
    }
