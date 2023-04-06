import base64
import json
from requests import post, get

class SetToken:
  @staticmethod
  def get_token(client_id : str, client_secret : str):
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
      "Content-Type"  : "application/x-www-form-urlencoded"
    }
    data = "grant_type=client_credentials&client_id=" + client_id + "&client_secret=" + client_secret
    print(data)
    result = post(url, headers = headers, data = data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

  @staticmethod
  def get_auth_header(token):
    return {"Authorization": "Bearer  " + token}

