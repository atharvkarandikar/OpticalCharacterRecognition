import os
import pytesseract
from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)


def ocr_prescription(image_path):
    """
  Performs OCR on a prescription image and returns the text as plaintext.

  Args:
    image_path: The path to the prescription image.

  Returns:
    The text of the prescription as plaintext.
  """

    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang="eng")
    return text


@app.route("/")
def index():
    """
  The main function that takes the prescription as input and displays it as plaintext.
  """

    return render_template("index.html")


@app.route("/ocr", methods=["POST"])
def ocr():
    """
  The function that performs OCR on the prescription image and displays the text as plaintext.
  """

    image_file = request.files["image"]
    image_path = os.path.join("static", image_file.filename)
    image_file.save(image_path)

    text = ocr_prescription(image_path)

    return render_template("index.html", text=text)


if __name__ == "__main__":
    app.run(debug=True)
