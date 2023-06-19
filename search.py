import os
import csv
import pandas as pd

from dotenv import load_dotenv
from datetime import datetime, time, timedelta
from dateutil.relativedelta import relativedelta

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

NOME_DIRETORIO_RAIZ = str(os.getenv('NOME_DIRETORIO_RAIZ'))
FIRST_WORKING_DAY_OF_THE_MONTH = int(os.getenv('FIRST_WORKING_DAY_OF_THE_MONTH'))
LAST_WORKING_DAY_OF_THE_MONTH = int(os.getenv('LAST_WORKING_DAY_OF_THE_MONTH'))
VALUE_PER_HOUR = float(os.getenv('VALUE_PER_HOUR'))

# Diretório do executavel
dir_path = os.path.dirname(os.path.realpath(__file__))

# obter a data atual
data_atual = datetime.today()
dia = data_atual.strftime("%d")
# dia = data_atual.day+1
ano = data_atual.year
# mes = data_atual.strftime('%B')
mes = data_atual.month
GLOBAL_HORA_ATUAL = datetime.now().strftime('%H:%M:%S')

# nome do diretório correspondente ao ano atual
nome_diretorio = f'{NOME_DIRETORIO_RAIZ}/{ano}'

# nome do arquivo csv correspondente a este mês
nome_arquivo = f'{nome_diretorio}/{mes}.csv'

# diretorios
diretorio_anos = f'{dir_path}/{NOME_DIRETORIO_RAIZ}'
diretorio_atual = f'{dir_path}/{nome_diretorio}'
diretorio_file = f'{dir_path}/{nome_diretorio}/{mes}.csv'

print('-----------------------------------------------\n')

print(f'{dir_path}/{nome_diretorio}')
print(f'{dir_path}/{nome_arquivo}\n')

print('-----------------------------------------------\n')

with open(nome_arquivo, 'r') as f:
    reader = csv.reader(f)
    linhas = list(reader)

def open_directory_in_file_manager(path):
    if os.name == 'posix': # Verifica se o sistema operacional é Unix-based (Linux, macOS, etc.)
        os.system(f'xdg-open {path}')
    elif os.name == 'nt': # Verifica se o sistema operacional é Windows
        os.system(f'explorer {path}')

def fetch_day(day):
    print(f'\nPasta: {nome_arquivo}')
    for i, row in enumerate(linhas):
        if row[0] == str(day):
            hora, minuto, segundo = row[-1].split(":")
            print(f'No dia {day}, teve um total de {hora} horas e {minuto} minutos\n')
            break
    else:
        print(f'Dia {day} não encontrado\n')

