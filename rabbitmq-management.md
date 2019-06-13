# Active rabbitmq management plugin

## This procedure is only for development, not for production server.

* `echo "[rabbitmq_management]." > /etc/rabbitmq/enabled_plugins`

* Add the following line to `/etc/rabbitmq/rabbitmq.config`:
```
{loopback_users, []
```

The file should be like:
```
[
    {rabbit, [
                    {disk_free_limit, 100000000},
                    {tcp_listeners, [{"0.0.0.0", 5672}]},
                    {heartbeat, 0},
                    {loopback_users, []}
             ]
    }
].
```
* `systemctl restart rabbitmq-server.service`

Now you can go to http://<ip>:15672
