from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import RedirectResponse
import requests

app = FastAPI()

@app.post("/oauth/token")
def get_token(client_id: str = Form(...), client_secret: str = Form(...)):
    try:
        res = requests.post(
            "https://analytics.dev.powerdms.net:8443/api/4.0/login",
            data={"client_id": client_id, "client_secret": client_secret},
            timeout=10
        )
        res.raise_for_status()
        data = res.json()
        return {
            "access_token": data.get("access_token"),
            "token_type": "Bearer",
            "expires_in": data.get("expires_in", 3600)
        }
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Looker login failed: {str(e)}")

@app.get("/authorize")
def authorize(request: Request):
    redirect_uri = request.query_params.get("redirect_uri")
    state = request.query_params.get("state", "")
    return RedirectResponse(f"{redirect_uri}?code=dummy-auth-code&state={state}")
