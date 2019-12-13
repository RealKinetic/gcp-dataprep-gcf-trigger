# gcp-dataprep-gcf-trigger

Trigger a Dataprep job when a file is uploaded to Cloud Storage using a Cloud
Function. This works by calling the [Dataprep
API](https://cloud.google.com/dataprep/docs/html/API-Overview_145281442).

For triggering Dataprep flows using Dataflow templates directly rather than
the Dataprep API, see
[gcp-dataflow-gcf-trigger](https://github.com/RealKinetic/gcp-dataflow-gcf-trigger).

## Deploying

Run the following command to deploy this Cloud Function:

```
$ gcloud functions deploy <function-name> \
    --entry-point trigger \
    --trigger-bucket gs://<my-bucket> \
    --set-env-vars RECIPE_ID=<dataprep-recipe>,DATAPREP_TOKEN=<dataprep-token> \
    --runtime python37
```

Ensure that the trigger bucket matches the bucket used for the Dataprep
recipe.

## Environment Variables

As shown above, this Cloud Function requires two environment variables:

- `RECIPE_ID`: the ID of the Dataprep recipe to start jobs for. The provided
recipe must have a parameterized dataset with a variable called `file` which
is the file to process from the configured bucket.
- `DATAPREP_TOKEN`: [Dataprep access token](https://cloud.google.com/dataprep/docs/html/Access-Tokens-Page_145281436)
used to authenticate with the Dataprep API
