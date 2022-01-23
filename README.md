# data-scraper

## Additional dependencies
- requests 2.27.1
- mysql-connector 2.2.9

## config.json example
```json
{
    "database": {
        "host": "localhost",
        "database": "marketwatcher",
        "user": "root",
        "password": ""
    },

    "interval": {
        "fetchPosts": 60,
        "updatePriceData": 20,
        "fetchPriceData": 600,
        "fetchFearAndGreedIndex": 1800
    }
}
```
