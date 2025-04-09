from flask import Flask,  render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello Flask!"


@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"
    
    


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        address = request.form['address']
        return render_template('result.html', first_name=first_name, last_name=last_name, email=email, address=address)
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)