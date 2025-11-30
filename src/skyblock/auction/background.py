import requests, time
from ..api import cooldown as apicooldown

async def main(userapi, useruuid, notified_auctions):
    result = {}
    now = int(time.time() * 1000)

    data = await apicooldown(f"https://api.hypixel.net/skyblock/auction?key={userapi}&player={useruuid}")
    ah = data.get("auctions", [])

    for i in ah:
        auc_data = i.get("auction", i)
        auc_id = auc_data.get("uuid")
        end_time = auc_data.get("end", 0)

        if end_time <= now:
            if auc_data['claimed'] == False:
                if auc_id in notified_auctions:
                    continue

                item_name = auc_data.get("item_name", "Unknown")
                sold_price = auc_data.get("highest_bid_amount", auc_data.get("starting_bid", 0))
                result[auc_id] = {"item": item_name, "price": sold_price}
                notified_auctions.add(auc_id)
            
    return result