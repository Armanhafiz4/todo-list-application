from flask_wtf import Flaskform
from wtforms import Stringfield, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    description = StringField('Description of the Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')