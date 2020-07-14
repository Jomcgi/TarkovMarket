from pyppeteer.errors import TimeoutError
from pyppeteer.page import Page
from src import globals

async def does_item_exist(page: Page, item_name: str):
    try:
        if not item_name:
            return False

        await page.waitForXPath(f"//span[contains(text(),'{item_name}')]", options={"timeout": 3000})
        return True
    except TimeoutError:
        return False

async def get_text_from_selector(selector: str):
    page = globals.page
    element = await page.querySelector(selector)
    if not element:
        return ""

    text = await page.evaluate(
        "(element) => element.textContent", element
    )

    return text.strip(' \n\r')