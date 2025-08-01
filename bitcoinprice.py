import requests
import os
import psycopg2
from datetime import datetime

def run_fetch_job():
    # PostgreSQL connection info
    # DB_HOST = 'localhost'  # or 'localhost' if not using Docker
    # DB_NAME = 'postgres'
    # DB_USER = 'postgres'
    # DB_PASS = 'postgres'
    # DB_PORT = '5432'
    # db_url = os.environ.get("DATABASE_URL")

    DB_HOST = "dpg-d22ekuvgi27c73eso4d0-a.oregon-postgres.render.com"
    DB_NAME = "bitcoinprice_q1kp"
    DB_USER = "bitcoinprice_q1kp_user"
    DB_PASS = "pVfh5ZkxguTrPeoxqIDUIhXMQXmNwTwo"
    DB_PORT = "5432"


    def fetch_bitcoin_price():
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        return data['bitcoin']['usd']
    def store_bitcoin_price(price):
        try:
            connection = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS,
                port=DB_PORT
            )
            # connection = psycopg2.connect(dsn=db_url) # Use DATABASE_URL for Render call API online
            cursor = connection.cursor()
            cursor.execute("INSERT INTO bitcoin_price (price_usd, timestamp) VALUES (%s, %s)", (price, datetime.now()))
            connection.commit()
        except Exception as e:
            print(f"Error storing Bitcoin price: {e}")
        finally:
            if connection:
                cursor.close()
                connection.close()
    if __name__ == "__main__":
        try:
            price = fetch_bitcoin_price()
            print(f"Current Bitcoin price: ${price}")
            store_bitcoin_price(price)
        except Exception as e:
            print(f"An error occurred: {e}")

    with open(r"C:\Users\admin\Desktop\Bitcoin PRice\log.txt", "a") as f:
        f.write(f"Script ran at: {datetime.now()}\n")
