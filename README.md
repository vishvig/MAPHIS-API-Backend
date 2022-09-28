# MAPHIS-API-Backend


The backend code is deployed using a GitHub workflow to AWS Elastic Container Service (ECS). The docker images are built and pushed to the Elastic Container Registry (ECR). Tile images are stored on an Elastic File System (EFS), which is similar to a Network File System (NFS). Amazon Data Sync is used to sync the data between EFS and S3, for backup purposes.  


Note: All the backend code is hosted in the AWS London region (eu-west-2)
