import requests
import json

ACCESS_TOKEN = "AQW2A_vvYyHcBlpA3qcummBQncUHe_Q5yIltkXAKiEG_LJMYodmBf6aWk-gda7ChZMPPZhtiipmRbVspMqr12L9nOx_Qf8dWYyVqN6TtytCAjrJg45i7sTYiWOGmcXMbthF6-WZwEKaiHHOVJazsU00JbYOf0arOp4AxlCrVP3-LdWbuleQZkblZ-Aoxr88vLFW72vNrlDEy1gG3ybykCIz9pP8zir8SppFwm5-aNWTENSWICPmtUEBzoRYpdDyFVyW55OJMnzA-bh7JYO7N_yUSxjbbDSPXC8xS23ubNZeS1v6kYk174tbM1Xk7N_jZYMUCKuu5Mb_H6KhUPyvTN-Ev_f1tTg"
PERSON_URN = "urn:li:person:hA7oDaqjgV"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0",
    "Content-Type": "application/json"
}

post_data = {
    "author": PERSON_URN,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "Testing auto post from my AI agent 🚀"
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

response = requests.post(
    "https://api.linkedin.com/v2/ugcPosts",
    headers=headers,
    data=json.dumps(post_data)
)

print(response.status_code)
print(response.text)