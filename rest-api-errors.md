# Errors in REST API

## Rationale

Errors should be as informative as possible when presented to the user. Hence, the REST API must give as much information as possible, and this information must be structured. A simple error message is not enough: it can't be translated easily, it does tell a GUI what field caused the error, etc.

## Error structure

When an error occurs during a HTTP request on a REST API, the error returned must be in JSON format, with the following structure:

```
{
    "error_id": "not-found",  # this field serves as a "sub-status-code", e.g. to distinguish between two different 400 status codes that don't have the same cause
    "message": "No such user ID: 'abcdefg-1234'",  # this should be human-readable
    "resource": "user",  # this helps abstracting the client-side logic, giving back the context of the request
    "resource_id": "abcdefg-1234",  # idem. This field is optional. The value may be a dictionary.
    "timestamp": 1500908147.0837858,  # the timestamp when the error occured
    "details": {
        # as many details as we want about this error, usually what field is invalid and why
    }
}
```

## Error details structure for invalid request

When returning a 400 status code, the error details should have this structure:

```
{
    ...
    "details": {
        "field1": {
            "constraint_id": "regex",
            "constraint": "[a-z]+",
            "message": "field1 must be lowercase alphabetic"
        },
        "field2": {
            ...
        }
    }
}
```

In case of a nested request, the details should be nested as well. Example:

Request:
```
{
    "config": {
        "url": "invalid"
    }
}
```

Response:
```
    "error_id": "invalid-data",
    "message": "Invalid request",
    "resource": "subscription",
    "resource_id": "abcdefg-1234",
    "timestamp": 1500908147.0837858,
    "details": {
        "config": {
            "url": {
                "constraing_id": "url",
                "constraint": {
                    "schemes": ["http", "https"]
                },
                "message": "Invalid URL"
            }
        }
    }
```
