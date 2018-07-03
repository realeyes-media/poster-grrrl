# Poster Grrrl
A notification container to send Slack Notifications from Bitbucket Pipelines, or any other shell-based/Docker enabled build process.

usage: app-notify.py [-h] --appname APPNAME --version VERSION -u URL --build BUILD --slug SLUG --orgname ORGNAME --title TITLE --destination DESTINATION

optional arguments:
  -h, --help            show this help message and exit
  --appname APPNAME     Name of the app
  --version VERSION     The version of this app
  -u URL, --url URL     URL for the Slack Webhook to send
  --build BUILD         The Bitbucket Build Number
  --slug SLUG           The Bitbucket repo slug
  --orgname ORGNAME     The organization name for Bitbucket as it appears in
                        the browser
  --title TITLE         The Title for the Slack notification
  --destination DESTINATION
                        The base URL for the production app