# TODO Change the resource group, embedding model ID and LLM/Chat model ID to your own
RESOURCE_GROUP = "default" # your resource group e.g. team-01
# RESOURCE_GROUP = "L2ACSOPCOM" # your resource group e.g. team-01
EMBEDDING_DEPLOYMENT_ID = "d0e8b15aaa3a39c8" # e.g. d6b74feab22bc49a
LLM_DEPLOYMENT_ID = "d2eadf2c6f656bbd"

# TODO Change the URL to your own orchestration deployment ID
AICORE_ORCHESTRATION_DEPLOYMENT_URL = "https://api.ai.intprod-eu12.eu-central-1.aws.ml.hana.ondemand.com/v2/inference/deployments/d0a6c652fb457754"
# AICORE_ORCHESTRATION_DEPLOYMENT_URL = "https://api.ai.intprod-eu12.eu-central-1.aws.ml.hana.ondemand.com/v2/inference/deployments/dff75c767fa0d0e5"

# HANA table name to store your embeddings
# TODO Change the name to your team name
EMBEDDING_TABLE = "EMBEDDINGS_CODEJAM_"+"SANDEEP"
