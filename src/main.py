import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rich.console import Console
from rich.panel import Panel
from loguru import logger
import time

from src.auth import SchwabAuth
from src.trading.stocks import StockTrader
from src.trading.options import OptionsTrader
from src.algorithms.base import TradingAlgorithm

# ASCII Art for Schwab Trader
ASCII_ART = """
__          __    _                                 
\ \        / /   | |              
\ \  /\  / /___ | |  ___  ___   _ __ ___    __                      
\ \/  \/ // _ \| | / __|/ _ \ | '_ ` _ \  / _ \                   
    \  /\  /|  __/| || (__| (_) || | | | | ||                    
__\/_ \/  \___||_| \___|\___/ |_| |_| |_| \___|                                                                                        
    """

def setup_logging():
    """Configure logging"""
    logger.remove()  # Remove default handler
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="INFO"
    )
    logger.add("schwab_trader.log", rotation="500 MB")

def main():
    """Main entry point"""
    console = Console()
    
    # Display ASCII art
    console.print(Panel(ASCII_ART, title="Schwab Trader", border_style="blue"))
    
    # Setup logging
    setup_logging()
    logger.info("Starting Schwab Trader...")
    
    # Initialize authentication
    auth = SchwabAuth()
    if not auth.authenticate():
        logger.error("Failed to authenticate with Schwab API")
        return
        
    # Initialize traders
    stock_trader = StockTrader(auth)
    options_trader = OptionsTrader(auth)
    
    # TODO: Initialize and run trading algorithm
    logger.info("Trading algorithm to be implemented")
    
    # Keep the program running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Shutting down Schwab Trader...")

if __name__ == "__main__":
    main() 