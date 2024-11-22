# metricsense-AI
Metricsense-AI is a FastAPI-based application designed to provide engineering metrics and summaries. It connects to a database to fetch and process data related to engineering issues and generates summaries using Azure OpenAI services.  
## Features
 - Fetch engineering issues from the database.
 - Generate summaries for critical defects identified.
 - Health check endpoint to verify application status.

## Installation
 - Clone the repository:
   git clone https://github.com/yourusername/metricsense-AI.git <br> 
   cd metricsense-AI
## Create and activate a virtual environment:
 - python -m venv venv <br> 
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
## Install the dependencies:
 - pip install -r requirements.txt
## Configure the application
 - Create .env file similar to .sample-env and cope values over. Update with your database URL and Azure OpenAI configuration

## Usage
Start the FastAPI application:
 - uvicorn src.main:app --reload
## Endpoints
 - Health Check: GET /v1/engineering/healthcheck
 - Engineering Summary: GET /v1/engineering/engineeringSummary
## Example
To get an engineering summary for all projects and priorities for the month of April 2024, use the following curl command:
```
curl --location 'http://127.0.0.1:8000/v1/engineering/engineeringSummary?type=defects&project=All&priority=All&month=2024-04'
```
