import json

from fastapi.responses import Response

from sqlalchemy.exc import IntegrityError

from services.data_provider_service.data_provider import DataProvider

dbcore = DataProvider()


def catch_check_error(e):
    hash_code = abs(hash(e.args[0]))
    first_two_digits = str(hash_code)[:2]
    resp_status = 400
    if isinstance(e, IntegrityError):
        if "UniqueViolation" in e.args[0]:
            resp_status = 403
    res = {"errorMessage": f"{e.args[0]}", "errorCode": f"{resp_status}{first_two_digits}"}
    return Response(status_code=resp_status, content=json.dumps(res))
