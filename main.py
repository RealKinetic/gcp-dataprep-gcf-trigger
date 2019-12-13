import os
import requests


RECIPE_ID = int(os.getenv('RECIPE_ID'))
DATAPREP_TOKEN = os.getenv('DATAPREP_TOKEN')
JOB_URL = 'https://api.clouddataprep.com/v4/jobGroups'


def trigger(event, context):
    """Triggered by a change to a Cloud Storage bucket. This will start a
    Dataprep job based on the configured recipe for files uploaded to Cloud
    Storage. This function expects a parameterized dataset with a single
    parameter called "file" which is the name of the file to process in the
    configured bucket. Ensure that the dataset bucket used in Dataprep matches
    the bucket configured for the Cloud Function trigger.

    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """

    payload = {
        'wrangledDataset': {
            'id': RECIPE_ID,
        },
        'runParameters': {
            'overrides': {
                'data': [{
                    'key': 'file',
                    'value': event['name'],
                }]
            }
        }
    }
    headers = {
        'Authorization': 'Bearer {}'.format(DATAPREP_TOKEN)
    }

    # Start the Dataprep job.
    print("Starting Dataprep job for recipe '{}'".format(RECIPE_ID))
    resp = requests.post(JOB_URL, json=payload, headers=headers)
    resp.raise_for_status()
    job = resp.json()['id']
    print("Dataprep job '{}' created".format(job))

