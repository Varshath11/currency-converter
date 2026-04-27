from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Function to get exchange rate
def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    
    rate = data['rates'][to_currency]
    converted_amount = amount * rate
    return round(converted_amount, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        from_currency = request.form["from_currency"].upper()
        to_currency = request.form["to_currency"].upper()
        amount = float(request.form["amount"])

        result = convert_currency(from_currency, to_currency, amount)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)