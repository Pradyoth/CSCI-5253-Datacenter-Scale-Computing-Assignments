from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'datacenter5'  # TODO: Update placeholder value.

# The name of the zone for this request.
zone = 'us-central1-f'  # TODO: Update placeholder value.

# Name of the instance scoping this request.
instance = 'demo-instance'  # TODO: Update placeholder value.

tags_body = {
    # TODO: Add desired entries to the request body.
    "name":"demonstrate-allow-5000"
}

request = service.instances().setTags(project=project, zone=zone, instance=instance, body=tags_body)
response = request.execute()
pprint(response)