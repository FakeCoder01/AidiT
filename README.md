# AidiT

**AidiT** (AI Edit Tool) is a Django-based web application designed to leverage AI capabilities for editing imaging. Built with simplicity and efficiency in mind, AidiT provides an intuitive interface and backend powered by AI tools.

## Features

- 🌐 Django-powered backend for robust and scalable performance.
- 🧠 Integrates LLM for editing images or generating new images.
- 📁 Modular directory structure for easy maintenance and future extension.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.8+
- pip
- virtualenv (optional but recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/FakeCoder01/AidiT.git
cd AidiT

# (Optional) Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install the dependencies
pip install -r requirements.txt

# Run the development server
python manage.py runserver
```

Install them via:

```bash
pip install -r requirements.txt
```

## Project Structure

```
AidiT/
├── AIEdit/         # AI editing module
├── app/            # Django app code
├── static/         # Static files (CSS, JS, etc.)
├── template/       # HTML templates
├── manage.py       # Django's command-line utility
└── requirements.txt
```

## Usage

Once the development server is running, navigate to `http://127.0.0.1:8000/` in your browser. Use the interface to interact with AI editing tools.
