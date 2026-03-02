import requests

ACCESS_TOKEN = "AQW2A_vvYyHcBlpA3qcummBQncUHe_Q5yIltkXAKiEG_LJMYodmBf6aWk-gda7ChZMPPZhtiipmRbVspMqr12L9nOx_Qf8dWYyVqN6TtytCAjrJg45i7sTYiWOGmcXMbthF6-WZwEKaiHHOVJazsU00JbYOf0arOp4AxlCrVP3-LdWbuleQZkblZ-Aoxr88vLFW72vNrlDEy1gG3ybykCIz9pP8zir8SppFwm5-aNWTENSWICPmtUEBzoRYpdDyFVyW55OJMnzA-bh7JYO7N_yUSxjbbDSPXC8xS23ubNZeS1v6kYk174tbM1Xk7N_jZYMUCKuu5Mb_H6KhUPyvTN-Ev_f1tTg"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

response = requests.get(
    "https://api.linkedin.com/v2/userinfo",
    headers=headers
)

print(response.status_code)
print(response.json())