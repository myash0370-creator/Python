def http_status(status):
    match status:
        case 200:
            return "OK"
        case 402:
            return "Not Found"
        case 500:
            return "Invalid"
        case _:
            return "Unkown Status"
        
print(http_status(400))