import re
import os

# Текст ошибки
errors_text = """Цена McBus вне допустимого диапазона. Минимальная цена: 10101,780774176055. Максимальная цена: 12506,966782016265. Оценка: 9620,744031360839. Минимальная наценка: 4,999995%. Текущая цена: 50000.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (10101,780774176055,12506,966782016265)
  But was:  50000

  2)   Цена Legionnaire-DRV вне допустимого диапазона. Минимальная цена: 120629,97868836764. Максимальная цена: 149351,4034899259. Оценка: 114885,69920623302. Минимальная наценка: 4,999995%. Текущая цена: 470200.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (120629,97868836764,149351,4034899259)
  But was:  470200

  3)   Цена Piecrust вне допустимого диапазона. Минимальная цена: 28708,84477978507. Максимальная цена: 35544,28432348547. Оценка: 27341,758174801616. Минимальная наценка: 4,999995%. Текущая цена: 28708.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (28708,84477978507,35544,28432348547)
  But was:  28708

  4)   Цена Copperhead вне допустимого диапазона. Минимальная цена: 23065,687369263076. Максимальная цена: 28557,51794467894. Оценка: 21967,32230166346. Минимальная наценка: 4,999995%. Текущая цена: 23065.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (23065,687369263076,28557,51794467894)
  But was:  23065

  5)   Цена GFSeagull вне допустимого диапазона. Минимальная цена: 60814,15095486156. Максимальная цена: 75293,71136358025. Оценка: 57918,241634874794. Минимальная наценка: 4,999995%. Текущая цена: 60814.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (60814,15095486156,75293,71136358025)
  But was:  60814

  6)   Цена Lyrae вне допустимого диапазона. Минимальная цена: 59696,526563277585. Максимальная цена: 73909,98591429659. Оценка: 56853,83740407601. Минимальная наценка: 4,999995%. Текущая цена: 59507.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (59696,526563277585,73909,98591429659)
  But was:  59507

  7)   Цена Baron вне допустимого диапазона. Минимальная цена: 267103,8235659458. Максимальная цена: 330699,9749221241. Оценка: 254384,60542471334. Минимальная наценка: 4,999995%. Текущая цена: 267093.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (267103,8235659458,330699,9749221241)
  But was:  267093

  8)   Цена Aeon вне допустимого диапазона. Минимальная цена: 42638,75307237176. Максимальная цена: 52790,83759825942. Оценка: 40608,338103550675. Минимальная наценка: 4,999995%. Текущая цена: 42405.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (42638,75307237176,52790,83759825942)
  But was:  42405

  9)   Цена Turncoat вне допустимого диапазона. Минимальная цена: 39961,94191670446. Максимальная цена: 49476,69042420416. Оценка: 38058,99402999878. Минимальная наценка: 4,999995%. Текущая цена: 39930.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (39961,94191670446,49476,69042420416)
  But was:  39930

  10)   Цена Disciple вне допустимого диапазона. Минимальная цена: 8427,299629306792. Максимальная цена: 10433,799632167815. Оценка: 8026,000011444092. Минимальная наценка: 4,999995%. Текущая цена: 8365.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (8427,299629306792,10433,799632167815)
  But was:  8365

  11)   Цена Nugget вне допустимого диапазона. Минимальная цена: 12060,824456286431. Максимальная цена: 14932,449457240105. Оценка: 11486,500003814697. Минимальная наценка: 4,999995%. Текущая цена: 12060.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (12060,824456286431,14932,449457240105)
  But was:  12060

  12)   Цена EagleMercenary вне допустимого диапазона. Минимальная цена: 89686,13314737778. Максимальная цена: 111039,97534268729. Оценка: 85415,36878123805. Минимальная наценка: 4,999995%. Текущая цена: 59715.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (89686,13314737778,111039,97534268729)
  But was:  59715

  13)   Цена Menace вне допустимого диапазона. Минимальная цена: 18811,00539325504. Максимальная цена: 23289,816404569432. Оценка: 17915,24404525757. Минимальная наценка: 4,999995%. Текущая цена: 18795.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (18811,00539325504,23289,816404569432)
  But was:  18795

  14)   Цена Spectre вне допустимого диапазона. Минимальная цена: 100493,56321864837. Максимальная цена: 124420,60316683148. Оценка: 95708,15979273245. Минимальная наценка: 4,999995%. Текущая цена: 100315.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (100493,56321864837,124420,60316683148)
  But was:  100315

  15)   Цена Caretaker вне допустимого диапазона. Минимальная цена: 44945,715978108325. Максимальная цена: 55647,07741125857. Оценка: 42805,44573260099. Минимальная наценка: 4,999995%. Текущая цена: 44940.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (44945,715978108325,55647,07741125857)
  But was:  44940

  16)   Цена Falcon вне допустимого диапазона. Минимальная цена: 32550,25476931362. Максимальная цена: 40300,315780628014. Оценка: 31000,24404525757. Минимальная наценка: 4,999995%. Текущая цена: 32550.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (32550,25476931362,40300,315780628014)
  But was:  32550

  17)   Цена Laqeramaline вне допустимого диапазона. Минимальная цена: 355598,8200656656. Максимальная цена: 440265,209640546. Оценка: 338665,55829952174. Минимальная наценка: 4,999995%. Текущая цена: 355598.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (355598,8200656656,440265,209640546)
  But was:  355598

  18)   Цена Europa вне допустимого диапазона. Минимальная цена: 259537,88591603562. Максимальная цена: 321332,62346423714. Оценка: 247178,95019280614. Минимальная наценка: 4,999995%. Текущая цена: 259537.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (259537,88591603562,321332,62346423714)
  But was:  259537

  19)   Цена GFIlmus вне допустимого диапазона. Минимальная цена: 60417,29989526779. Максимальная цена: 74802,37195217315. Оценка: 57540,288227621466. Минимальная наценка: 4,999995%. Текущая цена: 60383.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (60417,29989526779,74802,37195217315)
  But was:  60383

  20)   Цена Legionnaire-EMP вне допустимого диапазона. Минимальная цена: 129963,42826450709. Максимальная цена: 160907,10306606535. Оценка: 123774,69920623302. Минимальная наценка: 4,999995%. Текущая цена: 482350.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (129963,42826450709,160907,10306606535)
  But was:  482350

  21)   Цена Empress вне допустимого диапазона. Минимальная цена: 252537,67480670524. Максимальная цена: 312665,6953484231. Оценка: 240512,08216687143. Минимальная наценка: 4,999995%. Текущая цена: 252443.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (252537,67480670524,312665,6953484231)
  But was:  252443

  22)   Цена Courier вне допустимого диапазона. Минимальная цена: 27034,424697041417. Максимальная цена: 33471,19277436463. Оценка: 25747,072309292853. Минимальная наценка: 4,999995%. Текущая цена: 26888.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (27034,424697041417,33471,19277436463)
  But was:  26888

  23)   Цена Duran вне допустимого диапазона. Минимальная цена: 31437,133752405356. Максимальная цена: 38922,16593813439. Оценка: 29940,12874291614. Минимальная наценка: 4,999995%. Текущая цена: 31402.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (31437,133752405356,38922,16593813439)
  But was:  31402

  24)   Цена Cheetah вне допустимого диапазона. Минимальная цена: 9787,830787003324. Максимальная цена: 12118,266794503019. Оценка: 9321,74402999878. Минимальная наценка: 4,999995%. Текущая цена: 50000.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (9787,830787003324,12118,266794503019)
  But was:  50000

  25)   Цена Nook вне допустимого диапазона. Минимальная цена: 22819,626643752763. Максимальная цена: 28252,871329481797. Оценка: 21732,978742916137. Минимальная наценка: 4,999995%. Текущая цена: 22691.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (22819,626643752763,28252,871329481797)
  But was:  22691

  26)   Цена Akupara вне допустимого диапазона. Минимальная цена: 44410,97717674299. Максимальная цена: 54985,01984188146. Оценка: 42296,17066055388. Минимальная наценка: 4,999995%. Текущая цена: 44238.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (44410,97717674299,54985,01984188146)
  But was:  44238

  27)   Цена Phoenix вне допустимого диапазона. Минимальная цена: 64267,101735784454. Максимальная цена: 79568,79332015362. Оценка: 61206,76633747667. Минимальная наценка: 4,999995%. Текущая цена: 64267.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (64267,101735784454,79568,79332015362)
  But was:  64267

  28)   Цена Alleycat вне допустимого диапазона. Минимальная цена: 8413,387121927739. Максимальная цена: 10416,574622881413. Оценка: 8012,750003814697. Минимальная наценка: 4,999995%. Текущая цена: 50000.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (8413,387121927739,10416,574622881413)
  But was:  50000

  29)   Цена Wyvern вне допустимого диапазона. Минимальная цена: 484288,54064621805. Максимальная цена: 599595,3412746097. Оценка: 461227,2025135666. Минимальная наценка: 4,999995%. Текущая цена: 483821.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (484288,54064621805,599595,3412746097)
  But was:  483821

  30)   Цена Retort вне допустимого диапазона. Минимальная цена: 55848,64873443356. Максимальная цена: 69145,94665602686. Оценка: 53189,191686373204. Минимальная наценка: 4,999995%. Текущая цена: 55718.
Assert.That(vessel.Price, Is.InRange(allowedMinPrice, allowedMaxPrice))
  Expected: in range (55848,64873443356,69145,94665602686)
  But was:  55718
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