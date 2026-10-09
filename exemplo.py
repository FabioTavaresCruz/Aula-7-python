produto = "Mouse Gamer WIFI"

if "mouse".lower() in produto.lower():
    print ("produto encontrado")
else:
    print ("Produto não encontrado")



Valores = [20,71,100,30]

def dobrar(valor):
    resultado = valor * 2
    return resultado

valores_novos = []
for valor in Valores:
    valores_novos.append(dobrar(valor))
print (valores_novos)


alunos = ["Ana","Hugo","Mariana","Pedro","Ana Paula"]

aluno_procurado = input("Digite um nome: ")
alunos_encontrados = []
for item in alunos:
    alunos_encontrados.append(item)
print (alunos_encontrados)
    


