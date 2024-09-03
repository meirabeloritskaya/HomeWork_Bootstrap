from flask import Flask, Response
import os

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def contacts(path):

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "../templates", "contacts.html")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except Exception as e:
        return str(e), 500

    return Response(content, content_type="text/html")


if __name__ == "__main__":
    app.run(debug=True)
