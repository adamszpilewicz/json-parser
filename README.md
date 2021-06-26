# CLI json parser

## Usage
### exemplary json to parse
```json
[
    {
      "country": "US",
      "city": "Boston",
      "currency": "USD",
      "amount": 100
    },
    {
      "country": "FR",
      "city": "Paris",
      "currency": "EUR",
      "amount": 20
    },
    {
      "country": "FR",
      "city": "Lyon",
      "currency": "EUR",
      "amount": 11.4
    },
    {
      "country": "ES",
      "city": "Madrid",
      "currency": "EUR",
      "amount": 8.9
    },
    {
      "country": "UK",
      "city": "London",
      "currency": "GBP",
      "amount": 12.2
    },
    {
      "country": "UK",
      "city": "London",
      "currency": "FBP",
      "amount": 10.9
    }
  ]
```

### command to parse
- note that command line arguments are specified after main.py
- arguments must EXACTLY match keys from json to parse
```bash
cat ./data/data_json.json | python3 main.py currency country 
```

### output after parse based on arguments `currency` and `country`
```bash
[{'USD': {'US': [100]}}, {'EUR': {'FR': [20]}}, {'EUR': {'FR': [11.4]}}, {'EUR': {'ES': [8.9]}}, {'GBP': {'UK': [12.2]}}, {'FBP': {'UK': [10.9]}}]
```


