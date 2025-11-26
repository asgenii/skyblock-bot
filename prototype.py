api = "a7cc82ed-0f24-4e3d-8bc8-f04373d2ab55"
uuid = "d595c8de-79f4-4bd9-a6c8-c4199cbf4cae"
nickname = "FutureNOTHING"

import requests

# response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{nickname}").json()['id']
# print(response)

data = requests.get(f"https://api.hypixel.net/skyblock/auction?key={api}&player={uuid}").json()
if not data["success"]:
    print("csl: terminated close")
    exit()

ah = data.get("auctions", [])
ahact, ahcomp = [], []
for ahl in ah:
    if ahl.get("claimed") == False:
        ahact.append(ahl)

    else:
        ahcomp.append(ahl)

for i in ahact:
    print(f"{i['item_name']} {i['starting_bid']}")

print('\n\n\n')
for i in ahcomp:
    print(f"{i['item_name']} {i.get('highest_bid_amount', 0)}")