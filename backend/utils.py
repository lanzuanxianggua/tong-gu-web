from rest_framework import status
from rest_framework.response import Response


def error_response(message, errors=None, status_code=status.HTTP_400_BAD_REQUEST):
    resp = {'message': message}
    if errors:
        resp['errors'] = errors
    return Response(resp, status=status_code)
