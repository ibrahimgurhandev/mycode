import json
from datetime import date
import updateCryptoPrices
import pandas as pd
import streamlit as st
import unicodecsv as csv

def check_data():
    with open('latestprices.json', 'r') as currentData:
        data = json.load(currentData)
        last_update = data['status']["timestamp"].split("T")[0]

        if last_update != str(date.today()):
            print("crypto prices are not current, updating now.............")
            updateCryptoPrices.load_data()

        print('Data is upto date')
        organize_data(data)

def organize_data(data):
    data_list = []
    for token in data['data']:
        name = token['name']
        ticker = token['symbol']
        rank = token['cmc_rank']
        price = token['quote']['USD']['price']
        volume_24h = token['quote']['USD']['volume_24h']
        market_cap  = token['quote']['USD']['market_cap']
        data_list.append({'Name': name, 'ticker': ticker, 'Price': price, 'Rank': rank, 'Volume': volume_24h, 'Market Cap': market_cap})

    keys = data_list[0].keys()
    with open('data.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data_list)
    visualize_data()

def visualize_data():
    df = pd.read_csv("data.csv")

    st.title("Crypto Tracker!")  # add a title
    df.set_index('Rank', inplace=True)
    st.write(df)  # visualize my dataframe in the Streamlit app

def main():
    check_data()

if __name__ == '__main__':
    main()