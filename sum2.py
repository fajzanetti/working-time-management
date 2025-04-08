from datetime import timedelta, datetime

# Função para converter o tempo em HH:MM:SS para timedelta
def converter_para_timedelta(tempo_str):
    try:
        horas, minutos, segundos = map(int, tempo_str.split(':'))
        return timedelta(hours=horas, minutes=minutos, seconds=segundos)
    except ValueError:
        print(f"Formato inválido para o tempo: {tempo_str}")
        return timedelta()

# Função para somar uma lista de tempos no formato HH:MM:SS
def somar_tempos(tempos):
    total_timedelta = timedelta()
    
    for tempo in tempos:
        total_timedelta += converter_para_timedelta(tempo)
    
    return total_timedelta

# Função para converter o resultado para horas decimais e dias
def exibir_resultados(total_timedelta):
    # Converter o total para horas decimais
    total_em_horas = total_timedelta.total_seconds() / 3600
    total_em_horas = round(total_em_horas, 2)
    
    # Exibir em dias, horas, minutos e segundos
    dias = total_timedelta.days
    horas, resto = divmod(total_timedelta.seconds, 3600)
    minutos, segundos = divmod(resto, 60)
    
    # Exibir os resultados
    print(f"Total em horas decimais: {total_em_horas:.2f} horas")
    print(f"Total em dias, horas, minutos e segundos: {dias} dias, {horas} horas, {minutos} minutos, {segundos} segundos")

# Lista de tempos no formato HH:MM:SS
tempos = [
"9:42:32",
"8:18:25",
]

# Somar os tempos
total_tempo = somar_tempos(tempos)

# Exibir os resultados
exibir_resultados(total_tempo)
