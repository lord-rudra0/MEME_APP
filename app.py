from flask import Flask, render_template, request, redirect, url_for
import os
import json
import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)

def meme():
    url = os.getenv("meme_url")
    response = requests.get(url)
    data = response.json()
    return data['url']



@app.route('/')
def index():
    return render_template('index.html')



