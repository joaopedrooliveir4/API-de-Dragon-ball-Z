from flask import Flask, jsonify, request

app = Flask(__name__)

personagens = [
  {
    "id": 1,
    "nome": "Goku",
    "raca": "Saiyajin",
    "historia": "Enviado à Terra como bebê para conquistar o planeta, Goku sofreu uma lesão na cabeça que o fez esquecer sua missão. Criado como humano, ele se tornou um herói protetor da Terra.",
    "poder_maximo": 150000000,
    "maiores_feitos": [
      "Transformou-se em Super Saiyajin para derrotar Freeza (em Namekusei)",
      "Atingiu Super Saiyajin 3 para lutar contra Majin Boo",
      "Derrotou Kid Boo com a Genki Dama"
    ]
  },
  {
    "id": 2,
    "nome": "Vegeta",
    "raca": "Saiyajin",
    "historia": "Príncipe dos Saiyajins, Vegeta foi inicialmente inimigo de Goku. Com o tempo, tornou-se aliado e protetor da Terra, mas manteve seu orgulho e rivalidade com Goku.",
    "poder_maximo": 120000000,
    "maiores_feitos": [
      "Transformou-se em Majin Vegeta e enfrentou Goku",
      "Sacrificou-se contra Majin Boo em um gesto altruísta",
      "Atingiu Super Saiyajin 2 para enfrentar Cell e Majin Boo"
    ]
  },
  {
    "id": 3,
    "nome": "Gohan",
    "raca": "Meio-Saiyajin, Meio-Humano",
    "historia": "Filho de Goku e Chi-Chi, Gohan possui um enorme potencial de poder. Apesar de pacifista, ele luta quando necessário para proteger seus entes queridos.",
    "poder_maximo": 140000000,
    "maiores_feitos": [
      "Atingiu Super Saiyajin 2 e derrotou Cell",
      "Atingiu o estado Místico após o treinamento com o Supremo Senhor Kaioh",
      "Defendeu a Terra durante os ataques de Majin Boo"
    ]
  },
  {
    "id": 4,
    "nome": "Freeza",
    "raca": "Desconhecida (Mutante)",
    "historia": "Imperador galáctico cruel que destruiu o planeta Vegeta e escravizou os Saiyajins. Ele foi derrotado por Goku em Namekusei.",
    "poder_maximo": 120000000,
    "maiores_feitos": [
      "Destruiu o planeta Vegeta",
      "Derrotou vários Guerreiros Z em Namekusei",
      "Sobreviveu à explosão de Namekusei"
    ]
  },
  {
    "id": 5,
    "nome": "Cell",
    "raca": "Bio-Androide",
    "historia": "Criado pelo Dr. Gero usando células de guerreiros poderosos, Cell buscava atingir a perfeição ao absorver os andróides 17 e 18.",
    "poder_maximo": 120000000,
    "maiores_feitos": [
      "Organizou o Torneio de Cell para provar sua superioridade",
      "Absorveu os andróides 17 e 18, atingindo sua forma perfeita",
      "Travou uma batalha épica contra Gohan"
    ]
  },
  {
    "id": 6,
    "nome": "Majin Boo",
    "raca": "Criatura Mágica",
    "historia": "Criado pelo mago Bibidi, Majin Boo é uma entidade mágica que pode mudar de forma e regenerar-se. Ele causou destruição por milhares de anos.",
    "poder_maximo": 150000000,
    "maiores_feitos": [
      "Destruiu várias galáxias antes dos eventos de Dragon Ball Z",
      "Derrotou a maioria dos Guerreiros Z em várias formas",
      "Foi derrotado por Goku usando a Genki Dama"
    ]
  },
  {
    "id": 7,
    "nome": "Piccolo",
    "raca": "Namekuseijin",
    "historia": "Piccolo nasceu como a contraparte maligna do Kami-Sama original. Com o tempo, se tornou um aliado dos Guerreiros Z e mentor de Gohan.",
    "poder_maximo": 1000000,
    "maiores_feitos": [
      "Derrotou Raditz junto com Goku",
      "Fundiu-se com Nail e Kami-Sama, aumentando seu poder",
      "Protegeu a Terra durante a saga dos Andróides"
    ]
  },
  {
    "id": 8,
    "nome": "Trunks do Futuro",
    "raca": "Meio-Saiyajin, Meio-Humano",
    "historia": "Filho de Vegeta e Bulma de uma linha do tempo alternativa, ele viajou no tempo para avisar sobre a ameaça dos andróides.",
    "poder_maximo": 300000000,
    "maiores_feitos": [
      "Derrotou Freeza e Rei Cold com facilidade",
      "Ajudou a derrotar os Andróides 17 e 18 em sua linha do tempo",
      "Travou batalhas épicas durante a saga de Cell"
    ]
  },
  {
    "id": 9,
    "nome": "Andróide 18",
    "raca": "Androide",
    "historia": "Criada pelo Dr. Gero, a Andróide 18 foi projetada para destruir Goku. Mais tarde, se junta aos Guerreiros Z após sua luta contra Cell.",
    "poder_maximo": 25000000,
    "maiores_feitos": [
      "Lutou contra Vegeta e outros Guerreiros Z",
      "Tornou-se aliada dos Guerreiros Z e esposa de Kuririn",
      "Participou do Torneio do Poder no arco de Dragon Ball Super"
    ]
  },
  {
    "id": 10,
    "nome": "Kuririn",
    "raca": "Humano",
    "historia": "Um dos amigos mais próximos de Goku e um lutador habilidoso. Apesar de ser um humano, Kuririn frequentemente se destaca em batalhas.",
    "poder_maximo": 75000,
    "maiores_feitos": [
      "Lutou bravamente contra as forças de Freeza",
      "Ajudou Gohan e Goku em diversas batalhas",
      "Participou do Torneio do Poder em Dragon Ball Super"
    ]
  },
  {
    "id": 11,
    "nome": "Yamcha",
    "raca": "Humano",
    "historia": "Yamcha é um ex-bandido do deserto que se tornou aliado de Goku e um dos primeiros Guerreiros Z. Embora seu poder seja menor que o de outros personagens, ele desempenhou um papel importante no início da série.",
    "poder_maximo": 1480,
    "maiores_feitos": [
      "Lutou contra os Saiyajins Nappa e Vegeta, sacrificando-se para proteger seus amigos",
      "Participou de batalhas importantes na Saga dos Saiyajins e Freeza",
      "Se destacou como um lutador de artes marciais nos torneios iniciais"
    ]
  }
]

# Listar personagens
@app.route('/personagens', methods=['GET'])
def obter_personagens():
    return jsonify(personagens)

# Listar personagens por id
@app.route('/personagens/<int:id>', methods=['GET'])
def personagem_id(id):
    for personagem in personagens:
        if personagem.get('id') == id:
            return jsonify(personagem)

# Editar personagens por id
@app.route('/personagens/<int:id>', methods=['PUT'])
def editar_personagem(id):
    personagem_alterado = request.get_json()
    for i, personagem in enumerate(personagens):
        if personagem.get('id') == id:
            personagens[i].update(personagem_alterado)
            return jsonify(personagens[i])

# Criar novos personagens
@app.route('/personagens', methods=['POST'])
def novo_personagem():
    criar_novo_personagem = request.get_json()
    personagens.append(criar_novo_personagem)

    return jsonify(personagens)

# Deletar personagens por id
@app.route('/personagens/<int:id>', methods=['DELETE'])
def excluir_personagem(id):
    for i, personagem in enumerate(personagens):
        if personagem.get('id') == id:
            del personagens[i]
            return jsonify(personagens)
app.run(port=5000,host='localhost',debug=True)