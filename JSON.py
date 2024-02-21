import json

# Чтение данных из файла JSON
with open('sample-data.json') as f:
    data = json.load(f)

# Вывод заголовка
print("Interface Status")
print("=" * 80)
print("{:<50s}{:<20s}{:<8s}{:<6s}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Вывод данных для каждого интерфейса
for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes'].get('descr', '')
    speed = interface['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = interface['l1PhysIf']['attributes'].get('mtu', '')
    print("{:<50s}{:<20s}{:<8s}{:<6s}".format(dn, description, speed, mtu))
