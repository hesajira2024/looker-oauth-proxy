from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
import requests

app = FastAPI()

@app.post("/oauth/token")
def get_token(client_id: str = Form(...), client_secret: str = Form(...)):
    # Call Looker login endpoint
    res = requests.post(
        "https://analytics.dev.powerdms.net/api/4.0/login",
        data={"client_id": client_id, "client_secret": client_secret}
    )
    data = res.json()
    
    # Reformat the response to be strictly OAuth2-compliant
    return {
        "access_token": data.get("access_token"),
        "token_type": "Bearer",
        "expires_in": data.get("expires_in", 3600)  # default to 1 hour if not included
    }

@app.get("/authorize")
def authorize(request: Request):
    redirect_uri = request.query_params.get("redirect_uri")
    state = request.query_params.get("state", "")
    return RedirectResponse(f"{redirect_uri}?code=dummy-auth-code&state={state}")

