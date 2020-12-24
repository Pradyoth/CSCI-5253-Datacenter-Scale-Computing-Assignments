from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('compute', 'v1', credentials=credentials)

# Project ID for this request.
project = 'datacenter5'  # TODO: Update placeholder value.

# The name of the zone for this request.
zone = 'us-central1-f'  # TODO: Update placeholder value.

# Name of the persistent disk to snapshot.
disk = 'demo-instance'  # TODO: Update placeholder value.

snapshot_body = {
    # TODO: Add desired entries to the request body.
    "name":"base-snapshot-demo-instance"
}

request = service.disks().createSnapshot(project=project, zone=zone, disk=disk, body=snapshot_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)


