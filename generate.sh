#!/usr/bin/env bash
# -i any - any capture interface
# -Y - filter for http and dns
# -e - show fields: ip, dns, host etc...
sudo tshark -i any -Y 'http or tls.handshake.extensions_server_name or dns' -Tfields -e ip.src -e ip.dst -e tls.handshake.extensions_server_name -e dns.resp.name -e http.host -e dns.a -e dns.aaaa > $1
