# Pagination and collection in REST API

## Parameters

* `direction`: Sort list of items in 'asc' (ascending) or 'desc' (descending) order.
* `limit`: Maximum number of items to return in the list.
* `offset`: Number of items to skip over in the list.
* `order`: Name of the field to use for sorting the list of items returned.
* `recurse`: Should the query include sub-tenants.
* `search`: Search term for filtering a list of items. Only items with a field containing the search term will be returned.

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
