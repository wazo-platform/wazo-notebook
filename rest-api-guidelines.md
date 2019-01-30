# REST API guidelines

## Rationale

When writing new REST APIs, there are multiple ways to achieve the same feature.


## Robustness principle

Try to follow the [Robustness Principle](https://en.wikipedia.org/wiki/Robustness_principle):

> Be conservative in what you do, be liberal in what you accept from others

## REST API call = desired state, when possible

Example:

```
# Delete a user
DELETE /user/12
> 204
# Delete the same user again
DELETE /user/12
> 204, not 404
```

Generalization: do not raise an error if the desired state of a resource is already attained.

## PUT response = no body

When receiving a PUT query, do not send the resource back in response.

Pros:
- less bandwidth
- still available in edit event and query body
- generally unused

Cons:
- body may be useful
- resource may be deleted right after the PUT and won't be available by GET
