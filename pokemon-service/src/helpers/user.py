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

