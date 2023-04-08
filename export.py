#!/usr/bin/python3

import base64
import json
from pathlib import Path

# Get the path of the current directory
path = Path(__file__).parent

# Use context managers while opening files
with open(path.joinpath('xray/config/config.json'), 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

caddy = open(path.joinpath('caddy/Caddyfile'), 'r', encoding='utf-8').read()

uuid = config['inbounds'][0]['settings']['clients'][0]['id']

# Remove http:// or https:// prefix from domain
domain = caddy[:caddy.find(' {')].lstrip("http://").lstrip("https://")

j = json.dumps({
    "v": "2", 
    "ps": domain, 
    "add": domain, 
    "port": "443", 
    "id": uuid, 
    "aid": "0", 
    "net": "ws", 
    "type": "none",
    "host": domain, 
    "path": "/ws", 
    "tls": "tls"
})

# Use f-strings to format strings
print(f"vmess://{base64.b64encode(j.encode('ascii')).decode('ascii')}")
