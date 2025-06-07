from fastapi import FastAPI, Form
import requests

app = FastAPI()

@app.post("/oauth/token")
def get_token(client_id: str = Form(...), client_secret: str = Form(...)):
    res = requests.post(
        "https://analytics.dev.powerdms.net/api/4.0/login",
        data={"client_id": client_id, "client_secret": client_secret}
    )
    return res.json()
