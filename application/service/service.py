from flask import redirect, url_for, render_template, request

class IndexPage():
    def Index():
        return render_template('index.html')