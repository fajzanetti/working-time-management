# Sistema de Gerenciamento de Ponto

Este é um programa Python simples para automatizar o registro de pontos de entrada e saída ao longo do dia. Ele cria um arquivo CSV que registra os horários de entrada e saída em intervalos regulares durante o dia. Ele consiste em vários scripts e componentes que trabalham juntos para fornecer funcionalidades específicas.

## Índice

- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Clone o repositório](#clone-o-repositório)
- [Configuração](#configuração)
- [Uso](#uso)
  - [Execução do Sistema](#execução-do-sistema)
  - [Opções Disponíveis](#opções-disponíveis)
- [Contribuição](#contribuição)

# Requisitos

- Python 3
- Biblioteca Python: `os`
- Biblioteca Python: `csv`
- Biblioteca Python: `pandas`
- Biblioteca Python: `datetime`
- Biblioteca Python: `subprocess`
- Biblioteca Python: `load_dotenv`
- Biblioteca Python: `relativedelta` (da biblioteca `dateutil`)

# Instalação

Você pode instalar as bibliotecas usando o pip:

```bash

pip install python-dotenv pandas python-dateutil

```

# Clone o repositório

```bash

git clone https://github.com/fajzanetti/working-time-management.git

```

# Configuração

1. Faça uma cópia do arquivo `.env.example` no mesmo diretório com o nome `.env`.
2. Abra o arquivo `.env` em um editor de texto.

3. Configure as variáveis de ambiente conforme suas necessidades. Aqui estão as variáveis e exemplos:

   - **NOME_DIRETORIO_RAIZ**: Escolha um nome de diretório raiz para seus arquivos CSV. Exemplo: **NOME_DIRETORIO_RAIZ="Registros"**

   - **HEADER_CSV**: O cabeçalho a ser usado nos arquivos CSV gerados. Exemplo: **HEADER_CSV="Dia,Entrada 1,Saída 1,Entrada 2,Saída 2,Entrada 3,Saída 3,Total do dia"**

   - **VALUE_PER_HOUR**: Defina o valor por hora do seu salário. Exemplo: **VALUE_PER_HOUR=99**

   - **FIRST_WORKING_DAY_OF_THE_MONTH**: Escolha o primeiro dia do mês para contabilizar as horas. Exemplo: **FIRST_WORKING_DAY_OF_THE_MONTH=01**

     - **LAST_WORKING_DAY_OF_THE_MONTH**: Escolha o último dia do mês para contabilizar as horas. Exemplo: **LAST_WORKING_DAY_OF_THE_MONTH=30**

4. Salve o arquivo .env após configurar as variáveis de ambiente.

Agora, o arquivo .env está configurado com suas preferências e pode ser usado pelo seu código Python para realizar os cálculos necessários. Certifique-se de manter o arquivo .env seguro e não compartilhá-lo publicamente, pois ele pode conter informações sensíveis, como salário ou configurações específicas do ambiente.

# Uso

Este sistema foi criado para rastrear e calcular horas trabalhadas. Siga as etapas abaixo para utilizar o sistema:

## Execução do Sistema

Para iniciar o sistema, execute o script index.py localizado na pasta raiz do projeto. Você pode fazer isso digitando o seguinte comando no terminal:

```bash

python3 index.py

```

Isso abrirá uma interface de linha de comando interativa onde você pode escolher entre várias opções.

## Opções Disponíveis

O sistema oferece várias opções, incluindo:

1. Marcar Ponto: Use esta opção para registrar seu ponto de entrada e saída. Você pode registrar até três pontos por dia.

2. Pesquisar Ponto: Use esta opção para pesquisar e exibir os registros de ponto de entrada e saída.

   - Ao selecionar "Pesquisar ponto", você poderá:
     - **`[1]`** Abrir o projeto no VS Code (se configurado)
     - **`[2]`** Visualizar o arquivo CSV com os registros
     - **`[3]`** Abrir a pasta do ano atual
     - **`[4]`** Calcular o horário de saída para completar 8 horas
     - **`[5]`** Somar as horas trabalhadas no mês de trabalho
     - **`[6]`** Somar as horas trabalhadas no mês atual
     - **`[DIA]`** Pesquisar um dia específico no mês atual
     - **`[ANO]`** Abrir a pasta de um ano específico

3. Para sair do sistema, selecione a opção "Sair" no menu principal.

# Contribuição

Agradecemos muito pelo seu interesse em contribuir para este projeto! Sua ajuda é fundamental para tornar este software cada vez melhor.
