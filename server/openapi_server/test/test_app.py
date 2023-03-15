import schemathesis
from schemathesis import DataGenerationMethod
from schemathesis.checks import (
    not_a_server_error,
    status_code_conformance,
    content_type_conformance,
    response_schema_conformance,
    response_headers_conformance,
)

from openapi_server import create_app


posschema = schemathesis.from_uri("http://127.0.0.1:8080/api/openapi.json")

negschema = schemathesis.from_uri(
    "http://127.0.0.1:8080/api/openapi.json",
    data_generation_methods=[DataGenerationMethod.negative],
)


@schemathesis.check
def check_4xx(response, case):
    if 400 <= response.status_code < 500:
        return

    raise AssertionError("Status code is not 4XX.")


@schemathesis.hook
def before_generate_case(context, strategy):
    op = context.operation

    def tune_case(case):
        if op.method == "post" and op.path == "/users/{name}":
            try:
                if "name" in case.body and case.body["name"]:
                    if "/" in case.body["name"] or "?" in case.body["name"]:
                        return case
                    case.path_parameters["name"] = case.body["name"]
            except TypeError as e:
                pass
        return case

    return strategy.map(tune_case)


@posschema.parametrize()
def test_positive_test(case):
    checks = [
        not_a_server_error,
        status_code_conformance,
        content_type_conformance,
        response_schema_conformance,
        response_headers_conformance,
    ]

    response = case.call()
    case.validate_response(response, checks=checks)


@negschema.parametrize(method="post")
def test_negative_test(case):
    checks = [
        check_4xx,
        status_code_conformance,
        content_type_conformance,
        response_schema_conformance,
        response_headers_conformance,
    ]

    response = case.call()
    case.validate_response(response, checks=checks)
