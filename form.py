import dbConnector
from custom_validators import height_validator,weight_validator

from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, validators, SubmitField, SelectField

db = dbConnector.dbConnector()
db.build_table()

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SeCrEt'

class Questionnaire(Form):

    name = TextField('Name:',[validators.InputRequired()])
    surname = TextField('Surname:',[validators.InputRequired()])
    email = TextField('Email:',[validators.InputRequired(),validators.Email()])
    weight = TextField('Weight (kg):',[validators.InputRequired(),weight_validator])
    height = TextField('Height (kg):',[validators.InputRequired(),height_validator])

    feelings_options = [(1,'Bad'),(2,'OK'),(3,'Good')]

    feelings = SelectField('Feelings about yourself:',coerce=int, \
        choices=feelings_options,validators=[validators.InputRequired()])
 
@app.route("/", methods=['GET', 'POST'])
def form_handling():

    form = Questionnaire(request.form)

    values = (form.name.data,form.surname.data,form.email.data, \
        form.weight.data,form.height.data,form.feelings.data)

    if request.method == 'POST':
        if form.validate():
            db.add_values(values)
            flash('Success!','success')

        else:
            flash('Error:'+str(form.errors),'danger')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()
