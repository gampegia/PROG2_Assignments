import json
json_string = '{"Lenkrad": 120, "Reifen": "g\\u00fcnstig", "Hutablage": null, "Fahrgestell": 3430, "Getriebe": -1200, "Radaufh\\u00c3\\u00a4ngung": 1900, "Z\\u00c3\\u00bcndanlage": 160}'
decoded_data = json.loads(json_string)

print("++++++++++++++++++++++++++++")
for item in list(decoded_data.keys()):
    corrected_key = item.encode('latin-1').decode('utf-8')
    if corrected_key != item:
        decoded_data.update({corrected_key:decoded_data[item]})
        decoded_data.pop(item)


print("new dictt")
print(decoded_data)
data = decoded_data
print("+++++++++++++++")
invalid_entries = []
for item in list(data.keys()):
    if not str(data[item]).isnumeric():
        data.pop(item)

print(data)
print("++++++++++++++++++++")
currency = "CHF"
item_width = max(len(str(item)) for item in data.keys())
price_width = max(len(str(item)) for item in data.values())


print("BOM fetched from: xyxyxyyxyx")
print("=".ljust(item_width + price_width +3,"="))
for item, price in data.items():
    print(f"|{str(item).ljust(item_width)}|{str(price).ljust(price_width)}|")
print("|"+"-".ljust(item_width, "-")+"|"+"-".ljust(price_width, "-")+"|")
print(f"|{str('Total Price').ljust(item_width)}|{str('CHF').ljust(price_width)}|")
print("=".ljust(item_width + price_width +3,"="))


print(sum(list(data.values())))