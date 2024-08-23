import requests
from xml.dom.minidom import parseString

# URL do serviço web
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

def obter_capital_pais(country_code):
    """Obtém a capital do país usando o código ISO do país."""
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>{country_code}</sCountryISOCode>
                    </CapitalCity>
                </soap:Body>
                </soap:Envelope>"""

    headers = {'Content-Type': 'text/xml; charset=utf-8'}

    response = requests.post(url, headers=headers, data=payload)
    context = parseString(response.content)
    capital = context.getElementsByTagName('m:CapitalCityResult')[0].firstChild.nodeValue
    return capital

def obter_moeda_pais(country_code):
    """Obtém a moeda do país usando o código ISO do país."""
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>{country_code}</sCountryISOCode>
                    </CountryCurrency>
                </soap:Body>
                </soap:Envelope>"""

    headers = {'Content-Type': 'text/xml; charset=utf-8'}

    response = requests.post(url, headers=headers, data=payload)
    context = parseString(response.content)
    moeda = context.getElementsByTagName('m:CountryCurrencyResult')[0].getElementsByTagName('m:sISOCode')[0].firstChild.nodeValue
    return moeda

def obter_codigo_telefone_pais(country_code):
    """Obtém o código de telefone do país usando o código ISO do país."""
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <CountryIntPhoneCode xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>{country_code}</sCountryISOCode>
                    </CountryIntPhoneCode>
                </soap:Body>
                </soap:Envelope>"""

    headers = {'Content-Type': 'text/xml; charset=utf-8'}

    response = requests.post(url, headers=headers, data=payload)
    context = parseString(response.content)
    codigo_telefone = context.getElementsByTagName('m:CountryIntPhoneCodeResult')[0].firstChild.nodeValue
    return codigo_telefone

codigo_pais = "NZ"


capital = obter_capital_pais(codigo_pais)
print(f"A capital da NZ é: {capital}")


moeda = obter_moeda_pais(codigo_pais)
codigo_telefone = obter_codigo_telefone_pais(codigo_pais)

print(f"Sua moedalocal: {moeda}")
print(f"Telefone do país: +{codigo_telefone}")
