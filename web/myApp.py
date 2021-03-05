from flask import Flask, render_template, request
from web.forms import InputText, ContactForm
from model.lstm.predict import get_prediction_for_text

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    input_form = InputText()
    input_form.input.data = ""
    output_text = ""
    if request.method == "POST":
        input_text = request.form['input']
        input_form.input.data = input_text
        output_text = get_prediction_for_text(input_text)
        #output_text = "וָאָיְ וָאחִד מֻמְכִּן יִסָאוִיהָא בִּאלְבֵּית"
    return render_template('home.html', form=input_form, output=output_text)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    return render_template('contact.html', form=form)


@app.route("/help", methods=['GET'])
def helpp():
    return render_template('help.html')

@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')

@app.route("/intro", methods=['GET'])
def intro():
    return render_template('intro.html')
