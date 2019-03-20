ifconfig ens4 10.14.20.20
ifconfig ens4 netmask 255.255.255.0
route add -net 10.0.0.0 netmask 255.0.0.0 gw 10.14.20.14
