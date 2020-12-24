from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'datacenter5'  # TODO: Update placeholder value.

firewall_body = {
    # TODO: Add desired entries to the request body.
    "name": "allow-5000", "description": "", "network": "https://www.googleapis.com/compute/v1/projects/datacenter5/global/networks/default", "priority": 1000, "sourceRanges": ["0.0.0.0/0"], "targetTags": ["demonstrate-allow-5000"], "allowed": [{"IPProtocol": "tcp", "ports": ["5000"]}], "direction": "INGRESS", "logConfig": {"enable": False}, "disabled": False, "selfLink": "https://www.googleapis.com/compute/v1/projects/datacenter5/global/firewalls/allow-5000", "kind": "compute#firewall"
}

request = service.firewalls().insert(project=project, body=firewall_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)



