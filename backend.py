from fastapi import FastAPI
from ollama_connect import Gen_Rev
from pydantic import BaseModel



app = FastAPI()


object = Gen_Rev()

@app.get('/getting_plaintext')
def get_plain_message():


    plaintext = object.generate_plaintext()

    return {'plaintext' : plaintext}

@app.get('/getting_ciphertext')
def get_cipher_message():


    ciphertext = object.get_ciphertext()

    return {'ciphertext' : ciphertext}

class PlayerAnswer(BaseModel):
    message: str


@app.post("/evaluating_message")
def eval_message(request: PlayerAnswer):
    player_message = request.message


    sim_score = object.evaluate_analysist(player_message)

    return {'similarity_score' : sim_score}