from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)
app.secret_key = b'857de2a29c8ae59136644e2c5834591965617ced61e9e3a557f45d37467869b9'

# import secrets генерация надёжного секретного ключа
# secrets.token_hex()

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Обработка данных формы
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for('form'))
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False)

