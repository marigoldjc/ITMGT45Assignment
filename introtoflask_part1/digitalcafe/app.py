from flask import Flask
app = Flask(__name__)

navbar = """
         <a href='/'>Home</a> | <a href='/products'>Products</a> |

         <a href='/branches'>Branches</a> | <a href='/aboutus'>About Us</a>
         <p/>
         """

@app.route('/')
def index():
    pagecontent = 'Index Page. Place Home Page contents here.'
    return navbar+pagecontent

@app.route('/products')
def products():
    pagecontent = 'Products Page. Place Products Page contents here.'
    return navbar+pagecontent

@app.route('/branches')
def branches():
    pagecontent = 'Branches Page. Place Branches Page contents here.'
    return navbar+pagecontent

@app.route('/aboutus')
def aboutus():
        pagecontent = 'About Us Page. Place About Us Page contents here.'
        return navbar+pagecontent
