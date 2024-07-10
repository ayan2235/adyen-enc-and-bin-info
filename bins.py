import csv

mydict = {}

def country_code_to_flag(country_code):
    return ''.join(chr(127397 + ord(char)) for char in country_code.upper())
    
with open('bins.csv', mode='r', encoding='utf-8') as inp:
    reader = csv.reader(inp)
    for x in reader:
        x2 = {
            "country": x[7],
            "iso": x[6],
            "flag": country_code_to_flag(x[5]),
            "vendor": x[1],
            "type": x[2],
            "level": x[3],
            "bank_name": x[4],
            "prepaid": True if x[3] == "PREPAID" else False
        }
        mydict[x[0]] = x2

def get_bin_info(bin):
    return mydict.get(bin, False)
