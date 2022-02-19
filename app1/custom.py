def get_serializer_errors(serializer):
    error_keys=list(serializer.errors.keys())
    print(error_keys)
    if error_keys:
        error_msg=serializer.errors[error_keys[0]]
        return {'message': error_msg[0]}
    else:
        return serializer.errors