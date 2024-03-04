

balance = 10
a = 10
currency_dict = {
        "CHF": ["Fr.","Rp."],
        "EUR": ["€", "Cent"],
        "USD": ["$", "¢"]
    }

print(currency_dict["CHF"][0])


a = 100.12
b = str(a).split(".")[0]
print(str(a).split(".")[0])
print(b)
print(a - float(b))
c,n = divmod(a,1)
print(c)
m = round(n,3)
print(m)


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

print(is_float(3))

