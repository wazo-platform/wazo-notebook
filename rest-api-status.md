# What is in GET /status?

Each component in a daemon must be able to add values inside the body of `/status`.

## Example body

```
{
  "ari": {
    "status": "ok"
  },
  "bus_consumer": {
    "status": "ok"
  },
  "service_token": {
    "status": "ok"
  },
  "plugins": {
    "voicemails": {
      "cache_items": 12,
      "status": "ok"
    },
    "bad_plugin": {
      "status": "fail"
    }
  }
}
```

## Conventions

* Each key MAY have a `status` subkey. Each value associated to the `status` subkey MUST contain a string. Conventional values for this string are `ok` and `fail`. Other values are acceptable too, depending on the status being reported.

* If the key does not have a `status` value, the status SHOULD be considered `ok`.

* Key names must use `_` (underscore) as word separators.
