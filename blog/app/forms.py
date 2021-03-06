from flask_wtf import Form
from wtforms import TextAreaField, SubmitField
from wtforms.validators import Required

class PostForm(Form):
    body = TextAreaField("What's on your mind?", validators=[Required()])
    submit = SubmitField('Submit')