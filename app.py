import io
import base64 
# Importar Flask, render_template, request e jsonify
from flask import Flask, render_template, request, jsonify
# Importar a biblioteca qrcode
import qrcode
# Importar o dicionário de links do arquivo form_data.py
from form_data import FORM_LINKS

app = Flask(__name__)

# --- Configuração ---
# Lista de turmas disponíveis
TURMAS = ["DCC119 C - Seg / Qui 8h","DC5199 A - Ter 8h","DC5199 B - Ter 10h", "DC5199 G - Qua 8h","DC5199 HH - Qua 10h"]
# --------------------
 

# Rota principal - passa a lista de turmas para o template
@app.route('/')
def index():
    """Renderiza a página inicial com o seletor de turmas."""
    return render_template('index.html', turmas=TURMAS)

# Nova rota para gerar o QR Code (aceita requisições POST)
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    """Gera o QR Code com base na turma e data selecionadas."""
    data = request.get_json()

    # 1. Validação da entrada
    if not data or 'turma' not in data or 'data' not in data:
        return jsonify({"error": "Requisição inválida. Turma e data são obrigatórias."}), 400

    turma_selecionada = data['turma']
    data_selecionada = data['data'] # Formato esperado: 'AAAA-MM-DD'

    if not turma_selecionada or not data_selecionada:
         return jsonify({"error": "Turma ou data não podem estar vazias."}), 400

    # 2. Buscar o link no dicionário
    turma_links = FORM_LINKS.get(turma_selecionada)
    if not turma_links:
        print(f"AVISO: Turma '{turma_selecionada}' não encontrada no dicionário FORM_LINKS.")
        return jsonify({"error": f"Turma '{turma_selecionada}' não configurada."}), 404 # Not Found

    link_para_qrcode = turma_links.get(data_selecionada)
    if not link_para_qrcode:
        print(f"AVISO: Link para turma '{turma_selecionada}' na data '{data_selecionada}' não encontrado.")
        return jsonify({"error": f"Link para a aula de {turma_selecionada} em {data_selecionada} não encontrado."}), 404 # Not Found

    print(f"Gerando QR Code para: Turma='{turma_selecionada}', Data='{data_selecionada}', Link='{link_para_qrcode[:30]}...'") # Log reduzido

    # 3. Gerar o QR Code com o link encontrado
    try:
        img = qrcode.make(link_para_qrcode)
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        qr_code_data_uri = f"data:image/png;base64,{img_base64}"

        # 4. Retornar o QR Code e as informações usadas
        return jsonify({
            "qr_code": qr_code_data_uri,
            "turma": turma_selecionada,
            "data": data_selecionada # Retorna a data usada (opcional, mas pode ser útil)
        })

    except Exception as e:
        print(f"Erro ao gerar QR Code para {turma_selecionada} em {data_selecionada}: {e}")
        return jsonify({"error": "Erro interno ao gerar QR Code."}), 500


# Bloco para rodar o servidor
if __name__ == '__main__':
    # host='0.0.0.0' torna acessível na rede local
    # debug=True ativa o modo de depuração (recarrega automaticamente, mostra erros)
    app.run(host='0.0.0.0', port=5000, debug=True)
