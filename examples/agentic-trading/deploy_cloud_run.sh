#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Configuration ---
export PROJECT_ID="${PROJECT_ID:-your-gcp-project-id}" # Uses env var $PROJECT_ID if set, otherwise the default
export REGION="${REGION:-us-central1}"              # Uses env var $REGION if set, otherwise the default
export REPOSITORY_NAME="agentic-trading"

# Derived Artifact Registry path prefix
export AR_PREFIX="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY_NAME}"

# Service Names
export RISKGUARD_SERVICE_NAME="riskguard-service"
export ALPHABOT_SERVICE_NAME="alphabot-service"
export SIMULATOR_SERVICE_NAME="simulator-service"

# Cloud Build Config file names
export RISKGUARD_BUILDFILE="cloudbuild-riskguard.yaml"
export ALPHABOT_BUILDFILE="cloudbuild-alphabot.yaml"
export SIMULATOR_BUILDFILE="cloudbuild-simulator.yaml"

# Image tags (used for deployment after build)
export RISKGUARD_IMAGE_TAG="${AR_PREFIX}/riskguard:latest"
export ALPHABOT_IMAGE_TAG="${AR_PREFIX}/alphabot:latest"
export SIMULATOR_IMAGE_TAG="${AR_PREFIX}/simulator:latest"

# Check if PROJECT_ID is set
if [ "$PROJECT_ID" == "your-gcp-project-id" ]; then
  echo "ERROR: Please set your PROJECT_ID in the script before running."
  exit 1
fi

# --- Pre-flight Checks ---
echo "Using Project ID: $PROJECT_ID"
echo "Using Region: $REGION"
echo "Using Repository: $REPOSITORY_NAME"
echo "Artifact Registry Prefix: $AR_PREFIX"
echo "---"

# --- Setup Artifact Registry (if it doesn't exist) ---
echo "Creating Artifact Registry repository (if needed)..."
gcloud artifacts repositories create $REPOSITORY_NAME \
    --repository-format=docker \
    --location=$REGION \
    --description="Docker repository for agentic trading services" \
    --project=$PROJECT_ID || echo "Repository '$REPOSITORY_NAME' likely already exists in region '$REGION'."
echo "---"

# --- 1. Deploy RiskGuard ---
echo "Deploying RiskGuard..."

# Step 1.1: Build and Push Image using Cloud Build Config
echo "Building RiskGuard image using $RISKGUARD_BUILDFILE..."
gcloud builds submit . --config=$RISKGUARD_BUILDFILE \
    --substitutions=_REGION=$REGION,_REPO_NAME=$REPOSITORY_NAME \
    --project=$PROJECT_ID --quiet # Pass substitutions

# Step 1.2: Deploy to Cloud Run using the built image tag
echo "Deploying RiskGuard service ($RISKGUARD_SERVICE_NAME)..."
gcloud run deploy $RISKGUARD_SERVICE_NAME \
    --image=$RISKGUARD_IMAGE_TAG \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --project=$PROJECT_ID

# Step 1.3: Get Service URL
export RISKGUARD_SERVICE_URL=$(gcloud run services describe $RISKGUARD_SERVICE_NAME --platform managed --region $REGION --format 'value(status.url)' --project=$PROJECT_ID)
echo "RiskGuard URL: $RISKGUARD_SERVICE_URL"
echo "---"

# --- 2. Deploy AlphaBot ---
echo "Deploying AlphaBot..."

# Step 2.1: Build and Push Image using Cloud Build Config
echo "Building AlphaBot image using $ALPHABOT_BUILDFILE..."
gcloud builds submit . --config=$ALPHABOT_BUILDFILE \
    --substitutions=_REGION=$REGION,_REPO_NAME=$REPOSITORY_NAME \
    --project=$PROJECT_ID --quiet

# Step 2.2: Deploy to Cloud Run (passing RiskGuard URL)
echo "Deploying AlphaBot service ($ALPHABOT_SERVICE_NAME)..."
gcloud run deploy $ALPHABOT_SERVICE_NAME \
    --image=$ALPHABOT_IMAGE_TAG \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --set-env-vars="RISKGUARD_SERVICE_URL=$RISKGUARD_SERVICE_URL" \
    --project=$PROJECT_ID

# Step 2.3: Get Service URL
export ALPHABOT_SERVICE_URL=$(gcloud run services describe $ALPHABOT_SERVICE_NAME --platform managed --region $REGION --format 'value(status.url)' --project=$PROJECT_ID)
echo "AlphaBot URL: $ALPHABOT_SERVICE_URL"
echo "---"

# --- 3. Deploy Simulator ---
echo "Deploying Simulator..."

# Step 3.1: Build and Push Image using Cloud Build Config
echo "Building Simulator image using $SIMULATOR_BUILDFILE..."
gcloud builds submit . --config=$SIMULATOR_BUILDFILE \
    --substitutions=_REGION=$REGION,_REPO_NAME=$REPOSITORY_NAME \
    --project=$PROJECT_ID --quiet

# Step 3.2: Deploy to Cloud Run (passing AlphaBot URL)
echo "Deploying Simulator service ($SIMULATOR_SERVICE_NAME)..."
gcloud run deploy $SIMULATOR_SERVICE_NAME \
    --image=$SIMULATOR_IMAGE_TAG \
    --platform managed \
     --region $REGION \
     --allow-unauthenticated \
     --set-env-vars="ALPHABOT_SERVICE_URL=$ALPHABOT_SERVICE_URL,RISKGUARD_SERVICE_URL=$RISKGUARD_SERVICE_URL" \
     --project=$PROJECT_ID
 
 # Step 3.3: Get Service URL
export SIMULATOR_SERVICE_URL=$(gcloud run services describe $SIMULATOR_SERVICE_NAME --platform managed --region $REGION --format 'value(status.url)' --project=$PROJECT_ID)
echo "Simulator UI URL: $SIMULATOR_SERVICE_URL"
echo "---"

echo "Deployment Complete!"
echo "Access the Simulator UI at: $SIMULATOR_SERVICE_URL"
echo "Remember to consider security (--allow-unauthenticated) for production environments."
