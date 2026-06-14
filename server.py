from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    import os
    # Берем порт, который выдает хостинг, или ставим 3000 локально
    port = int(os.environ.get("PORT", 5000))
    # Запуск на хосте 0.0.0.0 обязателен, чтобы сервер слушал внешнюю сеть
    app.run(host='0.0.0.0', port=port)
