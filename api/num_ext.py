import requests
from xml.dom.minidom import parseString

# Parte 1: Obter a capital da Noruega (NO)
def capitalNoruega(codigo_pais):
    """Obtém a capital da Noruega usando o código ISO do país."""
    url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
    
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>{codigo_pais}</sCountryISOCode>
                    </CapitalCity>
                </soap:Body>
                </soap:Envelope>"""

    headers = {'Content-Type': 'text/xml; charset=utf-8'}

    response = requests.post(url, headers=headers, data=payload)
    context = parseString(response.content)
    capital = context.getElementsByTagName('m:CapitalCityResult')[0].firstChild.nodeValue
    return capital

# Parte 2: Converter número para texto em inglês
def numTexto(numero):
    """Converte um número específico para seu equivalente em texto em inglês."""
    tabela_numeros = {
        212: "two hundred twelve",
        213: "two hundred thirteen",
        214: "two hundred fourteen",
        215: "two hundred fifteen",
        216: "two hundred sixteen",
        217: "two hundred seventeen",
        218: "two hundred eighteen",
        219: "two hundred nineteen",
        220: "two hundred twenty",
        221: "two hundred twenty-one",
        222: "two hundred twenty-two",
        223: "two hundred and twenty-three"
    }
    return tabela_numeros.get(numero, "Número não está na tabela!")

if __name__ == "__main__":
    # Exibir a capital da Noruega
    codigo_pais_noruega = "NO"
    capital_noruega = capitalNoruega(codigo_pais_noruega)
    print(f"Essa é capital da Noruega: {capital_noruega}")

    # Converter número para texto
    numero = int(input("Digite um número de 212 a 223:"))
    numero_extenso = numTexto(numero)
    print(f"O número {numero} por extenso e em inglês, fica assim: {numero_extenso}")
