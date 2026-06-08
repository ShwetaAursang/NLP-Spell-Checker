from flask import Flask, render_template, request
from spell_checker import correction

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""

    if request.method == 'POST':
        word = request.form['word']
        result = correction(word)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
