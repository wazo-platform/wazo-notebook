# Bus events guidelines

## Do not send an updated list

When emitting an event regarding a single resource, do not send a list of all resources. Only send an event about the updated resource.

This leaves more flexibility for the receiving client: it does not have to refresh everything.
