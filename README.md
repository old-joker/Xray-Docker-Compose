# Xray-Docker-Compose
Xray Server Docker Compose ( Vmess + Websockets + TLS + CDN )

In this solution, you need to buy a vps and a domain/subdomain added to a CDN service.

  VPS : A server that has free access to the Internet.
  
  CDN Service: A Content delivery network like Cloudflare, ArvanCloud or DerakCloud.

    (Client) <-> [ CDN Service ] <-> [ Server ] <-> (Internet)

This solution provides VMESS over Websockets + TLS + CDN.

Follow these steps to setup Xray + Caddy (Web server) + CDN:

   1. In your CDN, create an A record pointing to your server IP with the proxy option turned off.
   1. Install Docker and Docker-compose on your server.
   1. Git clone this repo into the server. (git clone https://github.com/old-joker/Xray-Docker-Compose.git)
   1. Run cat /proc/sys/kernel/random/uuid to generate a UUID.
   1. Replace <YOUR-UUID> in xray/config/config.json with the generated UUID.
   1. Replace <EXAMPLE.COM> in caddy/Caddyfile with your domain/subdoamin.
   1. Run docker-compose up -d.
   1. Visit your domain/subdomain in your web browser. Wait until the homepage is loaded.
   1. (Optional) In your CDN, turn the proxy option on for the record.
   1. Run ./export.py to generate client configuration (link).

Some CDN services don't offer unlimited traffic for free plans. Please check CDN Free Plans.

You don't need to turn the cloud (proxy) on in your CDN (step 9) when the Internet is not blocked. When it's off, clients connect to the server directly and CDN services also don't charge you any fee.
