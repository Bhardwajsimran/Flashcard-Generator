from flask import Flask, render_template, request

app = Flask(__name__)

def generate_flashcards(text):

    sentences = text.split(".")
    flashcards = []

    for sentence in sentences:
        sentence = sentence.strip()

        if len(sentence) > 5:

            question = "Explain: " + sentence + "?"
            answer = sentence

            flashcards.append({
                "question": question,
                "answer": answer
            })

    return flashcards


@app.route("/", methods=["GET","POST"])
def index():

    flashcards = []

    if request.method == "POST":

        text = request.form["text"]

        flashcards = generate_flashcards(text)

    return render_template("index.html", flashcards=flashcards)


if __name__ == "__main__":
    app.run(debug=True)
