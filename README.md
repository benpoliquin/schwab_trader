# Schwab Trader

A Python-based trading service that interfaces with Charles Schwab's Individual Trader API to execute automated trades based on custom algorithms.

## Features

- Authentication with Charles Schwab API
- Stock trading capabilities (market and limit orders)
- Modular design for future options trading
- Customizable trading algorithms

## Prerequisites

- Python 3.8 or higher
- Charles Schwab API credentials (https://developer.schwab.com/products/trader-api--individual)
- Virtual environment (recommended)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd schwab_trader
```

2. Create and activate virtual environment:
```bash
make setup
source venv/bin/activate  # On Unix/macOS
# or
.\venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
make install
```

4. Configure your Schwab API credentials:
   - Create a `.env` file in the root directory
   - Add your Schwab API credentials and configuration:
     ```
     # Required Variables
     SCHWAB_API_KEY=your_api_key_here
     SCHWAB_API_SECRET=your_api_secret_here
     SCHWAB_API_BASE_URL=https://api.schwab.com/v1  # Replace with actual API endpoint

     # Optional Configuration
     SCHWAB_API_TIMEOUT=30  # API request timeout in seconds
     SCHWAB_API_RETRY_COUNT=3  # Number of retries for failed requests
     ```

   - For security, you can create a `.env.local` file with your actual credentials:
     ```bash
     cp .env .env.local
     ```
   - Edit `.env.local` with your actual credentials
   - Add `.env.local` to your `.gitignore` to prevent committing sensitive data

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `SCHWAB_API_KEY` | Yes | None | Your Schwab API key |
| `SCHWAB_API_SECRET` | Yes | None | Your Schwab API secret |
| `SCHWAB_API_BASE_URL` | No | https://api.schwab.com/v1 | Base URL for Schwab API |
| `SCHWAB_API_TIMEOUT` | No | 30 | API request timeout in seconds |
| `SCHWAB_API_RETRY_COUNT` | No | 3 | Number of retries for failed requests |

## Usage

Run the trading service:
```bash
make run
```

## Project Structure

```
schwab_trader/
├── src/
│   ├── main.py              # Main entry point
│   ├── auth.py              # Authentication module
│   ├── trading/
│   │   ├── stocks.py        # Stock trading functionality
│   │   └── options.py       # Future options trading module
│   └── algorithms/          # Trading algorithms
├── requirements.txt         # Python dependencies
├── Makefile                # Build and setup commands
├── .env                    # Environment variables template
├── .env.local             # Local environment variables (gitignored)
└── README.md              # This file
```

## API Documentation

This project uses the Charles Schwab Individual Trader API. For detailed documentation, visit:
https://developer.schwab.com/products/trader-api--individual

## License
None
