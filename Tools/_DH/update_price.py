import re
import os

# Текст ошибки
errors_text = """1)   Цена Gasbender вне допустимого диапазона. Минимальная цена: 81056,2119428901. Максимальная цена: 100355,3109009618. Оценка: 77196,39583228677. Минимальная наценка: 4,999995%. Текущая цена: 81056.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (81056,2119428901,100355,3109009618)
  But was:  81056

  2)   Цена McBus вне допустимого диапазона. Минимальная цена: 10044,11689925092. Максимальная цена: 12435,573412437836. Оценка: 9565,826052747667. Минимальная наценка: 4,999995%. Текущая цена: 50000.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (10044,11689925092,12435,573412437836)
  But was:  50000

  3)   Цена Bookworm вне допустимого диапазона. Минимальная цена: 29540,86476347982. Максимальная цена: 36574,40431229435. Оценка: 28134,15819525812. Минимальная наценка: 4,999995%. Текущая цена: 29461.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (29540,86476347982,36574,40431229435)
  But was:  29461

  4)   Цена Legionnaire-DRV вне допустимого диапазона. Минимальная цена: 120629,97868836764. Максимальная цена: 149351,4034899259. Оценка: 114885,69920623302. Минимальная наценка: 4,999995%. Текущая цена: 470200.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (120629,97868836764,149351,4034899259)
  But was:  470200

  5)   Цена Pearl вне допустимого диапазона. Минимальная цена: 90852,1684321953. Максимальная цена: 112483,63808887881. Оценка: 86525,87862673402. Минимальная наценка: 4,999995%. Текущая цена: 90820.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (90852,1684321953,112483,63808887881)
  But was:  90820

  6)   Цена Ayhiva вне допустимого диапазона. Минимальная цена: 150836,40870576055. Максимальная цена: 186749,8409809282. Оценка: 143653,7291006706. Минимальная наценка: 4,999995%. Текущая цена: 150769.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (150836,40870576055,186749,8409809282)
  But was:  150769

  7)   Цена Bulker вне допустимого диапазона. Минимальная цена: 42760,037965323965. Максимальная цена: 52940,999847987856. Оценка: 40723,84753065556. Минимальная наценка: 4,999995%. Текущая цена: 42755.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (42760,037965323965,52940,999847987856)
  But was:  42755

  8)   Цена Twilight вне допустимого диапазона. Минимальная цена: 35002,52553538094. Максимальная цена: 43336,46056513163. Оценка: 33335,74011900276. Минимальная наценка: 4,999995%. Текущая цена: 35002.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (35002,52553538094,43336,46056513163)
  But was:  35002

  9)   Цена Vetcher19 вне допустимого диапазона. Минимальная цена: 23471,070051264825. Максимальная цена: 29059,420317254837. Оценка: 22353,401063960046. Минимальная наценка: 4,999995%. Текущая цена: 23429.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (23471,070051264825,29059,420317254837)
  But was:  23429

  10)   Цена Argent вне допустимого диапазона. Минимальная цена: 54215,566204459785. Максимальная цена: 67124,03493459188. Оценка: 51633,87492052838. Минимальная наценка: 4,999995%. Текущая цена: 54058.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (54215,566204459785,67124,03493459188)
  But was:  54058

  11)   Цена Broadhead вне допустимого диапазона. Минимальная цена: 58020,89062128359. Максимальная цена: 71835,38901561455. Оценка: 55257,993577323854. Минимальная наценка: 4,999995%. Текущая цена: 57788.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (58020,89062128359,71835,38901561455)
  But was:  57788

  12)   Цена Brigand вне допустимого диапазона. Минимальная цена: 51888,02598826958. Максимальная цена: 64242,31845128479. Оценка: 49417,169852060826. Минимальная наценка: 4,999995%. Текущая цена: 51840.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (51888,02598826958,64242,31845128479)
  But was:  51840

  13)   Цена McCargo вне допустимого диапазона. Минимальная цена: 60478,95584933031. Максимальная цена: 74878,70789596485. Оценка: 57599,00818653814. Минимальная наценка: 4,999995%. Текущая цена: 60478.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (60478,95584933031,74878,70789596485)
  But was:  60478

  14)   Цена Baroness вне допустимого диапазона. Минимальная цена: 26216,58071404391. Максимальная цена: 32458,624024667526. Оценка: 24968,173242494464. Минимальная наценка: 4,999995%. Текущая цена: 267753.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (26216,58071404391,32458,624024667526)
  But was:  267753

  15)   Цена Legionnaire-EMP вне допустимого диапазона. Минимальная цена: 129963,42826450709. Максимальная цена: 160907,10306606535. Оценка: 123774,69920623302. Минимальная наценка: 4,999995%. Текущая цена: 482350.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (129963,42826450709,160907,10306606535)
  But was:  482350

  16)   Цена Cheetah вне допустимого диапазона. Минимальная цена: 9787,830787003324. Максимальная цена: 12118,266794503019. Оценка: 9321,74402999878. Минимальная наценка: 4,999995%. Текущая цена: 50000.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (9787,830787003324,12118,266794503019)
  But was:  50000

  17)   Цена Sprinter вне допустимого диапазона. Минимальная цена: 55237,889303622374. Максимальная цена: 68389,76830651386. Оценка: 52607,516011565924. Минимальная наценка: 4,999995%. Текущая цена: 55237.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (55237,889303622374,68389,76830651386)
  But was:  55237

  18)   Цена Solarsail вне допустимого диапазона. Минимальная цена: 20548,927640932892. Максимальная цена: 25441,529682390672. Оценка: 19570,40816583112. Минимальная наценка: 4,999995%. Текущая цена: 20548.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (20548,927640932892,25441,529682390672)
  But was:  20548

  19)   Цена Alleycat вне допустимого диапазона. Минимальная цена: 8413,387121927739. Максимальная цена: 10416,574622881413. Оценка: 8012,750003814697. Минимальная наценка: 4,999995%. Текущая цена: 50000.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (8413,387121927739,10416,574622881413)
  But was:  50000

  20)   Цена ShuttleTinia вне допустимого диапазона. Минимальная цена: 118403,05262404485. Максимальная цена: 146594,25691001874. Оценка: 112764,81714389558. Минимальная наценка: 4,999995%. Текущая цена: 117725.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (118403,05262404485,146594,25691001874)
  But was:  117725
"""
# Парсинг ошибок
pattern = r"Цена (\w+) вне допустимого диапазона\. Минимальная цена: ([\d.,]+)\."
matches = re.findall(pattern, errors_text)
price_map = {}
for name, val in matches:
    val = val.replace(',', '.')
    float_val = float(val)
    int_price = int(float_val) + 650
    price_map[name] = int_price

list_of_directory_ship = ["_DH", "_Lua", "_Mono", "_NF"]

# Директория с файлами, где надо изменить
for path in list_of_directory_ship:
    directory = f'Resources/Prototypes/{path}/Shipyard'

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