# link da aula onde cria e publica um site
# https://www.youtube.com/watch?v=K2ejI4z8Mbg&t=300s

import qrcode
from flask import Flask, request, render_template
from PIL import Image, ImageDraw, ImageFont


app = Flask(__name__)

@app.route('/')
def index():
    # Exibe a página HTML com o formulário para o usuário inserir o link
    return render_template('index.html')

@app.route('/gerar_qrcode', methods=['POST'])
def gerar_qrcode():
    # Obtém o link inserido pelo usuário
    link = request.form['link']

    # Cria o QR code a partir do link
    img = qrcode.make(link)

    # Salva o QR code em uma imagem
    img.save('static/images/qrcode.png')

    # Exibe a página HTML com o formulário e o QR code gerado
    return render_template('index.html', link=link, img='static/images/qrcode.png')


if __name__ == '__main__':
    app.run(debug=True)