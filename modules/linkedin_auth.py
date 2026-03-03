import requests
from config import LINKEDIN_CODE
from config import CLIENT_ID
from config import CLIENT_SECRET
from config import REDIRECT_URL 



response = requests.post(
    "https://www.linkedin.com/oauth/v2/accessToken",
    data={
        "grant_type": "authorization_code",
        "code": LINKEDIN_CODE,
        "redirect_uri": REDIRECT_URL,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    },
)

print(response.json())