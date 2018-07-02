## Track yo (dang) features
# Requires Python 3.5+, ElasticSearch 6.2+, and most arguments are required

import argparse
import requests

#### Gather CLI arguments
# Requres a PR message to be passed in as a text file to --prmessage
parser = argparse.ArgumentParser()
parser.add_argument("--playername", help="Name of the app", required=True)
parser.add_argument("--version", help="The version of this app", required=True)
parser.add_argument("-u", "--url", help="URL for the Slack Webhook to send", required=True)
parser.add_argument("--build", help="The Bitbucket Build Number", required=True)
parser.add_argument("--slug", help="The Bitbucket repo slug", required=True)
parser.add_argument("--title", help="The Title for the Slack notification", required=True)
parser.add_argument("--playerbase", help="The base URL for the production app", required=True)
parser.add_argument("--playerend", help="The base URL for the production app", required=True)
args = parser.parse_args()

# Test
print("Here's the Player Name: " + args.playername)

# Send the Notification
prod_url = args.playerbase + args.build + args.playerend

payload = "{\n  \"attachments\": [\n    {\n      \"fallback\": \"" + args.playername + " Build " + args.version + " Delivered\",\n      \"color\": \"#2eb886\",\n      \"title\": \" " + args.playername + " Build " + args.version + " Delivered\",\n      \"title_link\": \"https://bitbucket.org/realeyesmedia/" + args.slug + "/addon/pipelines/home#!/results/" + args.build + "\",\n      \"text\": \"Build number: " + args.version + "\",\n      \"fields\": [\n        {\n          \"title\": \"" + args.title + "\",\n          \"value\": \"" + prod_url + "\",\n          \"short\": false\n        }\n      ]\n    }\n  ]\n}"

headers = {
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    }

response = requests.request("POST", args.url, data=payload, headers=headers)

print(response.text)

