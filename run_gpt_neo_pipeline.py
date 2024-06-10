from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

huggingface_token = os.getenv("HUGGINGFACE_TOKEN")

if huggingface_token is None:
    raise ValueError("HUGGINGFACE_TOKEN environment variable not set")

print("Using Hugging Face token:", huggingface_token)

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B", use_auth_token=huggingface_token)
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-2.7B", use_auth_token=huggingface_token)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    max_length = data.get('max_length', 50)
    generated = pipe(prompt, max_length=max_length)
    response_text = generated[0]['generated_text']
    return jsonify({'generated_text': response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)