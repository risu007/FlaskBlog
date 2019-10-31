from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms import validators


class PostForm(FlaskForm):
    title= StringField('Title',[validators.DataRequired()])
    content=TextAreaField('content',[validators.DataRequired()])
    submit=SubmitField('Post')
