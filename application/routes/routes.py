from application import app
from application.service.service import IndexPage


@app.route('/')
@app.route('/index')
def  index():
    return IndexPage.Index
