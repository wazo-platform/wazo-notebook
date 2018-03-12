# Pagination and collection result in REST API

## Collection result

* `items`: Result of objects filtered
* `filtered`: Number of object filtered by the filtering keys except from `limit` and `offset`
* `total`: Number total of objects without filters

```
{
    ...
    "items": [
        {
            "uuid": "00000000-0000-0000-0000-aaaaaaaaaaaa",
            "name": "My object"
        },
        {
            "uuid": "00000000-0000-0000-0000-bbbbbbbbbbbb",
            "name": "Other object"
        }
     ],
     "filtered": 2,
     "total": 4
    }
}
```
