from application import app
from application.service.pages import IndexPage, DownloadPage


@app.route('/')
@app.route('/index')
def  index():
    return IndexPage.Index()

@app.route('/download', methods=['GET', 'POST'])
def download():
    return DownloadPage.Download()