def horas_faltantes_8h():
    GLOBAL_HORA_ATUAL = datetime.now().strftime('%H:%M:%S')
    for i, row in enumerate(linhas):
        if row[0] == str(dia):
            if row[1] == '' and row[2] == '':
                print('\n-----------------------------------------------\n')
                print('Ainda abriu o PRIMEIRO ponto')
                return
            elif row[1] != '' and row[2] == '':
                print('\n-----------------------------------------------\n')
                print('Ainda NÃO fechou o PRIMEIRO ponto')
                inicio_str = row[1]
                total_str = '00:00:01'
                # return
            elif row[2] != '' and row[3] == '':
                inicio_str = GLOBAL_HORA_ATUAL
                total_str = row[-1]
                print('\n-----------------------------------------------\n')
                print('Ainda NÃO iniciou o SEGUNDO ponto')
                print(f'Mas se iniciar outro agora ás {GLOBAL_HORA_ATUAL}')
            elif row[3] != '' and row[4] == '':
                inicio_str = row[3]
                total_str = row[-1]
            elif row[4] != '' and row[5] == '':
                print('\n-----------------------------------------------\n')
                print('Ainda NÃO iniciou o TERCEIRO ponto')
                print(f'Mas se iniciar outro agora ás {GLOBAL_HORA_ATUAL}')
                inicio_str = GLOBAL_HORA_ATUAL
                total_str = row[-1]
            elif row[5] != '' and row[6] == '':
                inicio_str = row[5]
                total_str = row[-1]
            else:
                print('\n-----------------------------------------------\n')
                print('Ja bateu os três pontos')
                print(f'E trabalhou um total de {row[-1]} hoje')
                return
            break

    # Hora total no formato "HH:MM:SS"
    tempo_total_com_ponto = datetime.strptime(total_str, '%H:%M:%S').time()

    # Hora total no formato "HH:MM:SS"
    hora_atual = datetime.strptime(GLOBAL_HORA_ATUAL, '%H:%M:%S').time()

    # Hora de início no formato "HH:MM:SS"
    tempo_ultimo_ponto_entrada = datetime.strptime(inicio_str, '%H:%M:%S')

    # Duração de 8 horas em um objeto timedelta
    carga_dia_trabalho = timedelta(hours=8)

    # Subtrai o tempo total da duração de 8 horas
    tempo_restante_com_ponto = carga_dia_trabalho - timedelta(hours=tempo_total_com_ponto.hour, minutes=tempo_total_com_ponto.minute, seconds=tempo_total_com_ponto.second)
    
    # Soma o tempo restante com o intervalo entre a hora de início e a hora atual
    tempo_trabalhado_sem_ponto = timedelta(hours=tempo_total_com_ponto.hour, minutes=tempo_total_com_ponto.minute, seconds=tempo_total_com_ponto.second) + timedelta(hours=hora_atual.hour, minutes=hora_atual.minute, seconds=hora_atual.second) - timedelta(hours=tempo_ultimo_ponto_entrada.hour, minutes=tempo_ultimo_ponto_entrada.minute, seconds=tempo_ultimo_ponto_entrada.second)
    tempo_restante_sem_ponto = carga_dia_trabalho - tempo_trabalhado_sem_ponto

    # print('╭──┬──╮')
    # print('┝  │  │')
    # print('├──┼──┤')
    # print('╰──┴──╯')
    
    print()
    print(f'╭───┬───────────────────────────────────────────╮')
    # print('│    ╭─────╮                                                   │')
    # Formatando para "HH:MM:SS"
    # tempo_trabalhado_sem_ponto += datetime(1, 1, 1)
    # tempo_trabalhado_sem_ponto_formatado = tempo_trabalhado_sem_ponto.strftime('%H:%M:%S')

    # tempo_restante_sem_ponto_dt = datetime(1, 1, 1) + tempo_restante_sem_ponto
    # tempo_restante_sem_ponto_formatado = tempo_restante_sem_ponto_dt.strftime('%H:%M:%S')

    # tempo_restante_com_ponto_dt = datetime(1, 1, 1) + tempo_restante_com_ponto
    # tempo_restante_com_ponto_formatado = tempo_restante_com_ponto_dt.strftime('%H:%M:%S')

    # 🟢 🔴

    if tempo_restante_sem_ponto < timedelta(0):
        print(f'│ ╭─┴─╮                                         │')
        print(f'│ │ ✘ ├╼ Trabalhado SEM ponto : {str(tempo_trabalhado_sem_ponto).rjust(8)}  hrs   │')
        print(f'│ ╰─┬─╯                                         │')
        # print(f' ✘ - Trabalhado SEM ponto : {tempo_trabalhado_sem_ponto} hrs')
    else:
        print(f'│ ╭─┴─╮                                         │')
        print(f'│ │ ✘ ├╼ Trabalhado SEM ponto : {str(tempo_trabalhado_sem_ponto).rjust(8)}  hrs   │')
        print(f'│ │ ✘ ├╼ Restante   SEM ponto : {str(tempo_restante_sem_ponto).rjust(8)}  hrs   │')
        print(f'│ ╰─┬─╯                                         │')
        # print(f' ✘ - Trabalhado SEM ponto : {tempo_trabalhado_sem_ponto} hrs')
        # print(f' ✘ - Restante   SEM ponto : {tempo_restante_sem_ponto} hrs')
    

    if tempo_restante_com_ponto < timedelta(0):
        print(f'│ ╭─┴─╮                                         │')
        print(f'│ │ ✔ ├╼ Trabalhado COM ponto : {str(tempo_total_com_ponto).rjust(8)}  hrs   │')
        print(f'│ ╰─┬─╯                                         │')
        print(f'╰───┴───────────────────────────────────────────╯')
        # print(f' ✔ - Trabalhado COM ponto : {tempo_total_com_ponto} hrs')
    else:
        print(f'│ ╭─┴─╮                                         │')
        print(f'│ │ ✔ ├╼ Trabalhado COM ponto : {str(tempo_total_com_ponto).rjust(8)}  hrs   │')
        print(f'│ │ ✔ ├╼ Restante   COM ponto : {str(tempo_restante_com_ponto).rjust(8)}  hrs   │')
        print(f'│ ╰─┬─╯                                         │')
        # print(f' ✔ - Trabalhado COM ponto : {tempo_total_com_ponto} hrs')
        # print(f' ✔ - Restante   COM ponto : {tempo_restante_com_ponto} hrs')
        # print('\n-----------------------------------------------\n')
        fim = tempo_ultimo_ponto_entrada + tempo_restante_com_ponto
        print(f'│   ╰────────────────────────────────────╮      │')
        print(f'│                                  ╭─────┴────╮ │')
        print(f'│    Deve fechar o ponto as ╾──────┤ {str(fim.time().strftime("%H:%M:%S")).rjust(8)} │ │')
        print(f'│ Finalizar o dia com {str(carga_dia_trabalho).rjust(8)} Hrs ╰─────┬────╯ │')
        # print(f'│    Para finalizar o dia com  {carga_dia_trabalho}         │')
        # print(f'│    Para finalizar o dia com ╾────┤ {carga_dia_trabalho}  │ │')
        # print(f'│                                  ╰─────┬────╯ │')
        print(f'╰────────────────────────────────────────┴──────╯')

        # Soma o tempo restante com a hora de início

        # Formata o resultado para exibir somente a hora, sem a data

        # print(f'Deve fechar o ponto as {fim.time().strftime("%H:%M:%S")}')
        # print(f'Para finalizar o dia com {carga_dia_trabalho} horas\n')
        # print('-----------------------------------------------')

