from termcolor import colored

from src.pyppeteer import get_text_from_selector


async def print_item_info(item_name: str):
    main_price_text = await get_text_from_selector("span.price-main")
    price_per_slot_text = await get_text_from_selector("span.price-sec")
    if not price_per_slot_text:
        price_per_slot_text = main_price_text

    price_per_slot = parse_price_to_int(price_per_slot_text)

    if price_per_slot > 50000:
        print_item_prices(main_price_text, price_per_slot_text, "cyan")
    elif price_per_slot > 25000:
        print_item_prices(main_price_text, price_per_slot_text, "green")
    elif price_per_slot > 10000:
        print_item_prices(main_price_text, price_per_slot_text, "yellow")
    else:
        print_item_prices(main_price_text, price_per_slot_text, "red")


def parse_price_to_int(price: str) -> int:
    return int(price.replace("₽", "").replace(",",""))


def print_item_prices(main_price_text: str, price_per_slot_text: str, color: str):
    print(colored(f"Price is: {main_price_text}", color))
    print(colored(f"Price per slot: {price_per_slot_text}", color))

