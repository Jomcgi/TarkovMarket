import src.globals as globals
from src.img_processing import run
import os
# make directory for storing images if it does not exist in path
from src.item_output import print_item_info
from src.pyppeteer import does_item_exist

if not os.path.exists("images"):
    os.makedirs("images")


async def fetch_price():
    page = globals.page
    search_bar = await page.querySelector('.search input[type="text"]')
    item_name = run()
    print(f"Item name: {item_name}")

    await page.evaluate("""
    () => { const input = document.querySelector('.search input[type="text"]');
    input.value = '';
    }""")
    await search_bar.type(item_name)
    if not await does_item_exist(page, item_name):
        print(f"Could not find item: {item_name}")
        return

    await print_item_info(item_name)

