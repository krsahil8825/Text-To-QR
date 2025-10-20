# Text To QR Web App

A **basic Flask web application** that converts any text or URL into a **QR code image** instantly.
You can enter text in the form, and the app will generate and download the QR code as a PNG file.

## Features

-   Generate QR codes from text or URLs
-   Download the QR code instantly as a `.png` file
-   Simple and clean Flask app structure
-   Includes basic pages: **Home**, **About**, and **Contact**
-   Uses environment variables for configuration (via `.env` file)

## How It Works

1. You open the app in your browser.
2. Enter text or a URL in the input box.
3. Click **Generate QR**.
4. The app creates a QR code image and lets you download it instantly.

## Technologies Used

-   **Python 3.x**
-   **Flask** (for the web framework)
-   **qrcode** (for QR code generation)
-   **python-dotenv** (for managing environment variables)

## Installation & Setup

### 1. Clone or Download the Project

```bash
git clone https://github.com/krsahil8825/text-to-qr.git
cd text-to-qr
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

Create a file named `.env` in the project root and add:

```
IS_DEBUG=True
```

### 5. Run the App

```bash
python app.py
```

Then open your browser and visit:
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Project Structure

```
text-to-qr/
│
├── app.py               # Main Flask app
├── templates/
│   ├── index.html       # Home page (QR form)
│   ├── about.html       # About page
│   └── contact.html     # Contact page
├── .env                 # Environment variables
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Example

**Input:**

```
https://www.google.com
```

**Output:**
A downloadable `qrcode.png` image containing a QR code that opens Google.

## License

This project is open-source and free to use for learning purposes.
