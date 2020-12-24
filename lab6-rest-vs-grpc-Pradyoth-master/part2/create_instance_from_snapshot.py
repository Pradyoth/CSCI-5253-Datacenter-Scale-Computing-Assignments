from pprint import pprint
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from datetime import datetime
credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)
# Project ID for this request.
project = 'datacenter5'  # TODO: Update placeholder value.
# The name of the zone for this request.
zone = 'us-central1-f'  # TODO: Update placeholder value.
f = open("TIMING.md", "w")
start_time1 = datetime.now()
instance_body = {
   # TODO: Add desired entries to the request body.
       "name": "cloned-instance-1",
       "machineType": "zones/%s/machineTypes/f1-micro" % zone,
       "networkInterfaces": [{
       "accessConfigs": [{
       "type": "ONE_TO_ONE_NAT",
       "name": "External NAT"
    }],
       "network": "global/networks/default"
    }],
       "disks": [{
       "boot": True,
       "initializeParams": {
         "sourceSnapshot":  "projects/datacenter5/global/snapshots/base-snapshot-demo-instance"
         }
       }],
       "tags": {"items": ["demonstrate-allow-5000"]},
       'metadata': {
             'items': [{
                 'key': 'startup-script',
                 'value': ''.join(['#!/bin/bash\n',
                                   'cd /home/vepr4844\n',
                                   'sudo python3 setup.py install\n',
                                   'sudo pip3 install -e .\n',
                    		   'sudo pip3 install pillow jsonpickle numpy\n',
                                   'python3 rest-client.py 34.68.217.40 add 1000\n',
                                   'python3 rest-client.py 34.68.217.40 image 1000\n'])
             }
}
request = service.instances().insert(project=project, zone=zone, body=instance_body)
response = request.execute()
end_time1 = datetime.now()
f.write("Duration of instance-1: {}\n".format(end_time1 - start_time1))

# TODO: Change code below to process the response dict:
pprint(response)







