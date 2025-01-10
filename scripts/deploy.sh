#!/bin/sh
# Usage: sh scripts/deploy.sh NAMESPACE IMAGE
namespace=${1:-default}
image=${2:-parcel-api:latest}
kubectl -n "$namespace" set image deployment/parcel-api parcel-api="$image"
echo "Deployment complete"
