import logging

logging.basicConfig(filename="app.log",level=logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s')

def process_data(data):
    logging.info(f"Processing {data}")
    return data.upper()

name = input("Enter Name: ")
result = process_data(name)
print(result)
