import re

with open('target/release/librustdesk.dll', 'rb') as f:
    data = f.read()

if b'UnivecsSoporte' in data:
    count = data.count(b'UnivecsSoporte')
    print(f'OK: UnivecsSoporte ENCONTRADO ({count} ocurrencias)')
else:
    print('MAL: UnivecsSoporte NO encontrado')

print()
matches = set(re.findall(rb'Univecs[A-Za-z ]{2,30}', data))
print(f'Strings que empiezan por Univecs ({len(matches)} unicos):')
for m in sorted(matches)[:20]:
    try:
        s = m.decode('ascii')
        print(f'  {s!r}')
    except:
        pass