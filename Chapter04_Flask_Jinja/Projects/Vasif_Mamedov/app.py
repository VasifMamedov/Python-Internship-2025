from flask import Flask, render_template
app = Flask(__name__)

products = [
    {"name":"s25", "price":100, "img":"/static/s25.jpg" },
    {"name":"s25", "price":100, "img":"/static/s25.jpg" },
    {"name":"s25", "price":100, "img":"/static/s25.jpg" },
    {"name":"s25", "price":100, "img":"/static/s25.jpg" },
    {"name":"iphone17", "price":200, "img":"/static/iphone17.jpg" },
    {"name":"iphone17", "price":200, "img":"/static/iphone17.jpg" },
    {"name":"iphone17", "price":200, "img":"/static/iphone17.jpg" },
    {"name":"iphone17", "price":200, "img":"/static/iphone17.jpg" },
    {"name":"iphone17", "price":200, "img":"/static/iphone17.jpg" },
    {"name":"iphone17", "price":200, "img":"/static/iphone17.jpg" },
]

@app.route('/')
def index():
    return render_template("index.html", product_list=products)
@app.route('/register')
def register():
    return render_template("register.html")
@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)