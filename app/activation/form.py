#coding=utf-8
from flask_wtf import FlaskForm
from ..leotool.leoform.formcore import StringField,HiddenField,SubmitField,TextAreaField,StringField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
photos = UploadSet('photos', IMAGES)

class details_qupu(FlaskForm):
    id = StringField('曲谱id', validators=[DataRequired(), Length(1, 36)])
    oldurl = StringField('原网址', validators=[DataRequired(), Length(1, 255)])
    title = TextAreaField('曲名',validators=[DataRequired(), Length(1, 255)])
    jianpu = TextAreaField('简谱',validators=[DataRequired(), Length(1, 1028)])
    # hidden_pic_url = HiddenField("pic_url",default="")
    submit = SubmitField('返回')


class select_list(FlaskForm):
    user_ip = StringField('IP查询',validators=[DataRequired(), Length(1, 255)],render_kw={"id":"user_ip"})
    # user_num = StringField('业务号码',validators=[DataRequired(), Length(1, 255)],render_kw={"id":"user_num"})
    submit = SubmitField('搜索')



