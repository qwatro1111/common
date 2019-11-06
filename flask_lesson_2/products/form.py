from wtforms import Form, StringField, TextAreaField, FileField, FloatField, validators

class Add_product(Form):
    name = StringField('name', [validators.DataRequired()],render_kw={
        "class": "form-control",
    })
    description = TextAreaField('description', [validators.DataRequired()], render_kw={
        "class": "form-control",
    })
    image = FileField('image', render_kw={
        "class": "form-control",
        "accept": "image/jpeg,image/png"
    })
    price = FloatField('price', [validators.DataRequired()], render_kw={
        "class": "form-control",
        "type": "number",
        "step": "0.1",
        "min": "0",
        "value": 0
    })
