# Uptime

A very primitive and simple uptime monitor for your internal microservices.

Create a `config.json` to get started:

```json
{
  "services": {
    "website": {
      "url": "https://rashiq.me"
    },
    "simpledeploy": {
      "url": "https://deploy.rashiq.me"
    },
    "analytics": {
      "url": "127.0.0.1",
      "port": 8080
    }
  },
  "down": [
    "sendgrid --subject '$SERVICE is down!' --body 'you better do something'"
  ],
  "up": [
  ]
}
```

You can specify a list of steps in `up` or `down`. For now it's just going to execute them and replace `$SERVICE` with the actual affected service.

You can set up a cron job to make this script run every hour or so.

```
0 * * * * python /app/uptime/uptime.py
```

<img src="https://analytics.rashiq.me/uptime-gh.png" width="0px" height="0px" style="display:none;"/>
