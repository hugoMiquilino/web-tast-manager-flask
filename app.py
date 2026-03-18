from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = []

@app.route("/")
def home():
    return render_template('index.html', tarefas=tarefas)

@app.route("/add", methods=["POST"])
def add():
    texto = request.form.get("tarefa")
    tarefas.append({"texto": texto, "feito": False})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)