#MQL5 Signals Scraper
#https://www.mql5.com/en/signals/mt4/list

import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape data from a single page
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    signals = soup.find_all('div', class_='row signal')
    data = []
    for signal in signals:
        signal_num = signal.find('div', class_='col-num').text
        signal_chart = signal.find('div', class_='signal-chart').find('a')['href']
        signal_title = signal.find('span', class_='name').text
        price_value = signal.find('span', class_='price-value').text
        growth = signal.find('div', class_='col-growth').text
        subscribers = signal.find('div', class_='col-subscribers').text
        facilities = signal.find('div', class_='col-facilities').text.strip()
        balance = signal.find('div', class_='col-balance').text.strip()
        weeks = signal.find('div', class_='col-weeks').text
        experts = signal.find('div', class_='col-experts').text
        trades = signal.find('div', class_='col-trades').text
        plus = signal.find('div', class_='col-plus').text
        activity = signal.find('div', class_='col-activity').text
        pf = signal.find('div', class_='col-pf').text
        ep = signal.find('div', class_='col-ep').text.strip()
        drawdown = signal.find('div', class_='col-drawdown').text
        leverage = signal.find('div', class_='col-leverage').text
        row_data = [
            signal_num,
            signal_chart,
            signal_title,
            price_value,
            growth,
            subscribers,
            facilities,
            balance,
            weeks,
            experts,
            trades,
            plus,
            activity,
            pf,
            ep,
            drawdown,
            leverage
        ]
        data.append(row_data)
    return data

# Main function to scrape data from multiple pages and write to CSV
def main():
    base_url = "https://www.mql5.com/en/signals/mt4/list/page{}"
    total_pages = 10  # Change this to the total number of pages you want to scrape
    all_data = []
    for page_num in range(1, total_pages + 1):
        url = base_url.format(page_num)
        page_data = scrape_page(url)
        all_data.extend(page_data)
    csv_filename = 'data.csv'
    # Write the data to a CSV file
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(all_data)
    print(f'Data has been scraped and saved to {csv_filename}')

if __name__ == "__main__":
    main()