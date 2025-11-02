import os
from flask import Flask, render_template, request

app = Flask(__name__)

# nossos personagens
PERSONAGENS = [
    {"id":"carol", "nome":"Carol", "desc":"Criança Gigante e Forte"},
    {"id":"yasmin", "nome":"Yasmin", "desc":"Anã Assassina"},
    {"id":"vitoria","nome":"Vitória","desc":"A Sedutora Armadilhada"},
    {"id":"daniel","nome":"Daniel","desc":"Portador do Fogo"},
    {"id":"geovanna","nome":"Geovanna","desc":"Senhora Fofoqueira"},
]

@app.route("/")
def index():
    rota = request.args.get("rota")
    msg = None
    if rota == "carol":
        msg = "Vocês foram para a casa da Carol. A porta está emperrada…"
    elif rota == "vitoria":
        msg = "Vocês foram para a casa da Vitória. Há trancas e esconderijos…"
    return render_template("index.html", personagens=PERSONAGENS, msg=msg)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=False)
