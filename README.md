# Stock Trading Python Application

A Python application that fetches stock ticker data from the Polygon.io API and exports it to CSV format. The application includes both manual execution and scheduled automation capabilities.

## Features

- **Stock Data Fetching**: Retrieves comprehensive stock ticker information from Polygon.io API
- **CSV Export**: Exports ticker data to CSV format with consistent schema
- **Scheduled Execution**: Automated data collection using the `schedule` library
- **Pagination Support**: Handles large datasets by fetching multiple pages of data
- **Environment Configuration**: Secure API key management using environment variables

## Project Structure

```
Stock_trading_python_app/
├── script.py          # Main data fetching and CSV export logic
├── scheduler.py       # Automated scheduling functionality
├── requirements.txt   # Python dependencies
├── .env              # Environment variables (create this file)
├── tickers.csv       # Generated CSV output file
└── README.md         # This file
```

## Prerequisites

- Python 3.7 or higher
- Polygon.io API key (free tier available at [polygon.io](https://polygon.io))

## Installation

1. **Clone or download the project**
   ```bash
   cd Stock_trading_python_app
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv pythonenv
   source pythonenv/bin/activate  # On Windows: pythonenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```bash
   touch .env
   ```
   
   Add your Polygon.io API key to the `.env` file:
   ```
   POLYGON_API_KEY=your_api_key_here
   ```

## Usage

### Manual Execution

Run the script directly to fetch and export stock data:

```bash
python script.py
```

This will:
- Fetch stock ticker data from Polygon.io API
- Process all available pages of data
- Export the data to `tickers.csv` with the following schema:

| Field | Description |
|-------|-------------|
| ticker | Stock symbol (e.g., 'AAPL') |
| name | Company name |
| market | Market type (e.g., 'stocks') |
| locale | Geographic region (e.g., 'us') |
| primary_exchange | Primary exchange (e.g., 'XNAS') |
| type | Security type (e.g., 'CS') |
| active | Whether the ticker is active |
| currency_name | Currency (e.g., 'usd') |
| cik | Central Index Key |
| composite_figi | Composite FIGI identifier |
| share_class_figi | Share class FIGI identifier |
| last_updated_utc | Last update timestamp |

### Automated Scheduling

Run the scheduler for automated data collection:

```bash
python scheduler.py
```

The scheduler is configured to:
- Run the stock job every minute
- Execute a basic job every minute and daily at 9:00 AM
- Run continuously until stopped

**Note**: Be mindful of API rate limits when using automated scheduling.

## Configuration

### API Limits
- The script fetches up to 1,000 records per API call
- There's a commented limit of 5,000 total records per execution
- Adjust `LIMIT` and `LIMIT_READ_PER_MINUTE` variables in `script.py` as needed

### Scheduling
Modify `scheduler.py` to change execution frequency:
```python
# Examples:
schedule.every().hour.do(run_stock_job)
schedule.every().day.at("09:30").do(run_stock_job)
schedule.every().monday.do(run_stock_job)
```

## Dependencies

- **requests**: HTTP library for API calls
- **python-dotenv**: Environment variable management
- **schedule**: Job scheduling library
- **csv**: Built-in CSV handling (no installation required)
- **datetime**: Built-in date/time handling (no installation required)

## API Information

This application uses the [Polygon.io Tickers API](https://polygon.io/docs/stocks/get_v3_reference_tickers):
- **Endpoint**: `https://api.polygon.io/v3/reference/tickers`
- **Rate Limits**: Varies by subscription tier
- **Documentation**: [Polygon.io API Docs](https://polygon.io/docs)

## Output

The application generates a `tickers.csv` file containing:
- All active US stock tickers
- Complete company information
- Standardized schema for easy data analysis
- UTF-8 encoding for international character support

## Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure your `.env` file contains a valid `POLYGON_API_KEY`
   - Verify the API key is active on your Polygon.io account

2. **Rate Limiting**
   - Reduce the frequency of scheduled runs
   - Implement delays between API calls if needed

3. **Missing Data**
   - Some tickers may have missing fields; the script handles this gracefully
   - Check your internet connection and API status

4. **File Permissions**
   - Ensure write permissions in the project directory for CSV output

### Debug Mode

Uncomment debug print statements in `script.py`:
```python
#print(data.keys())
#print(data['next_url'])
#print(len(tickers))
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for educational purposes. Please ensure compliance with Polygon.io's terms of service and any applicable data usage policies.

## Support

For issues related to:
- **Polygon.io API**: Check their [documentation](https://polygon.io/docs) and [support](https://polygon.io/support)
- **This application**: Create an issue in the project repository

---

**Note**: This application is designed for educational and personal use. Always review API terms of service and implement appropriate rate limiting for production use.