from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, jsonify
from data_loader import load_data, get_bill
from agent import detect_intent, generate_response
from validator import validate_response

app = Flask(__name__)

data = load_data()

@app.route("/query", methods=["POST"])
def handle_query():
    user_id = "user_1"
    query = request.json.get("query")

    intent = detect_intent(query)

    if intent != "bill_explanation":
        return jsonify({"response": "Please ask about your bill."})

    bill_data = get_bill(data, user_id)

    response = generate_response(query, bill_data)

    if not validate_response(response, bill_data):
        return jsonify({"response": "Connecting you to support..."})

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)