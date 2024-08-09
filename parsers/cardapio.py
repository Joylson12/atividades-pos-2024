from xml.dom.minidom import parse

dom = parse("parsers/cardapio.xml")
cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName("prato")

for prato in pratos:
    
    cardapioId = prato.getAttribute("id")
    elemento_nome = prato.getElementsByTagName("nome")[0].firstChild.nodeValue
    print(f" Prato {cardapioId }: {elemento_nome}")  
 

prato_id = int(input("Esolha um Prato do cardapio: "))
prato = pratos [prato_id]

descricao_prato = prato.getElementsByTagName("descricao")[0].firstChild.nodeValue 
elemento_ingredientes = prato.getElementsByTagName("ingrediente")
elemento_ingredientes = [ingrediente.firstChild.nodeValue for ingrediente in elemento_ingredientes]
precoPrato = prato.getElementsByTagName("preco")[0].firstChild.nodeValue 
caloriasPrato = prato.getElementsByTagName("calorias")[0].firstChild.nodeValue 
tempoPreparo = prato.getElementsByTagName("tempoPreparo")[0].firstChild.nodeValue 

print(f"Nome do Prato: {elemento_nome}")
print(f"Descrição do Prato: {descricao_prato}")
print(f"Ingredientes:")
print(f"Preço do Prato: {precoPrato}")
print(f"Calorias do Prato: {caloriasPrato} Kilocaloria")
print(f"Tempo de Preparo: {tempoPreparo}")
