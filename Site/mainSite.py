from flask import Flask, render_template, request, redirect, g, url_for, session, jsonify


lista = [None, None]
lista2 = [None, None]


app = Flask(__name__)

app.secret_key = 'OBAJC#@($IVÇaeOFQ#!%&QW_JDASBJBCI'

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        session.pop('user', None)

        if request.form['password'] == '123':
          if request.form['username'] == 'adm':
            session['user'] = request.form['username']
            return redirect(url_for('comandvoice'))

    return render_template('login.html')

@app.route("/teste")
def teste():
    return render_template('teste.html')


@app.route("/comandvoice")
def comandvoice():
    if g.user:
        return render_template('comand-voice.html', user=session['user'])
    return redirect(url_for('login'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/r", methods=["GET", "POST"])
def r():
    if len(lista) == 10:
        lista.clear()
        lista.append(None and None)

    req = request.get_json()
    print(req)
    lista.append(req)

    if lista[-2] != None:
        return jsonify(lista[-2])
    else:
        return jsonify('')

@app.route("/garraTeste", methods=["GET", "POST"])
def garraTeste():
    if len(lista) == 10:
        lista2.clear()
        lista2.append(None and None)

    req = request.get_json()
    print(req)
    lista2.append(req)

    if lista2[-2] != None:
        return jsonify(lista2[-2])
    else:
        return jsonify('')

app.run(debug=True, host='0.0.0.0')