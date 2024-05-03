import psycopg2

conexao = psycopg2.connect(database="FixadeTreino",
                           host="localhost",
                           user="postgres",
                           password="#Dddmglouros",
                           port="5432")
print(conexao.info)
print(conexao.status)

cursor = conexao.cursor()
cursor.execute('select * from Biopedancia')
print(cursor.fetchall())

# Pedido para inserir os dados do usuario ou cliente // interação homem maquina
nome = input("Digite o nome: ")
peso = float(input("Digite o peso (em kg): "))
estatura = float(input("Digite a estatura(em metros): "))
bracoES = float(input("Digite o tamanho do braçoES (em cm): "))
bracoDI = float(input("Digite o tamanho do braçoDI (em cm): "))
antibracoES = float(input("Digite o tamanho do antibraçoES (em cm): "))
antibracoDI = float(input("Digite o tamanho do antibraçoDI (em cm): "))
coxaES = float(input("Digite o tamanho da coxaEs (em cm): "))
coxaDI = float(input("Digite o tamanho da coxaDi (em cm): "))
torax = float(input("Digite o tamanho do torax (em cm): "))
abdominal = float(input("Digite o tamanho do abdomem (em cm): "))
quadril = float(input("Digite o tamanho do quadril (em cm): "))
cintura = float(input("Digite o tamanho da cintura (em cm): "))
panturilhaES = float(input("Digite o tamanho da panurilhaES  (em cm): "))
panturilhaDI = float(input("Digite o tamanho da panurilhaDI (em cm): "))

# Calcula o IMC
imc = peso / (estatura ** 2)
print(imc)

# Insere os dados na tabela
cursor.execute("""
    INSERT INTO Biopedancia
    ( nome, peso, estatura, bracoES,bracoDI,antibracoES,antibracoDI,coxaES, coxaDI,torax, abdominal, quadril,cintura, 
    panturilhaES, panturilhaDI, imc)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s,%s);
""", (
    nome, peso, estatura, bracoES, bracoDI, antibracoES, antibracoDI, coxaES, coxaDI, torax, abdominal, quadril,
    cintura,
    panturilhaES, panturilhaDI, imc))

# Confirma a transação
cursor.execute(Biopedancia)
conexao.commit()

# Fecha a conexão
cursor.close()
conexao.close()

print("Dados inseridos com sucesso!")
