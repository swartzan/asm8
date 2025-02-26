import random
import time

locations = [
    {"Item_name": "Groceries", "price": 60 },
    {"Item_name": "Entertainment", "price": 20 },
    {"Item_name": "Dates", "price": 30 },
    {"Item_name": "Rent", "price": 400 }
]

def save_to_txt(expenses):
    f = open('./example.txt', 'r+')
    for item in expenses: 
        f.write(str(item["price"]))
        f.write("\n")

while True:
    total_budget = 0
    for item in locations:
        item["price"] = random.randint(10,1000)
        total_budget = total_budget + item["price"]    
    save_to_txt(locations)
    print("items saved to the txt file")
    time.sleep(5) #refreshes every 10 sec