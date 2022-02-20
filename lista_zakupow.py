prod = {"piekarnia":['chleb', 'paczek', 'bulka'], "warzywniak":['marchew', 'seler', 'rukola']}

cap_prod = dict()
for k,v in prod.items():
    cap_prod[k.capitalize()] = list()
    for x in v:
        cap_prod[k.capitalize()].append(x.capitalize())
        
i = 0
for keys,values in cap_prod.items(): 
    i = i + len(values)
    print(f'Ide do {keys.capitalize()},kupuje tu nastepujace rzeczy: {cap_prod[keys]}')
print(f'W sumie kupuje {i} produktow.')



