from flask import Flask, render_template

app = Flask(__name__)


@app.route('https://gasoline-alt.github.io/Gasosite/')
def index():
	return render_template("index.html")


@app.route('https://gasoline-alt.github.io/Gasosite/schedule')
def about():
	return render_template("schedule.html")


if __name__ == "__main__":
	app.run(debug=True)
