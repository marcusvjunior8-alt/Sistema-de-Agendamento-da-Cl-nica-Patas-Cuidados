""" Entrada de Valores """
name = input('Digite seu nome:\n')
name_pet = input('Digite o nome do pet:\n')
species = input('Digite a espécie:\n')
service = input('Escolha o serviço (banho ,tosa ou consulta):\n')
price = float(input('Digite o preço:\n'))
club_pet = input('Cliente faz parte do clube pet?(sim ou não)\n')
""" valores padrões antes de verificar """
desconto = 0.0
valor_taxa = 0.0

""" Condições """
if club_pet.lower() == 'sim':
    desconto = price * 0.15
if species.lower() == 'gato':
    valor_taxa = 10.0
""" Calculo : preço base - desconto + taxa """
valor_total = (price - desconto) + valor_taxa
""" Tela de resultados """
print('--- Patas & Cuidados ---\n')
print('Nome do cliente:', name ,'\n Nome do pet:',name_pet)
print('Preço base: R$',price)
print('Desconto: R$',desconto)
print('Taxa de manejo: R$', valor_taxa)
print('Valor total: R$', valor_total)

