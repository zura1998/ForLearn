from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, PasswordField, SubmitField, RadioField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email
from flask_wtf.file import FileField, FileAllowed


class LoginForm(FlaskForm):
    login = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password")
    # email = EmailField(label="Email", validators=[Email()])
    email = EmailField(label="Email")
    submit = SubmitField(label="Submit")
    confirmpassword = PasswordField(label="Confirm Password", validators=[EqualTo('password', message="password not "
                                                                                                     "match")])
    gender = RadioField(choices=[('firstchoice', 'Male'), ('secondchoice', 'Female')])
    textarea = TextAreaField(label="Write something")
    # fileupload = FileField(label="FileUpload", validators=[FileAllowed(['.pnj', '.jpg'])])
    fileupload = FileField(label="FileUpload")







