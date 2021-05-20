from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from flask_pymongo import PyMongo
# creating an instance of the flask class
app = Flask(__name__)
app.config['MONGO_URI']='mongodb+srv://santanu:vjtivjti@cluster0.bwcp2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
mongodb_client = PyMongo(app)
db = mongodb_client.db
# HOME
@app.route('/data')
def index():
    return'''
        <form method="POST" action="/create" enctype="multipart/form-data">
            <h1> Enter username</h1>
            <input type="text" name="username">
            <h1>Enter the 1 url</h1>
            <input type="url" name="stock_info1">
            <h1>Enter the Name of the 1 Company</h1>
            <input type="text" name="Company1">
            <h1>Enter the 1 Sector</h1>
            <input type="text" name="sector1">
            <h1>Enter the 2 url</h1>
            <input type="url" name="stock_info2">
            <h1>Enter the Name of the 2 Company</h1>
            <input type="text" name="Company2">
            <h1>Enter the 2 Sector</h1>
            <input type="text" name="sector2">
            <input type="submit">
        </form>
    '''
@app.route('/create',methods=['POST'])
def create():
    db.stock_data_url.insert_one({'name': request.form.get('username'),'url1': request.form.get('stock_info1'),'company1' : request.form.get('Company1'),'sector1' : request.form.get('sector1'),'url2': request.form.get('stock_info2'),'company2' : request.form.get('Company2'),'sector2' : request.form.get('sector2')})
    return jsonify(message="success")

@app.route('/home')
def home():
    return render_template('home.html')

# ABOUTUS
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

# PREDICT
@app.route('/predict')
def predict():
    return render_template('predict.html')

# COMPARE
@app.route('/compare')
def compare():
    return render_template('compare.html')

# PASTPERFORMANCE
@app.route('/pastperformance')
def pastPerformance():
    return render_template('pastPerformance.html')


if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
