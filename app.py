from flask import Flask, render_template, request, redirect, url_for
import os
import json
import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)

def meme():
    url = os.getenv("meme_url")
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit



@app.route('/')
def index():
    meme_pic, subreddit = meme()
    return render_template('index.html', meme_pic=meme_pic, subreddit=subreddit)


if __name__ == '__main__':
    app.run(debug=True)


