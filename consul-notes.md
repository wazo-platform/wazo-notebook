Consul it is a tool for discovering and configuring services in your infrastructure.

Key features :

* Service Discovery: Clients of Consul can provide a service, such as api or mysql and other clients can use Consul to discover providers of a given service. Using either DNS or HTTP. Applications can easily find the services they depend upon.
* Health Checking: Consul clients can provide any number of health checks, either associated with a given service ("is the webserver returning 200 OK"), or with the local node ("is memory utilization below 90%"). This information can be used by an operator to monitor cluster health, and it is used by the service discovery components to route traffic away from unhealthy hosts.
* Key/Value Store: Applications can make use of Consul's hierarchical key/value store for any number of purposes, including dynamic configuration, feature flagging, coordination, leader election and more. The simple HTTP API makes it easy to use.
* Multi Datacenter: Consul supports multiple datacenters out of the box. This means users of Consul do not have to worry about building additional layers of abstraction to grow to multiple regions.

Consul agent listens on 6 different ports, all of which serve different functions:

¦ Function      ¦ Ports         ¦ Description ¦
¦ ------------- ¦ ------------- ¦ ------------¦
¦ Server RPC    ¦ 8300 /TCP     ¦ Used by servers to handle incoming requests from other agents. ¦
¦ Serf LAN      ¦ 8301 /TCP-UDP ¦ Used by all agents to handle gossip in the LAN. ¦
¦ Serf WAN      ¦ 8302 /TCP-UDP ¦ Used by servers to gossip over the WAN to other servers. ¦
¦ CLI RPC       ¦ 8400 /TCP     ¦ Used by all agents to handle RPC from the CLI. ¦
¦ HTTP API      ¦ 8500 /TCP     ¦ Used by clients to talk to the HTTP API, and used by servers to handle HTTP API requests from clients and the web UI. ¦
¦ DNS Interface ¦ 8600 /TCP-UDP ¦ Used to resolve DNS queries. ¦




