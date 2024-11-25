import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as f_csv:
        f_csv_record = csv.DictReader(f_csv) #Записывание данных из CSV для парсинга
        data = [row for row in f_csv_record] #В data отправляем содержание столбцов, полученных из f_csv_record
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as f_json: #Здесь ошибка, но не понимаю какая. Идея реешния похожа на верную 
        json.dump(data, f_json, indent=4) #Запись в формат JSON'а

if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME) as output_file:
        for line in output_file:
            print(line, end="")