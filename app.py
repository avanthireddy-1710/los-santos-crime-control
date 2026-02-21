from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Hackathon ML App</h1>
        <form method="POST" action="/predict">
            <input name="number" type="text" placeholder="Enter a number">
            <button type="submit">Predict</button>
        </form>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    number = float(request.form['number'])
    result = number * 2  # Dummy ML logic
    return f"<h2>Result: {result}</h2><br><a href='/'>Go Back</a>"

if __name__ == "__main__":
    app.run(debug=True)