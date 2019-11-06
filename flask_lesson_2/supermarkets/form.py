from wtforms import Form, StringField, FileField, validators

class Add_supermarket(Form):
    name = StringField('name', [validators.DataRequired()],render_kw={
        "class": "form-control",
    })
    location = StringField('location', [validators.DataRequired()],render_kw={
        "class": "form-control",
    })
    image = FileField('image', render_kw={
        "class": "form-control",
        "accept": "image/jpeg,image/png"
    })
