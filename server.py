from flask import Flask, request, render_template, url_for


app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main_page.htm')


if __name__ == '__main__':
    app.run(
        debug=True
    )