def calcular_total_horas(data_atual):
    print('\n-----------------------------------------------\n')
    total_horas = timedelta()

    if data_atual.day > FIRST_WORKING_DAY_OF_THE_MONTH:
        data_atual = data_atual + relativedelta(months=1)

    ano_atual = data_atual.year
    mes_atual = data_atual.month

    # Definir o intervalo de datas a serem consideradas
    data_inicio_mes_anterior = data_atual.replace(day=LAST_WORKING_DAY_OF_THE_MONTH)
    
    if data_inicio_mes_anterior.day > FIRST_WORKING_DAY_OF_THE_MONTH:
        if mes_atual == 1:  # Se for janeiro, volta para dezembro do ano anterior
            mes_anterior = 12
            ano_anterior = ano_atual - 1
        else:
            mes_anterior = mes_atual - 1
            ano_anterior = ano_atual
        data_inicio_mes_anterior = data_inicio_mes_anterior.replace(year=ano_anterior, month=mes_anterior)
    
    data_inicio_mes_atual = data_atual.replace(day=1)
    
    # Loop para percorrer os arquivos CSV
    for data_inicio in [data_inicio_mes_anterior, data_inicio_mes_atual]:
        nome_arquivo = f'{NOME_DIRETORIO_RAIZ}/{data_inicio.year}/{data_inicio.month}.csv'
        
        try:
            with open(nome_arquivo, 'r') as arquivo:
                reader = csv.reader(arquivo)
                next(reader)  # Ignorar a linha de cabeçalho
                
                for linha in reader:
                    dia = int(linha[0])
                    if data_inicio == data_inicio_mes_anterior and dia < LAST_WORKING_DAY_OF_THE_MONTH:  # Ignorar dias menores que {LAST_WORKING_DAY_OF_THE_MONTH} do mês anterior
                        continue
                    if data_inicio == data_inicio_mes_atual and dia > FIRST_WORKING_DAY_OF_THE_MONTH:  # Ignorar dias maiores que {FIRST_WORKING_DAY_OF_THE_MONTH} do mês atual
                        continue
                    
                    total_dia = datetime.strptime(linha[-1], '%H:%M:%S')
                    total_horas += timedelta(hours=total_dia.hour, minutes=total_dia.minute, seconds=total_dia.second)
            
        except FileNotFoundError:
            print(f"Arquivo {nome_arquivo} não encontrado.")
    
    # Exemplo de uso
    total = total_horas
    total_em_horas = total.total_seconds() / 3600
    total_em_horas = round(total_em_horas, 2)
    total_a_receber = total_em_horas * VALUE_PER_HOUR

    if(total_em_horas == 0):
        return

    # Exibir a quantidade total de horas como número decimal
    print(f"Total de horas (decimal): {total_em_horas}")
    if(total_em_horas < 160):
        total_horas_faltante = 160 - total_em_horas
        print(f"Para completar as 160 hora falta (decimal): {total_horas_faltante:.2f}")
    print(f"Total aproximado a receber R$:{total_a_receber:.2f}")

    # Exibir a quantidade total de horas no formato dias, horas e minutos
    dias = total.days
    horas, resto = divmod(total.seconds, 3600)
    minutos = resto // 60
    print(f"Total de horas (formato dias, horas e minutos): {dias} dia(s), {horas} hora(s) e {minutos} minuto(s)")

