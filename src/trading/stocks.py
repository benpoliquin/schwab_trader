from typing import Optional
from loguru import logger
import requests
from ..auth import SchwabAuth

class StockTrader:
    """
    Stock trading functionality for Schwab API
    Documentation: https://developer.schwab.com/products/trader-api--individual
    """
    
    def __init__(self, auth: SchwabAuth):
        self.auth = auth
        self.base_url = "https://api.schwab.com/v1"  # Replace with actual API endpoint
        
    def get_stock_price(self, ticker: str) -> Optional[float]:
        """
        Get current stock price
        Documentation: https://developer.schwab.com/products/trader-api--individual
        """
        try:
            response = requests.get(
                f"{self.base_url}/stocks/{ticker}/price",
                headers=self.auth.get_headers()
            )
            if response.status_code == 200:
                return response.json().get("price")
            logger.error(f"Failed to get price for {ticker}: {response.text}")
            return None
        except Exception as e:
            logger.error(f"Error getting stock price: {str(e)}")
            return None
            
    def buy_stock(self, ticker: str, quantity: int, limit_price: Optional[float] = None) -> bool:
        """
        Buy stock with market or limit order
        Documentation: https://developer.schwab.com/products/trader-api--individual
        """
        try:
            order_type = "LIMIT" if limit_price else "MARKET"
            payload = {
                "ticker": ticker,
                "quantity": quantity,
                "order_type": order_type,
                "side": "BUY"
            }
            
            if limit_price:
                payload["limit_price"] = limit_price
                
            response = requests.post(
                f"{self.base_url}/orders",
                headers=self.auth.get_headers(),
                json=payload
            )
            
            if response.status_code == 200:
                logger.success(f"Successfully placed buy order for {quantity} shares of {ticker}")
                return True
            else:
                logger.error(f"Failed to place buy order: {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"Error placing buy order: {str(e)}")
            return False
            
    def sell_stock(self, ticker: str, quantity: int, limit_price: Optional[float] = None) -> bool:
        """
        Sell stock with market or limit order
        Documentation: https://developer.schwab.com/products/trader-api--individual
        """
        try:
            order_type = "LIMIT" if limit_price else "MARKET"
            payload = {
                "ticker": ticker,
                "quantity": quantity,
                "order_type": order_type,
                "side": "SELL"
            }
            
            if limit_price:
                payload["limit_price"] = limit_price
                
            response = requests.post(
                f"{self.base_url}/orders",
                headers=self.auth.get_headers(),
                json=payload
            )
            
            if response.status_code == 200:
                logger.success(f"Successfully placed sell order for {quantity} shares of {ticker}")
                return True
            else:
                logger.error(f"Failed to place sell order: {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"Error placing sell order: {str(e)}")
            return False 