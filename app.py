from flask import Flask, render_template_string

app = Flask(__name__)

HOME_HTML = """<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Flask CI App</title></head>
<body>
  <h1>Welcome</h1>
  <p>This is a simple Flask app for CI.</p>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HOME_HTML)


if __name__ == "__main__":
    app.run(debug=True)
