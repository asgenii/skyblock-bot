import pytest, sys, os
from pathlib import Path

sys.path.append(os.path.abspath('../src'))

from skyblock.auction import background

@pytest.mark.asyncio
async def test_background_filters_ended_auctions(monkeypatch):
    async def fake_apicooldown(url):
        return {
            "auctions": [
                {
                    "auction": {
                        "uuid": "auc1",
                        "end": 1,
                        "claimed": False,
                        "item_name": "TestItem",
                        "highest_bid_amount": 123
                    }
                },
                {
                    "auction": {
                        "uuid": "auc2",
                        "end": 9999999999999,
                        "claimed": False,
                        "item_name": "NotEnded",
                        "highest_bid_amount": 50
                    }
                }
            ]
        }

    monkeypatch.setattr(background, "apicooldown", fake_apicooldown)

    notified = set()
    result = await background.main("fake_api", "fake_uuid", notified)
    assert "auc1" in result
    assert result["auc1"]["item"] == "TestItem"
    assert "auc2" not in result
