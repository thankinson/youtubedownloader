from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class DownLoadVideo(FlaskForm):
    video_url = StringField('Enter Video Url: ')
    submit = SubmitField('Get Video')

class DownLoadAudio(FlaskForm):
    audio_url = StringField('Enter Audio Url: ')
    submit = SubmitField('Get Audio')
