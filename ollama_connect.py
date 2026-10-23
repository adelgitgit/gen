import ollama 
from  ceaser_encrypt import caesar_cipher
from  roc_enc_dec import rot13_encrypt
from time import sleep
import numpy as np
from sentence_transformers import SentenceTransformer
from numpy.linalg import norm
from numpy import random
from veg_cipher import veg_encrypt

MODEL = 'qwen2.5:1.5b'
LEADER_SYSTEM = """
You are an army leader in a fictional war simulation.

You issue commands to soldiers and subordinate leaders.

STRICT OUTPUT REQUIREMENTS:
- Every response MUST contain between 50 and 70 words.
- Never produce fewer than 50 words.
- Describe the situation, explain the command, assign responsibilities,
  and state the expected outcome.
- Do not include an introduction or a word count.
- Before responding, verify that your response contains at least 50 words.
"""

ANALYST_SYSTEM = """
    You interpret commands from a fictional military simulation.
    Summarize the command's intent and important details.
    Be concise and do not invent information.
    """


class Gen_Rev:

    def __init__(self):
        self.client = ollama.Client()
        self.sentence_model =SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
        self.current_leader_command = ''

    def generate_plaintext(self):
        response = self.client.generate(MODEL,prompt=f'Issue the next command to your soldiers.',system=LEADER_SYSTEM,stream=False,keep_alive=False,options={'temperature' : 1.0})
        self.current_leader_command = response['response']
        return response['response']


    def get_ciphertext(self):
        cipher = random.choice(["rot", "caesar",'veg'])
        cipher_text = ''

        if cipher == 'rot':
            cipher_text = rot13_encrypt(self.current_leader_command)
        elif cipher == 'caesar':

            random_key = random.choice([_ for _ in range(26)])
            cipher_text = caesar_cipher(self.current_leader_command,random_key)

        elif cipher == 'veg':
            random_key = self.client.generate(MODEL,prompt=f'just produce a random word.',stream=False,keep_alive=False,options={'temperature' : 2.0})
            cipher_text = veg_encrypt(self.current_leader_command,random_key['response'])


        return cipher_text 

    def evaluate_analysist(self,analysis):
         embs = self.sentence_model.encode([self.current_leader_command,analysis])
        
         sim_score = self.sentence_model.similarity(embs[0],embs[1])

         return sim_score.item()




