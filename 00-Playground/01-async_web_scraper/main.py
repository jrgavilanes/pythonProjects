import asyncio
import datetime

import httpx
from colorama import Fore


async def get_html(url: str) -> str:
    print(Fore.YELLOW + f"Getting HTML for url {url}", flush=True)

    async with httpx.AsyncClient(timeout=None) as client:
        try:
            resp = await client.get(url, follow_redirects=True)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            print(Fore.RED + f"{url}: {e=}", flush=True)


def curated_url(url: str) -> str:
    CARACTERS = "abcdefghijklmnopqrstuvwxyz_0123456789"
    result = ""
    for c in url.lower():
        if c in CARACTERS:
            result += c
        else:
            result += "_"
    return result


def save_page(url: str, html: str) -> str:
    url_curated = curated_url(url)
    if html:
        with open(f"downloaded_{url_curated}.txt", "w") as text_file:
            text_file.write(html)
        print(Fore.GREEN + f"saved file {url_curated}", flush=True)
        return f"saved file {url_curated}"

    print(Fore.RED + f"cannot save file {url_curated}", flush=True)
    return f"cannot save file {url_curated}"

    # print(Fore.CYAN + f"Getting TITLE for episode {episode_number}", flush=True)
    # soup = bs4.BeautifulSoup(html, 'html.parser')
    # header = soup.select_one('h1')
    # if not header:
    #     return "MISSING"
    #
    # return header.text.strip()


def main(pages):
    t0 = datetime.datetime.now()
    asyncio.run(get_pages(pages))

    dt = datetime.datetime.now() - t0
    print(f"Done in {dt.total_seconds():.2f} sec.")


async def get_pages(pages: list):
    tasks = []
    for url in pages:
        tasks.append((url, asyncio.create_task(get_html(url))))

    for url, page_content in tasks:
        html = await page_content
        title = save_page(url, html)
        print(Fore.WHITE + f"Proccesed url: {url}", flush=True)


if __name__ == '__main__':
    urls = [f"https://www.meneame.net/{i}" for i in range(1, 10)]
    urls.append("https://www.menexame.net/20")
    main(urls)