executar_novamente = ''

while True:
    print(f'┏━━━┓')
    print(f'┃ 1 ╉╼ Para pasta raiz')
    print(f'┃ 2 ╉╼ Para print o {nome_arquivo}')
    print(f'┃ 3 ╉╼ Para pasta do ANO ATUAL')
    print(f'┃ 4 ╉╼ Para calcular qual horario de saida para um total de 8h')
    print(f'┃ 5 ╉╼ Somar as horas do mês de trabalho')
    print(f'┃ 6 ╉╼ Somar as horas do mês atual')
    print(f'┗━━━┛')
    print(f'┏━━━━━━┓')
    print(f'┃  01  ╉╼ Para print do DIA especifico no MÊS atual')
    print(f'┃ 2020 ╉╼ Para pasta do ANO ESPECIFICO')
    print(f'┗━━━━━━┛')
    print(f'┏━━━┓')
    print(f'┃ 0 ╉╼ Para terminar')
    print(f'┗━━━┛')

    if executar_novamente != '0':
        option = executar_novamente
    else:
        option = input("Opção: ").lower()

    if option == '0':
        break
    elif option == '1':
        print(f'\nAbrindo: {dir_path}')
        open_directory_in_file_manager(dir_path)
        break
    elif option == '2':
        print()
        dataframe = pd.read_csv(diretorio_file)
        print(dataframe.to_string(index=False, header=True, na_rep='  :  :  ', justify='center'))
    elif option == '3':
        print(f'\nAbrindo: {diretorio_atual}')
        open_directory_in_file_manager(diretorio_atual)
        break
    elif option == '4':
        horas_faltantes_8h()
    elif option == '5':
        calcular_total_horas(data_atual)
    elif option == '6':
        print('\n-----------------------------------------------\n')
         # Obter a data especifica
        data_atual_string = input("Data (MM/AAAA): ")
        data_especifica = datetime.strptime("01/" + data_atual_string, "%d/%m/%Y").date()
        calcular_total_horas(data_especifica)
    elif option.isdigit() and len(option) == 2:
        fetch_day(option)
    elif option.isdigit() and len(option) == 4:
        diretorio_espc_ano = f'{diretorio_anos}/{option}'
        print(f'\nAbrindo: {diretorio_espc_ano}')
        if os.path.isdir(diretorio_espc_ano):
            open_directory_in_file_manager(diretorio_espc_ano)
            break
        print(f'Essa pasta não existe\n')
    else:
        # teste = data_atual.month
        # print(teste)
        pass

    # Pergunta se o usuário quer executar o código novamente
    executar_novamente = input('\nOpção: ').lower()

    # Se a resposta for 'n' ou 'não', encerra o loop e o programa
    if executar_novamente in ['n', 'não', 'nao', '0']:
        break
    else:
        os.system('clear')
