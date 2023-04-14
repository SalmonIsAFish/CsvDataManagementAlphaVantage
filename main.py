import csv
import requests
import time


def get_key(f_name):
    f = open(f_name, "r")
    return f.read()


def generate_url(symbol, month_num):
    interval = "15min"
    time_slice = "year1month" + str(month_num)
    adjusted = "true"

    api_key = get_key("key.txt")

    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=" + symbol + "&interval=" + \
          interval + "&slice=" + time_slice + "&adjusted=" + adjusted + "&apikey=" + api_key
    return url


def generate_csv(stock_name, month_num):
    url = generate_url(stock_name, month_num)

    with requests.Session() as s, open("StockData/" + stock_name + ".csv", "a", newline='') as file:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        reader = csv.reader(decoded_content.splitlines(), delimiter=',')
        writer = csv.writer(file)
        next(reader)
        for row in reader:
            writer.writerow(row)


# Since the Alpha Vantage API allows me to only make a certain number of API calls per minute and per month,
# I have this method to extract as much data as I can from one API call
# For reference, with my free key, I get 5 API calls per minute.
def generate_csv_range(stock_name, number_of_months):

    if number_of_months == 5 or number_of_months == 10:
        for month_num in range(number_of_months - 4, number_of_months + 1):
            generate_csv(stock_name, month_num)
    else:
        for month_num in range(1, number_of_months + 1):
            generate_csv(stock_name, month_num)


# Takes 2:10 seconds to run.
# 60 seconds inbetween calls from Alpha Vantage and additional 5 seconds for a safety net
# I could Include a check to see if it's the last call to this function to make it finish running 1 minute faster
# but I may want to immediately run the code again for more stocks. The 65 seconds at the end is good for my use case
def generate_ten_months_with_free_key(stock_name):
    print("\nRunning 1-5 for stock: " + stock_name)
    generate_csv_range(stock_name, 5)
    time.sleep(65)
    print("\nRunning 6-10 for stock: " + stock_name)
    generate_csv_range(stock_name, 10)
    time.sleep(65)
    print("\nDone with stock: " + stock_name)


if __name__ == '__main__':
    generate_ten_months_with_free_key("BRK-A")
    generate_ten_months_with_free_key("HPQ")
    generate_ten_months_with_free_key("FNMA")
