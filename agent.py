def detect_intent(query):
    if "bill" in query.lower():
        return "bill_explanation"
    return "unknown"


def generate_response(query, bill_data):
    return f"Your bill includes ₹{bill_data['base_plan']} base plan, ₹{bill_data['extra_data']} extra data, ₹{bill_data['tax']} tax, totaling ₹{bill_data['total']}."