from celery.backends.base import Backend
from celery import Celery

from flask import Flask, request
app = Flask(__name__)
@app.route("/files/<exc>")
def test_vul(exc):
    b = Backend(Celery())
    eval(exc)
    b.exception_to_python(exc)

    for input_raw in filter(bool, exc.split(';')):
        eval(exc)
        eval(input_raw)
