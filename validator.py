def validate_response(response, bill_data):
    for value in bill_data.values():
        if str(value) not in response:
            return False
    return True