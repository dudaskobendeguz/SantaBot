from flask import Flask, request, render_template, url_for

import data_manager

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/profiles')
def profiles():
    profiles_list = data_manager.get_profiles()
    return render_template('profiles.html', profiles=profiles_list)


if __name__ == '__main__':
    app.run(
        debug=True
    )