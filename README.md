# 📚 Gerador de QR Code para Formulários de Presença

Este é um projeto simples em Flask (Python) que gera QR Codes para links de formulários (como Google Forms) com base na turma e na data selecionadas. O objetivo é gerar, para cada aula, um QRCode com o link de um formulário de presença específico.

## Resumo:
* Crie um formulário de presença para **cada** aula
* Atribua no código os nomes da aulas, tal como as datas e o link do formulário pra cada aula
* Rode o código e gere o QRCode com o link do formulário a cada aula 

## Funcionalidades

*   Interface web para selecionar a turma e a data.
*   Geração dinâmica de QR Code correspondente ao link do formulário da aula selecionada.
*   Configuração centralizada dos nomes das turmas e dos links dos formulários em arquivos Python.
*   Fácil de executar localmente.

## Pré-requisitos

*   Python 3.6 ou superior
*   pip (gerenciador de pacotes do Python)

## Configuração do Ambiente

1.  **Clone o Repositório (ou baixe os arquivos):**
    ```bash
    git clone https://github.com/Carchedi/presenca-aula-qrcode.git # Ou simplesmente coloque os arquivos em uma pasta
    cd <pasta-do-projeto>
    ```

2.  **Instale as Dependências:**
    ```bash
    pip install Flask qrcode[pil]
    ```

## Configuração do Projeto

Antes de executar a aplicação, é **necessário** configurar suas turmas e os links dos formulários correspondentes.

1.  **Configure as Turmas (`turmas.py`):**
    *   Abra o arquivo `turmas.py`.
    *   Edite a lista `TURMAS` para incluir os nomes exatos das suas turmas. Estes nomes serão exibidos no seletor da página web.
    *   Exemplo:
        ```python
        TURMAS = [
            "Nome da Turma 1 - Dia/Horário",
            "Nome da Turma 2 - Dia/Horário",
            "Outra Turma - Dia/Hora"
        ]
        ```

2.  **Configure os Links dos Formulários (`form_data.py`):**
    *   Abra o arquivo `form_data.py`.
    *   Edite o dicionário `FORM_LINKS`.
    *   As **chaves principais** deste dicionário devem ser **exatamente iguais** aos nomes das turmas definidos em `turmas.py`.
    *   Para cada turma (chave principal), o valor deve ser outro dicionário.
    *   Neste dicionário interno, as **chaves** devem ser as **datas das aulas** no formato **`'AAAA-MM-DD'`** (ano-mês-dia).
    *   Os **valores** devem ser os **links completos** para os formulários correspondentes àquela turma naquela data específica.
    *   **Exemplo:**
        ```python
        FORM_LINKS = {
            "Nome da Turma 1 - Horário": {
                "2024-08-20": "https://link-para-o-form-da-turma1-20-08.com",
                "2024-08-22": "https://link-para-o-form-da-turma1-22-08.com",
                # Adicione mais datas e links para esta turma
            },
            "Nome da Turma 2 - Horário": {
                "2024-08-21": "https://link-para-o-form-da-turma2-21-08.com",
                "2024-08-23": "https://link-para-o-form-da-turma2-23-08.com",
                # Adicione mais datas e links para esta turma
            },
            # Adicione entradas para todas as turmas listadas em turmas.py
        }
        ```
    *   **IMPORTANTE:** Se uma combinação de turma e data selecionada pelo usuário não existir no dicionário `FORM_LINKS`, um erro será exibido na interface web e nenhum QR Code será gerado.

## Executando a Aplicação

1.  Navegue até o diretório raiz do projeto no seu terminal.
2.  Execute o script principal:
    ```bash
    python app.py
    ```
3.  A aplicação Flask será iniciada. Por padrão, ela estará acessível no seu navegador web em:
    `http://127.0.0.1:5000` ou `http://localhost:5000`
    *   O uso de `host='0.0.0.0'` no `app.run` torna a aplicação acessível por outros dispositivos na mesma rede local, usando o endereço IP da máquina onde o servidor está rodando (ex: `http://192.168.1.10:5000`).

## Como Usar

1.  Abra o endereço da aplicação no seu navegador.
2.  Selecione a **Turma** desejada no menu suspenso.
3.  Selecione a **Data** da aula usando o seletor de data.
4.  Clique no botão "Gerar QR Code".
5.  Se um link correspondente à turma e data selecionadas existir no arquivo `form_data.py`, o QR Code será exibido abaixo do botão. Caso contrário, uma mensagem de erro será mostrada.
6.  Mostre o QR Code gerado para que os alunos possam escaneá-lo e acessar o formulário de presença.

## Tecnologias Utilizadas

*   Python
*   Flask (Microframework Web)
*   qrcode (Biblioteca para geração de QR Code)
*   HTML/CSS/JavaScript (Para a interface do usuário)
