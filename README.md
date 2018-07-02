# slack-notification-scripts
A collection of Slack notification scripts to simplify notifying from shell scripts

usage: app-notify.py [-h] --playername PLAYERNAME --version VERSION -u URL --build BUILD --slug SLUG --title TITLE --playerbase PLAYERBASE --playerend PLAYEREND

optional arguments:
  -h, --help                show this help message and exit
  --playername PLAYERNAME   Name of the app
  --version VERSION         The version of this app
  -u URL, --url URL         URL for the Slack Webhook to send
  --build BUILD             The Bitbucket Build Number
  --slug SLUG               The Bitbucket repo slug
  --title TITLE             The Title for the Slack notification
  --playerbase PLAYERBASE   The base URL for the production app
  --playerend PLAYEREND     The URL portion after the build number