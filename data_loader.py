import json

def load_data():
    with open("sample_data.json") as f:
        return json.load(f)

def get_bill(data, user_id):
    return data.get(user_id, {}).get("bill", {})