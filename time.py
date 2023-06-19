import os
import csv
import datetime
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

NOME_DIRETORIO_RAIZ = str(os.getenv('NOME_DIRETORIO_RAIZ'))
HEADER_CSV = os.getenv('HEADER_CSV')

# Diretório do executavel
dir_path = os.path.dirname(os.path.realpath(__file__))

# obter a data atual
data_atual = datetime.date.today()
dia = data_atual.strftime("%d")
# dia = data_atual.day+1
ano = data_atual.year
mes = data_atual.month
hora_atual = datetime.datetime.now().strftime('%H:%M:%S')

# criar o nome do diretório correspondente ao ano atual
nome_diretorio = f'{NOME_DIRETORIO_RAIZ}/{ano}'

# verificar se o diretório já existe
if not os.path.isdir(nome_diretorio):
    # se o diretório não existir, criá-lo
    os.makedirs(nome_diretorio)

# criar o nome do arquivo csv correspondente a este mês
nome_arquivo = f'{nome_diretorio}/{mes}.csv'

diretorio_completo = f'{dir_path}/{nome_arquivo}'
print(f'╭─────────────────────────────────────────────────╮')
print(f'│{str(diretorio_completo).center(49)}│')        # │
print(f'╰────────────────────────┬────────────────────────╯')
print(f'                         │                         ')


# verificar se o arquivo já existe
if not os.path.isfile(nome_arquivo):
    # se o arquivo não existir, criá-lo e adicionar o cabeçalho
    with open(nome_arquivo, 'w') as f:
        f.write(f'{HEADER_CSV}')
        print(f'╭────────────────────────┴────────────────────────╮')
        print(f'│{str("Novo arquivo criado.").center(49)}│')   #  │
        print(f'╰────────────────────────┬────────────────────────╯')
        print(f'                         │                         ')

# verificar se a linha correspondente ao dia atual já existe no arquivo
with open(nome_arquivo, 'r') as f:
    reader = csv.reader(f)
    linhas = list(reader)
    for i, row in enumerate(linhas):
        # verificar se a primeira coluna (Dia) é igual à data atual
        if row[0] == str(dia):
            if '' in row:
                # a linha já existe, preencher o próximo campo vazio com a hora atual
                primeiro_vazio = row.index('')
                row[primeiro_vazio] = hora_atual
                # row[primeiro_vazio] = '14:00:00'
                linhas[i] = row
                print(f'┏━━━━━━━━━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(f'┃{str(f"{linhas[0][primeiro_vazio]}: {hora_atual}").center(49)}┃')
                print(f'┗━━━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━┛')

            else:
                print(f'┏━━━━━━━━━━━━━━━━━━━━━━━━┷━━━━━━━━━━━━━━━━━━━━━━━━┓')
                print(f'┃{str("Já registrou todos os pontos possíveis do dia.").center(49)}┃')
                print(f'┗━━━━━━━━━━━━━━━━━━━━━━━━┯━━━━━━━━━━━━━━━━━━━━━━━━┛')
            break
    else:
        # a linha não existe, adicioná-la ao arquivo
        row = [str(dia), hora_atual, '', '', '', '', '', '']
        linhas.append(row)

# calcular o total do dia
total = datetime.timedelta()
def parse_horario(horario_str):
    try:
        return datetime.datetime.strptime(horario_str, '%H:%M:%S')
    except ValueError:
        return None

for row in linhas:
    if row[0] == str(dia):
        for i in range(1, 7, 2):  # percorre as colunas de horários (1, 3, 5)
            entrada = parse_horario(row[i])
            saida = parse_horario(row[i+1])
            if entrada and saida:  # só calcula o intervalo se ambos horários forem válidos
                intervalo = saida - entrada
                total += intervalo

# adicionar o total do dia à última coluna
linhas[-1][-1] = str(total)

print(f'╔════════════════════════╧════════════════════════╗')
print(f'║                          ╭─────────╮            ║')
print(f'║{str(f"Total do dia: │ {str(total).center(8)}│").center(49)}║')
print(f'║                          ╰─────────╯            ║')
print(f'╚════════════════════════╤════════════════════════╝')
print(f'                         │                         ')
print(f'  ╭──────────────────────╯                         ')

# escrever as linhas atualizadas de volta ao arquivo
with open(nome_arquivo, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(linhas)


print(f'┏━┷━┓')
print(f'┃ 1 ╉╼ Executar busca')
print(f'┃ 0 ╉╼ Fechar')
print(f'┗━┯━┛')

busca = input(f'  ╰──╼ Buscar: ').lower()

if busca in ['1']:
    os.system('clear')
    os.system('python3 search.py')
