#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/ping')
def ping():
    return 'pong';

if __name__ == "__main__":
    p = None
    try:
        app.run(debug=True)
    except:
        if p:
            p.kill()
        raise
