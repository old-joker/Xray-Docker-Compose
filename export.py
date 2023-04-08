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

domain = caddy[:caddy.find(' {')]

# Check if domain starts with "http://" or "https://"
if domain.startswith("http://") or domain.startswith("https://"):
    # Remove the prefix using lstrip() only if it is present
    domain = domain.lstrip("http://").lstrip("https://")

    j = {
        "v": "2", 
        "ps": domain, 
        "add": domain, 
        "port": "80", 
        "id": uuid, 
        "aid": "0", 
        "net": "ws", 
        "type": "none",
        "host": domain, 
        "path": "/ws"
    }
else : 
    j = {
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
    }

# Use json.dumps() to encode the JSON string
json_str = json.dumps(j)

# Use base64.b64encode() to encode the JSON string in base64
b64_str = base64.b64encode(json_str.encode('ascii')).decode('ascii')

# Use f-strings to format strings
print(f"vmess://{b64_str}")
