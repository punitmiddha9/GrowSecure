"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template, request, send_file
from Components import app
from Components.functions import encryption, decryption

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Decrypt',
        year=datetime.now().year,
        message='Upload your encrypted image along with the key'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='Encrypt',
        year=datetime.now().year,
        message='Upload the image here'
    )

@app.route('/contact1', methods = ['POST'])  
def contact1():  
    if request.method == 'POST':  
        global f
        f = request.files['file']  
        f.save(f.filename)  
        #key = request.form['key']
        image=decryption.decrypt("secret",f.filename)
        return render_template('contact1.html',
        title='Decrypted',
        year=datetime.now().year,
        message='This is your Decrypted image', name = f.filename) 

@app.route('/about1', methods = ['POST'])  
def about1():  
    if request.method == 'POST':  
        global f
        f = request.files['file']  
        f.save(f.filename) 
        key = request.form['key'] 
        image=encryption.encrypt(key,f.filename)
        return render_template('about1.html',
        title='Encrypted',
        year=datetime.now().year,
        message='This is your encrypted image', name = f.filename,keys="secret",images=image)

@app.route('/return-file')
def return_file():
    return send_file("../enc.jpg",attachment_filename="enc.jpg")

@app.route('/return-file1')
def return_file1():
    return send_file("../dec.jpg",attachment_filename="dec.jpg")

app.run(debug = True)