from __future__ import annotations

import os
from dotenv import load_dotenv




load_dotenv()


class DatabaseConfigs:
    

    # Add the configurations for the postgres database container
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_URL = os.getenv("POSTGRES_URL")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    