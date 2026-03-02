import requests

CLIENT_ID = "86o2yxabkpve7z"
CLIENT_SECRET = "WPL_AP1.dMfos3yIQWdLWoYK.ikWKsQ=="
REDIRECT_URI = "http://localhost:8000/callback"

code = "AQRJ3Uv1gE16ZrLYdYPDWHyTIIEZTb6TkJxCCA-Q_4yM853sOncZhu5Ins0C2IkBTTmav9YhtUzIyuMFYmehESJ_eNHWfwzT4k-8s1YhC9a0XCv-z_KfaYVk7tw1B_RFDwOWp5YdWOR5KH0Rh3_nRAqY5hHQL1Dw1rPkQawPdLK2rgIop3DWzz1MtX9BDQp2jnzuQN8JNYwqZGWycqc"

response = requests.post(
    "https://www.linkedin.com/oauth/v2/accessToken",
    data={
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    },
)

print(response.json())