from flask_cors import CORS
from flask import Flask, request, jsonify
from minhas_funcoes import salvar_lista_arquivo, adicionar_valor_arquivo, ler_arquivo

app = Flask(__name__)
CORS(app)

dados_telas = []


@app.route('/quant_ux_data/<int:num_tela>', methods=['POST'])
def receber_dados_quant_ux(num_tela):
  try:
    dados_quant_ux = request.get_json()

    # No meu quant ux as únicas telas que têm dados para serem salvos são as telas 2 e 5
    if num_tela == 2:
      processar_tela_2(dados_quant_ux)
    elif num_tela == 5:
      processar_tela_5(dados_quant_ux)
    else:
      return {"erro": "Número de tela não suportado"}, 400

    salvar_lista_arquivo(dados_telas)

    return {
        "mensagem":
        f"Dados da tela {num_tela} do Quant-UX recebidos com sucesso!"
    }, 201
  except Exception as e:
    return {"erro": str(e)}, 500


def processar_tela_2(dados):
  if 'nome_animal' in dados and 'nome_dono' in dados and 'idade_pet' in dados and 'email_tutor' in dados and 'senha_tutor' in dados:
    dados_telas.append(
        f"Nome Animal: {dados['nome_animal']}, Nome Dono: {dados['nome_dono']}, Idade Pet: {dados['idade_pet']}, Email Tutor: {dados['email_tutor']}, Senha Tutor: {dados['senha_tutor']}"
    )


def processar_tela_5(dados):
  if 'peso_animal' in dados and 'altura_animal' in dados:
    dados_telas.append(
        f"Peso Animal: {dados['peso_animal']}, Altura Animal: {dados['altura_animal']}"
    )


if __name__ == '__main__':
  app.run(host='0.0.0.0')
