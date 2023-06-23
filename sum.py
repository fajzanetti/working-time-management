horas = [
    '2h',
    '1h 35min',
    '26min',
]

total_horas = 0
total_minutos = 0

for hora in horas:
    if hora == '0s':
        continue

    if 'h' in hora and 'min' in hora:
        h, m = hora.split('h')
        m = m.replace('min', '').strip()
        total_horas += int(h)
        total_minutos += int(m)
    elif 'h' in hora:
        h = hora.replace('h', '').strip()
        total_horas += int(h)
    elif 'min' in hora:
        m = hora.replace('min', '').strip()
        total_minutos += int(m)

# Ajusta minutos caso ultrapasse 60
total_horas += total_minutos // 60
total_minutos = total_minutos % 60

print(f'Total de horas: {total_horas} h {total_minutos} min')
