from abc import ABC, abstractmethod
from typing import List, Dict, Any
from loguru import logger

class TradingAlgorithm(ABC):
    """
    Base class for trading algorithms
    """
    
    def __init__(self):
        self.name = self.__class__.__name__
        logger.info(f"Initializing trading algorithm: {self.name}")
        
    @abstractmethod
    def analyze(self, market_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Analyze market data and generate trading signals
        
        Args:
            market_data: Dictionary containing market data (prices, volumes, etc.)
            
        Returns:
            List of trading signals, each containing:
            - ticker: Stock symbol
            - action: "BUY" or "SELL"
            - quantity: Number of shares
            - limit_price: Optional limit price
            - reason: Explanation for the trade
        """
        pass
        
    @abstractmethod
    def update(self, market_data: Dict[str, Any]) -> None:
        """
        Update algorithm state with new market data
        
        Args:
            market_data: Dictionary containing market data
        """
        pass 