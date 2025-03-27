import os
from typing import Optional
from dotenv import load_dotenv
from loguru import logger
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class SchwabAuth:
    """
    Authentication handler for Charles Schwab API
    Documentation: https://developer.schwab.com/products/trader-api--individual
    """
    
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Required environment variables
        self.api_key = os.getenv('SCHWAB_API_KEY')
        self.api_secret = os.getenv('SCHWAB_API_SECRET')
        self.base_url = os.getenv('SCHWAB_API_BASE_URL', 'https://api.schwab.com/v1')
        
        # Optional configuration with defaults
        self.timeout = int(os.getenv('SCHWAB_API_TIMEOUT', '30'))
        self.retry_count = int(os.getenv('SCHWAB_API_RETRY_COUNT', '3'))
        
        # Initialize session with retry strategy
        self.session = requests.Session()
        retry_strategy = Retry(
            total=self.retry_count,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retry_strategy))
        
        self.access_token: Optional[str] = None
        
        # Validate required environment variables
        if not self.api_key or not self.api_secret:
            logger.error("Missing required environment variables: SCHWAB_API_KEY or SCHWAB_API_SECRET")
            raise ValueError("Missing required environment variables")
        
    def authenticate(self) -> bool:
        """
        Authenticate with Schwab API
        Returns:
            bool: True if authentication successful, False otherwise
        """
        try:
            logger.info("Attempting to authenticate with Schwab API...")
            
            # Example authentication request (replace with actual implementation)
            response = self.session.post(
                f"{self.base_url}/auth",
                json={
                    "api_key": self.api_key,
                    "api_secret": self.api_secret
                },
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                self.access_token = response.json().get("access_token")
                logger.success("Successfully authenticated with Schwab API")
                return True
            else:
                logger.error(f"Authentication failed: {response.text}")
                return False
                
        except requests.exceptions.Timeout:
            logger.error("Authentication request timed out")
            return False
        except requests.exceptions.RequestException as e:
            logger.error(f"Authentication request failed: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error during authentication: {str(e)}")
            return False
            
    def get_headers(self) -> dict:
        """
        Get headers for API requests
        Returns:
            dict: Headers with authentication token
        """
        if not self.access_token:
            raise ValueError("Not authenticated. Call authenticate() first.")
            
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        } 