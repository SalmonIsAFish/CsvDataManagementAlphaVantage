# CsvDataManagementAlphaVantage

This program is used to generate CSVs via Alpha Vantage API. 

## Use case
I am using this data to create CSVs to pass into https://github.com/SalmonIsAFish/TradingAlgorithmSimulator

## How to use
1) Create a "key.txt" file
2) Put your API key from Alpha Vantage in key.txt
3) Type in main 

``` 
generate_csv_range("STOCK_SYMBOL", [number_of_months_to_go_back])
```

STOCK_SYMBOL examples: XOM, WMT, CVX, COP, GM, GE, BRKA, FNMA, F, HW

number_of_months_to_go_back: [1-5] | With my free key it only allows 5 since only 5 api calls can be made per minute.

If you want to append [6-10] when you first must call with 5 first. Then call with 10.

Use ```generate_ten_months_with_free_key``` to generate multiple CSVs with data from the last 10 months with just their stock name.
This function includes a sleep timer that takes 2 minutes to comply with alpha vantage's free key usage


*Note: This program does not handle incorrect input. So double-check your stock symbols!*
