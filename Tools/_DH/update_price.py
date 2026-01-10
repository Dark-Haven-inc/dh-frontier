import re
import os

# Текст ошибки
errors_text = """
"""
# Парсинг ошибок
pattern = r"Цена (\w+) вне допустимого диапазона\. Минимальная цена: ([\d.,]+)\."
matches = re.findall(pattern, errors_text)
price_map = {}
for name, val in matches:
    val = val.replace(',', '.')
    float_val = float(val)
    int_price = int(float_val)
    price_map[name] = int_price

# Директория с файлами, где надо изменить
directory = ''

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith(('.yml', '.yaml')):
            path = os.path.join(root, file)
            with open(path, 'r+', encoding='utf-8') as f:
                content = f.read()
                updated = False
                for name, price in price_map.items():
                    if f"id: {name}" in content:
                        content = re.sub(r"price:\s*\d+", f"price: {price}", content)
                        updated = True
                if updated:
                    f.seek(0)
                    f.write(content)
                    f.truncate()