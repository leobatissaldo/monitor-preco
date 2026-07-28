import requests
import json

url = "https://www.vans.com.br/_next/data/qTiN5HRsXG5jYRZ4heZ7w/tenis-knu-skool-black-true-white/p/1002002760001U.json?n1=tenis-knu-skool-black-true-white&sku=1002002760001U"

base_price = 600.00

def get_price():
    response = requests.get(url)   
    if response.status_code == 200: 
        data = response.json()     
        price = data["pageProps"]["product"]["price"]["value"]
        if price < base_price: 
            on_sale = True 
        else: 
            on_sale = False
        return {
            "current_price": price,
            "base_price": base_price,
            "on_sale": on_sale
            }

    else:
        raise Exception(f"Error: {response.status_code}")