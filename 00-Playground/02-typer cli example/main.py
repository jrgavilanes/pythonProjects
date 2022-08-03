import asyncio
import time
from pathlib import Path
from typing import List

import httpx
import typer
# from bs4 import BeautifulSoup as Soup
from colorama import Fore

app = typer.Typer()


@app.command()
def download_pages(file: Path, asyn: bool = True):
    if file.is_file():
        urls = []
        with open(file) as f:
            for url in f:
                urls.append(url.strip())

        if len(urls) == 0:
            raise Exception(f"File is empty: {file}")

        if asyn:
            asyncio.run(_download_all(urls))
        else:
            t = time.time()
            for url in urls:
                _download(url)
            print(f"It took {round(time.time() - t, 2)} sec. Total urls: {len(urls)}")
    else:
        raise Exception(f"File {file} is not valid")


async def _download_all(urls: List[str]):
    t1 = time.time()
    await asyncio.gather(*(_download_async(url) for url in urls))
    print(f"It took {round(time.time() - t1, 2)} sec. Total urls: {len(urls)}")


async def _download_async(_url: str):
    async with httpx.AsyncClient(timeout=None) as client:
        try:
            print(Fore.GREEN + f"Downloading {_url} and renaming as 'downloaded_{curated_url(_url)}.txt'", flush=True)
            resp = await client.get(_url.strip(), follow_redirects=True)
            resp.raise_for_status()
            with open(f"downloaded_{curated_url(_url)}.txt", "w") as text_file:
                text_file.write(resp.text)
        except Exception as e:
            print(Fore.RED + f"{_url}: {e=}", flush=True)


def _download(_url: str):
    try:
        print(Fore.GREEN + f"Downloading {_url} and renaming as 'downloaded_{curated_url(_url)}.txt'", flush=True)
        resp = httpx.get(_url.strip(), follow_redirects=True)
        resp.raise_for_status()
        with open(f"downloaded_{curated_url(_url)}.txt", "w") as text_file:
            text_file.write(resp.text)
    except Exception as e:
        print(Fore.RED + f"{_url}: {e=}", flush=True)


@app.command()
def check_file(file: Path, asyn: bool = False, substring: str = None):
    if asyn:
        if file.is_file():
            urls = []
            with open(file) as f:
                for url in f:
                    urls.append(url.strip())
            if len(urls) > 0:
                asyncio.run(_async_check(urls, substring))
            else:
                raise Exception(f"File is empty: {file}")
        else:
            raise Exception(f"File {file} is not valid")
    else:
        if file.is_file():
            start = time.time()
            with open(file) as f:
                for url in f:
                    _check_url(url.strip(), substring)
            print(f"It took {round(time.time() - start, 2)} sec.")
        else:
            print(Fore.RED + f" Sorry, {file} not found!")


@app.command()
def check_urls(urls: List[str], asyn: bool = False, substring: str = None):
    if asyn:
        asyncio.run(_async_check(urls, substring))
    else:
        for url in urls:
            _check_url(url, substring)


@app.command()
def check(url: str, substring: str = None):
    _check_url(url, substring)


def _check_url(url: str, substring: str = None):
    try:
        res = httpx.get(url.strip())
        if 200 <= res.status_code <= 399:
            print("+" * 10)
            print(Fore.GREEN + f" URL: {url} is OK, returns {res.status_code}", flush=True)
            if substring is not None:
                if substring.lower() in res.text.lower():
                    print(
                        Fore.GREEN + f" ---- > URL: {url} DOES contain '{substring}'",
                        flush=True)
                else:
                    print(
                        Fore.RED + f" ---- > URL: {url} DOES NOT contain '{substring}'",
                        flush=True)

        else:
            print("+" * 10)
            print(Fore.RED + f" URL: {url} is KO, returns {res.status_code}", flush=True)
    except Exception as e:
        print(Fore.RED + f" URL: {url} :: {e}", flush=True)


async def _async_check(urls: List[str], substring: str = None):
    async def _check(url: str, substr: str = None):
        await _check_url_async(url, substr)

    start = time.time()
    await asyncio.gather(*(_check(url, substring) for url in urls))
    print(f"It took {round(time.time() - start, 2)} sec.")


async def _check_url_async(url: str, substring: str = None):
    async with httpx.AsyncClient(timeout=None) as client:
        try:
            res = await client.get(url.strip(), follow_redirects=True)
            if 200 <= res.status_code <= 399:
                print("+" * 10)
                print(Fore.GREEN + f" URL: {url} is OK, returns {res.status_code}", flush=True)
                if substring is not None:
                    if substring.lower() in res.text.lower():
                        print(
                            Fore.GREEN + f" ---- > URL: {url} DOES contain '{substring}'",
                            flush=True)
                    else:
                        print(
                            Fore.RED + f" ---- > URL: {url} DOES NOT contain '{substring}'",
                            flush=True)

            else:
                print("+" * 10)
                print(Fore.RED + f" URL: {url} is KO, returns {res.status_code}", flush=True)
        except Exception as e:
            print(Fore.RED + f" URL: {url} :: {e}", flush=True)


def curated_url(url: str) -> str:
    valid_caracters = "abcdefghijklmnopqrstuvwxyz_-0123456789"
    result = ""
    for c in url.lower():
        if c in valid_caracters:
            result += c
        else:
            result += "_"
    return result


if __name__ == "__main__":
    app()
