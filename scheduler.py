import schedule 
import time 
from modules.analysis import update_market_data

schedule.every(2).minutes.do(update_market_data)

print("Market tracker started...")

while True :
    schedule.run_pending()
    time.sleep(1)