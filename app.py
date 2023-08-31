from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/weather")
async def pegar_clima(cidade: str):
    api_key = "b619d00fa5a5670821bf8e06f118e99a"
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # dic com parametros para consulta na API:
    parametros_consulta = {
        "q": cidade,
        "appid": api_key,
        "units": "metric" #pegar em celsius
    }

    # requisição HTTP GET para a URL definida em base_url, passando os parâmetros definidos no dicionário parametros_consulta
    #vai retornar um objeto: Esses parâmetros serão incluídos na URL da requisição para fornecer informações adicionais para a API.
    resposta = requests.get(base_url, params=parametros_consulta)

    #se a requisição for 'ok':
    if resposta.status_code == 200:
        data = resposta.json()
        clima = {
            "cidade": data["name"],
            "temperatura": data["main"]["temp"],
            "clima": data["weather"][0]["description"]
        }
        return clima
    else:
        raise HTTPException(status_code=resposta.status_code, detail="Cidade não encontrada")

#  iniciar o servidor FastAPI usando o pacote chamado uvicorn
if __name__ == "__main__":
    # o uvicorn cria um servidor ASGI
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)