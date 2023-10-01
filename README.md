# join-every-web-meeting
Never miss a meeting again.

## How to Use
You need to install Node.js  and Python before starting set up.
- Install dependencies modules

  `pip install -r requirements.txt`
- Start Fastify Server
`gunicorn main:app --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000` 
- Install [localtunnel](https://github.com/localtunnel/localtunnel) to o forward local ports and expose them to the outside world

  `npm install -g localtunnel`
- Start start the tunnel

  `lt --port 8000 --subdomain your-domain`