import requests
import json
from config import LINKEDIN_ACCESS_TOKEN
from config import LINKEDIN_MEMBER_ID

ACCESS_TOKEN = LINKEDIN_ACCESS_TOKEN
PERSON_URN = f"urn:li:person:{LINKEDIN_MEMBER_ID}"

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