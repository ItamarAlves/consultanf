# CONSULTANF

Projeto gera possíveis chaves de acessos com base nos dados informado, e já consulta essas chaves para retornar somente as chaves válidas.

## Dados da nota Fiscal
### Manual de Orientacao Contribuinte versão 6.00
- cUF - Código da UF do emitente do Documento Fiscal
- AAMM - Ano e Mês de emissão da NF-e
- CNPJ - CNPJ do emitente
- mod - Modelo do Documento Fiscal
- serie - Série do Documento Fiscal
- nNF - Número do Documento Fiscal
- tpEmis – forma de emissão da NF-e
- cNF - Código Numérico que compõe a Chave de Acesso
- cDV - Dígito Verificador da Chave de Acesso

## Rodar
```
$ git clone https://github.com/ItamarAlves/consultanf.git

$ pip install Flask
$ export FLASK_APP=main.py
$ flask run

```

## Instruções para Utilização

### Endpoints disponíveis
 - POST [/consulta]

 ### Body
 ``` json
 {
	"codigoUf": "00",
	"dataEmissao": "00/00/0000",
	"cnpj": "00000000000000",
	"modelo": "00",
	"serie": "000",
	"numeroNfInicio": "000000000",
	"numeroNfFinal": "000000000",
	"tipoEmissao": "0",
	"codigoNumerico": "00000000"		
}
 ```

 ### Retorno
 ``` json
 {
  "chaveValida": [
    ""
  ]
}
 ```