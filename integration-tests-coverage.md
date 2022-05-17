Tests coverage
===

Database
---

Given the database server has been restarted
When a query is made with the old connection

Given the database server is down
When a query is made

When an insert/update/delete violates integrity rules
Then the error is logged
Then the transaction is not locked (see wazo-tools/dev-tools/list-stuck-pg-connections.py)


REST API
---

When I make a request with no token
When I make a request with wrong tenant
When I make a request with wrong resource_id

When I make a POST/PUT/DELETE request
When I make the exact same request a second time

When I make a POST/PUT/DELETE request 10 times in a row without waiting
