#!/usr/bin/env bash
sudo tshark -i any -Y 'http or tls.handshake.extensions_server_name or dns' -Tfields -e ip.src -e ip.dst -e tls.handshake.extensions_server_name -e dns.resp.name -e http.host -e dns.a -e dns.aaaa > $1
