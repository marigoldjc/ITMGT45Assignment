from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page. Place Home Page contents here.'

@app.route('/products')
def products():
    return 'Products Page. Place Products Page contents here.'

@app.route('/branches')
def branches():
    return 'Branches Page. Place Branch Page contents here.'

@app.route('/aboutus')
def aboutus():
    return 'About Us Page. Place About Us Page contents here.'

if __name__ == '__main__':
    app.run(debug=True)