"""
Text To QR Web App
========================================

A compact Flask-based web application that generates Quick Response (QR) codes
from user-supplied text or URLs. It provides a simple web interface for input
and allows users to download generated QR codes instantly.

Key Features:
-------------
- Convert text/URLs into QR codes dynamically.
- Uses in-memory streaming (no file saving needed).
- Environment-driven configuration for flexibility.
- Well-documented and type-hinted for maintainability.

Dependencies:
-------------
- Flask: Web framework.
- qrcode: QR code generation library.
- python-dotenv: Environment variable management.

Environment Variables:
----------------------
- IS_DEBUG (str): If 'true' or '1', enables Flask debug mode.
"""

from __future__ import annotations
import io
import os
from typing import Union, Tuple
from flask import Flask, render_template, request, send_file, jsonify, Response
from werkzeug.exceptions import BadRequest
from qrcode import QRCode
import dotenv


# Flask App Initialization
app = Flask(__name__)

# Load environment variables (from .env)
dotenv.load_dotenv()


# Utility Functions
def generate_qr_code(data: str) -> io.BytesIO:
    """
    Generates a QR code image in memory for the given text data.

    Parameters
    ----------
    data : str
        The text or URL to encode into a QR code.

    Returns
    -------
    io.BytesIO
        A byte stream containing the PNG image of the QR code.
    """
    qr = QRCode(version=1, box_size=10, border=5)
    qr.add_data(data.strip())
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer


def is_truthy(value: str) -> bool:
    """Helper to interpret common truthy environment variable values."""
    return str(value).lower() in {"true", "1", "t", "yes", "y"}


# Routes
@app.route("/", methods=["GET", "POST"])
def home() -> Union[str, Response, Tuple[Response, int]]:
    """
    Main endpoint for displaying the form and generating QR codes.

    Methods
    -------
    GET:
        Render the home page containing the input form.
    POST:
        Process the input data and return a downloadable QR code image.

    Returns
    -------
    Union[str, Response, Tuple[Response, int]]
        - Rendered HTML for GET requests.
        - PNG file download for successful POST requests.
        - JSON error with 400 status for invalid input.
    """
    if request.method == "POST":
        data = request.form.get("data", "").strip()

        # Basic validation
        if not data:
            return jsonify({"error": "No text provided for QR generation."}), 400

        if len(data) > 1000:
            # Security measure: prevent huge payloads
            raise BadRequest("Input too long. Please limit text to 1000 characters.")

        # Generate QR code
        qr_stream = generate_qr_code(data)

        # Send file response with correct headers
        response = send_file(
            qr_stream,
            mimetype="image/png",
            as_attachment=True,
            download_name="qrcode.png",
        )
        response.headers["Cache-Control"] = "no-store"
        return response

    # Render home page
    return render_template("index.html")


@app.route("/about", methods=["GET"])
def about() -> str:
    """
    Displays the 'About' page, providing app details and purpose.

    Returns
    -------
    str
        Rendered HTML for the About page.
    """
    return render_template("about.html")


@app.route("/contact", methods=["GET"])
def contact() -> str:
    """
    Displays the 'Contact' page for reaching the developers.

    Returns
    -------
    str
        Rendered HTML for the Contact page.
    """
    return render_template("contact.html")


# Application Entry Point
if __name__ == "__main__":
    debug_mode = is_truthy(os.getenv("IS_DEBUG", "False"))
    host = os.getenv("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_RUN_PORT", 5000))

    app.run(host=host, port=port, debug=debug_mode)
