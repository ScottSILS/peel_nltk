peel_nltk
=========

Using Python's Natural Language Toolkit (NLTK) to parse named entities out of OCR'd newspapers from the University of Alberta PEEL Repository.

Usage:

If you don’t already have virtualenv, install it:

    pip install virtualenv

Enter the project directory and create a new virtualenv:

    cd mods_nltk/ && virtualenv venv

Activate the virtualenv:

    source venv/bin/activate

Install the required packages:

    pip install -r requirements.txt

Run the Named Entity Recognition (ner) script!

    python ner.py

