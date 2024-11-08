import os
from typing import Any

from dotenv import load_dotenv

load_dotenv()
AppConfigDict = dict[str, Any]

def get_app_config()->AppConfigDict :
    app_config = {
        "azure_open_api" : {
            "name" : "openai",
            "api_key" : os.getenv("AZURE_OPENAI_API_KEY"),
            "endpoint" : os.getenv("AZURE_OPENAI_ENDPOINT")
        },
        "gemini" : {
            "name" : "gemini",
            "api_key" : os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        },
        "database" : {
            "url" : os.getenv("DB_URL")
        }
    }
    return app_config