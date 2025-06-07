from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
import requests

app = FastAPI()

@app.post("/oauth/token")
def get_token(client_id: str = Form(...), client_secret: str = Form(...)):
    res = requests.post(
        "https://analytics.dev.powerdms.net/api/4.0/login",
        data={"client_id": client_id, "client_secret": client_secret}
    )
    return res.json()

@app.get("/authorize")
def authorize(request: Request):
    redirect_uri = request.query_params.get("redirect_uri")
    state = request.query_params.get("state", "")
    # Simulate redirect to the callback with dummy auth code
    redirect_with_code = f"{redirect_uri}?code=dummy-auth-code&state={state}"
    return RedirectResponse(redirect_with_code)
