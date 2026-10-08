# bad_code.py
import time
import requests

# ТУТ ВСЁ В КУЧЕ: НАСТРОЙКИ, ЛОГИКА, И СЕКРЕТНЫЕ ТОКЕНЫ ПРЯМО В КОДЕ
TOKEN = "5938201948:AAFlk3910dkasKDJW1039"
CHAT_ID = "12345678"
FILE_NAME = "database.txt"

def run_everything():
    print("Запуск системы...")
    
    # 1. Запрос к банку (Синхронный!)
    # Что будет, если сайт банка упадет или будет долго отвечать?
    response = requests.get("https://fake-bank-api.com")
    data = response.json()
    
    # Жесткая завязка на структуру ответа, без валидации
    # А если банк изменит название ключа с 'price' на 'value'?
    rate = data["price"] 
    
    print(f"Курс получен: {rate}")
    
    # 2. Сохранение в файл (Вместо нормальной базы данных)
    # Что будет, если два процесса одновременно захотят записать данные?
    f = open(FILE_NAME, "a")
    f.write(f"{time.time()}:{rate}\n")
    f.close()
    
    # 3. Отправка в Telegram (Опять синхронно)
    # Если Telegram затупит, вся программа зависнет
    tele_url = f"https://telegram.org{TOKEN}/sendMessage"
    requests.post(tele_url, json={"chat_id": CHAT_ID, "text": f"Курс USD: {rate}"})
    
    print("Все сделано! Спим минуту...")
    time.sleep(60) # Полная заморозка всего потока

if __name__ == "__main__":
    while True:
        run_everything()

