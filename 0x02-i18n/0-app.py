#!/usr/bin/env python3
from flask import Flask, render_templete
ap = Flask(__name__)

@ap.route('/')
def welcome_page():
    """hompage"""
    return render_template('index.html')

if __name__ == '__main__':
    ap.run(Debug=True)
