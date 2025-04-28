# Gerador de QR Code para Registro de Presença

Este projeto permite gerar QR Codes dinamicamente para registrar a presença em aulas ou eventos, gerando QR Code para acesso rápido a formulários de presença associados a uma turma e data específicas.

## Resumo Rápido

-   Crie um formulário de presença para cada aula (o QR Code gerado apontará para este formulário).
-   Configure as turmas, datas e o link base do formulário no código backend (Python/Flask).
-   Rode o projeto e utilize a interface web para gerar o QR Code para a aula desejada.

## Descrição

A aplicação web fornece uma interface simples onde o usuário seleciona uma data e, em seguida, uma turma. Ao selecionar ambos, um QR Code é gerado dinamicamente. Este QR Code contém um link (configurado no backend) que direciona para um formulário online (como Google Forms) para que os participantes possam registrar sua presença escaneando o código com seus smartphones.

## Funcionalidades

-   Seleção de data através de um calendário.
-   Seleção de turma a partir de uma lista pré-definida (configurada no backend).
-   Geração dinâmica de QR Code via chamada assíncrona para o backend.
-   Exibição do QR Code gerado na página.

## Tecnologias Utilizadas

-   **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
-   **Backend:** Python, Flask e qrcode[pil] (Biblioteca de Geração de QR Code)
-   **Templating:** Jinja2 (integrado ao Flask)

## Requisitos

-   Python 3.x
-   Pip (gerenciador de pacotes Python)
-   Bibliotecas Python (listadas em `requirements.txt` - *você precisará criar este arquivo*)
    -   Flask
    -   qrcode (`pip install qrcode[pil]`) 

## Instalação e Configuração

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Carchedi/presenca-aula-qrcode.git # Ou simplesmente coloque os arquivos em uma pasta
    cd <pasta-do-projeto>
    ```

2. **Instale as dependências:**
    ```bash
       pip install flask
       pip install qrcode[pil]
    ```

3. **Configure as Turmas (`turmas.py`):**
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

4.  **Configure os Links dos Formulários (`form_data.py`):**
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
 

## Uso

1.  **Execute a aplicação Flask:**
    ```bash
     python3 app.py
    ```

2.  **Acesse a aplicação:**
    Abra seu navegador e vá para o endereço fornecido pelo Flask (geralmente `http://127.0.0.1:5000`).

3.  **Gere o QR Code:**
    -   A data atual será selecionada por padrão. Se necessário, escolha outra data.
    -   Selecione a turma desejada na lista suspensa que aparecerá (essas turmas foram definidas no Array 'TURMAS').
    -   Será gerado e exibido um QRCode com o link do formulário adicionado em 'FORM_LINKS' para aquela turma naquela data.

4.  **Registre a Presença:**
    -   Exiba o QR Code para os participantes (ex: em um projetor).
    -   Os participantes devem escanear o código com seus smartphones.
    -   Eles serão redirecionados para o formulário de presença configurado para preencherem seus dados.

## Como Funciona

1.  O usuário acessa a página inicial (`index.html`).
2.  O JavaScript define a data atual no seletor de data.
3.  Ao selecionar uma data, o seletor de turmas é exibido.
4.  Ao selecionar uma turma (e com a data já selecionada), o JavaScript envia uma requisição POST para o endpoint `/generate_qr` no backend Flask, contendo a turma e a data selecionadas em formato JSON.
5.  O backend Flask recebe a requisição, constrói a URL do formulário (incluindo turma e data, se configurado), gera um QR Code para essa URL e o converte para uma string Base64.
6.  O backend retorna a string Base64 do QR Code em uma resposta JSON.
7.  O JavaScript no frontend recebe a resposta, decodifica a imagem Base64 e a exibe na tag `<img>` dentro do container `qrCodeContainer`.
8.  Instruções para escanear o código são exibidas.
