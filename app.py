# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista per memorizzare i nomi
nomi = []

@app.route('/', methods=['GET', 'POST'])
def index():
    global nomi
    if request.method == 'POST':
        if 'reset' in request.form:
            nomi = []
        elif 'ordina' in request.form:
            nomi = sorted(nomi)
        else:
            nome = request.form.get('nome')
            if nome:
                nomi.append(nome)
        return redirect(url_for('index'))
    return render_template('index.html', nomi=nomi, nomi_ordinati=sorted(nomi))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5005)
