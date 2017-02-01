from wtforms import Form, StringField, TextAreaField, SelectMultipleField, validators


class ArticleForm(Form):
    title = StringField("Title", [validators.DataRequired("Please enter title")])
    content = TextAreaField("Content", [validators.DataRequired("Please Enter content")])
    tags = SelectMultipleField("Tags", choices=[])


class TagForm(Form):
    name = StringField("Tag name", [validators.DataRequired("Please enter tag's name")])
 
