from celery.backends.base import Backend
from celery import Celery

from flask import Flask, request
app = Flask(__name__)
@app.route("/files/<exc>")
def test_vul(exc):
    b = Backend(Celery())
    b.exception_to_python(exc)

    eval(exc)

