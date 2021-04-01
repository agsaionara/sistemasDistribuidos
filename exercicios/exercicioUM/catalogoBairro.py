#back-end Catalogo de Pequenos empreendedore do Bairro

import json
import time

from flask import Flask, escape , request , render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')
    #return f'<h1>Catologo de Empresas do Bairro<h1>'

@app.route('/empresas')
def empresas():
    time.sleep(2)

    return f"<p>Seu Zé Mecanico <br> Rua: Pedras Azuis, 110 <br>Entre em contato: (77) 998730092<p><a href='#'>Whatapp</a>"

@app.route('/empresas/<id>')
def empresas_com_id(id):
    return f"<p>Bella e Delicada <br> Rua: Pedras Amarela, 110 <br>Ligue: (77) 9988989<p>"

@app.route('/empresas/<categoria>/listartodos')
def empresas_categoria(categoria):
    return f"{categoria}<p>Bella e Delicada <a href='/empresas/<id>'>Ver mais</a><p>Fina Flor <a href='#'>Ver mais</a>"

@app.route('/empresas/<id>/avaliacoes')
def empresas_avaliacoes(id):
    return f'<p>Empresa {id} :<br>  10 - Gostam | 5 - Não gostam</p>'


if __name__ == '__main__':
    app.run(debug = True)