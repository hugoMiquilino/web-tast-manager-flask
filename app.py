from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = []


@app.route("/")
def home():
    return render_template("index.html", tarefas=tarefas)


@app.route("/add", methods=["POST"])
def add():
    try:
        texto = request.form.get("tarefa", "").strip()

        if texto:
            tarefas.append({"texto": texto, "feito": False})

    except Exception:
        pass

    return redirect("/")


@app.route("/done/<int:id>")
def done(id):
    try:
        tarefas[id]["feito"] = True

    except IndexError:
        pass

    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):
    try:
        tarefas.pop(id)
    except IndexError:
        pass

    return redirect("/")


app.run(debug=True)
