import helperfunctions as hf
import pyttsx3 as pyt

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def main():
    engine = pyt.init()
    tossups = hf.getQuestionFromAL("India")
    hf.speakQuestion(engine, tossups[0])


if __name__ == "__main__":
    app.run(debug=True)
