def validate_id(id): # Validate id function
    id_int = int(id)
    if id_int >= 1 and id_int <=10:
        return True
    return False

def RetrieveResponse(data, message): #Retrieve success response
    return {
        "data": data,
        "status_code": 200,
        "message": message
    }
def ErrorResponse(error): #Error response
    return {
        "status_code": 400,
        "error": error
    }

