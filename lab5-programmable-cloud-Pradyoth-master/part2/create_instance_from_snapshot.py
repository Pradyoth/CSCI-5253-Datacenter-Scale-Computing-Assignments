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
       "tags": {"items": ["demonstrate-allow-5000"]}
}
request = service.instances().insert(project=project, zone=zone, body=instance_body)
response = request.execute()
end_time1 = datetime.now()
f.write("Duration of instance-1: {}\n".format(end_time1 - start_time1))

# TODO: Change code below to process the response dict:
pprint(response)




start_time2 = datetime.now()
instance_body = {
   # TODO: Add desired entries to the request body.
       "name": "cloned-instance-2",
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
       "tags": {"items": ["demonstrate-allow-5000"]}
}
request = service.instances().insert(project=project, zone=zone, body=instance_body)
response = request.execute()
end_time2 = datetime.now()
f.write("Duration of instance-2: {}\n".format(end_time2 - start_time2))
# TODO: Change code below to process the response dict:
pprint(response)


start_time3 = datetime.now()
instance_body = {
   # TODO: Add desired entries to the request body.
       "name": "cloned-instance-3",
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
       "tags": {"items": ["demonstrate-allow-5000"]}
}
request = service.instances().insert(project=project, zone=zone, body=instance_body)
response = request.execute()
end_time3 = datetime.now()
# TODO: Change code below to process the response dict:
pprint(response)
f.write("Duration of instance-3: {}\n".format(end_time2 - start_time2))