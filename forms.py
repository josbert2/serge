from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField



class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")



class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")



class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")



class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])

from flask_wtf.file import FileField, FileAllowed


# Menu Forms
class MenuForm(FlaskForm):
    title = StringField("Menu Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle (Optional)")
    img_file = FileField("Menu Image", validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    is_active = BooleanField("Active / Visible")
    submit = SubmitField("Save Menu")

class MenuSectionForm(FlaskForm):
    title = StringField("Category Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle (Optional)")
    order = StringField("Order (numeric)", validators=[DataRequired()])
    submit = SubmitField("Save Category")

class MenuItemForm(FlaskForm):
    name = StringField("Item Name", validators=[DataRequired()])
    description = CKEditorField("Description")
    price = StringField("Price (Optional)")
    img_file = FileField("Item Image", validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    order = StringField("Order (numeric)", validators=[DataRequired()])
    submit = SubmitField("Save Item")



