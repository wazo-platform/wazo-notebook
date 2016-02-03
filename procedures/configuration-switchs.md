Cisco Small Business
--------------------

- Security \> Traffic Control \> Port Security : Unlock all ports
- Monitor & Device Properties \> CDP : CDP Status Disable
- Monitor & Device Properties \> Bonjour : Disable Bonjour

Netgear ProSafe GS110TP
-----------------------

- Pour que les switchs netgear puissent supporter les téléphones Cisco via POE, il faut configurer le switch tel que :

```
System / poe / advanced / poe port configuration :  detection mode = 802.3af 2point and legacy
```
