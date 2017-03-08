Cisco Small Business
--------------------

- Security \> Traffic Control \> Port Security : Unlock all ports
- Monitor & Device Properties \> CDP : CDP Status Disable
- Monitor & Device Properties \> Bonjour : Disable Bonjour

Netgear ProSafe GS110TP
-----------------------

- Pour que les switchs netgear puissent supporter les téléphones Cisco via POE,
  il faut configurer le switch tel que :

```
System / poe / advanced / poe port configuration :  detection mode = 802.3af 2point and legacy
```

Debugging
---------

Si les téléphones Cisco ont des symptômes bizarres comme "le DHCP ne fonctionne
pas" après une coupure de courant, il y a sûrement un switch Cisco quelque part
qui balance du CDP et qui reset le VLAN du téléphone à 100.
