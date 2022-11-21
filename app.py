contact={    }
from flask import Flask, flash, redirect,render_template, url_for, request
from forms import Addform
app = Flask(__name__)

app.config['SECRET_KEY']='d11846b07a6dce4b09b4799230945911'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/add", methods=['GET','POST'])
def add():
    global contact
    form= Addform()
    if form.validate_on_submit():
        flash(f'Entry created for {form.name.data} !', 'success')
        contact[form.name.data]=[form.email.data,form.number.data]
        print(contact)
        return redirect(url_for('home'))
    return render_template('add.html',title='Add',form=form,contact=contact)

@app.route("/display",methods=['GET'])
def display():
    return render_template('display.html',title='Display',contact=contact)

@app.route("/search",methods=["GET",'POST'])
def search():
    global contact
    a = request.form.get('search')
    return render_template("search.html",contact=contact,a=a)

if __name__ == '__main__':
    app.run(debug=True)
