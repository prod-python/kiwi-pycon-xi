from flask import Flask


app = Flask(__name__)


@app.route("/polls/v2/")
def new_polls_api():
    return "New Polls API", 200


if __name__ == '__main__':
    app.run(port=8000)
