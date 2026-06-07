from flask import Flask,render_template,request,jsonify
from prometheus_client import Counter,generate_latest
from prometheus_client import Histogram
import random
import time

app = Flask(__name__)
APP_VERSION = "v3-dockerized"

#Prometheus metrics
REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total App Requests'  
)

REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds',
    'Request latency'
)

choices = ["rock","paper","scissors"]

def determine_winner(user,computer):
    if user == computer:
        return "Draw"
    
    wins = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if wins[user] == computer:
        return "You Win!"
    else:
        return "Computer Wins!"
    
@app.route("/", methods=["GET", "POST"])
def index():
    REQUEST_COUNT.inc()

    start_time = time.time()

    result = None
    user_choice = None
    computer_choice = None

    if request.method == "POST":
        user_choice = request.form["choice"]
        computer_choice = random.choice(choices)

        result = determine_winner(user_choice, computer_choice)
    
    latency = time.time() - start_time
    REQUEST_LATENCY.observe(latency)

    return render_template(
        "index.html",
        result=result,
        user_choice=user_choice,
        computer_choice=computer_choice,
        version=APP_VERSION
    )

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200

@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000)
    
