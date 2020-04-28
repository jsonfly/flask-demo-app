from flask import Flask, render_template

app = Flask('codecool_series')


@app.route('/')
@app.route('/<name>')
def index(name=None):
    return render_template('index.html', name=name)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
