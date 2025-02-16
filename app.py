import logging
from re import DEBUG
from flask import Flask
from datetime import date
from flask_bcrypt import Bcrypt
 

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.debug = True
app.secret_key = "hfldshfds34234dfds"

logging.basicConfig(
    filename="public/logs/app-"+date.today().strftime("%Y-%m-%d")+".log",
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
    level=logging.DEBUG
    )

logger = logging.getLogger()

@app.route("/")
def index():
    return "Hello, World!"
