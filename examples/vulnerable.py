"""Vulnerable sample for testing KV-14"""
def get_user(request):
    query = "SELECT * FROM users WHERE id = " + request["id"]  # injection
    eval(request["code"])  # critical
    return query

def divide(a, b):
    return a / b  # no zero guard
