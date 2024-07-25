from flask import (Flask, Response, render_template, request,
                   stream_with_context)

from chatbot import ask_question

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chatbot", methods=["POST"])
def chatbot():
    question = request.form.get("question")
    if not question:
        return "Please provide a question", 400
    data = ask_question(question)
    return Response(stream_with_context(data), content_type="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True)
