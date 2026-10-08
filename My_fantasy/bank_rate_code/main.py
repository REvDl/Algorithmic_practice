import time
import httpx
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict, SecretStr
import json
import logging
import aiofiles
import asyncio


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

class Settings(BaseSettings):
    FILE_NAME: str = "database.json1"
    BANK_API: str = "https://fake-bank-api.com"
    TOKEN: SecretStr
    CHAT_ID: int

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent / ".env"
    )

settings = Settings()


async def save_to_json(rate: float, path: str) -> None:
    record = {"timestamp": time.time(), "rate": rate}
    async with aiofiles.open(path, "a", encoding="utf-8") as f:
        await f.write(json.dumps(record) + "\n")




async def notify(client: httpx.AsyncClient, message: str, user_to_send: int) -> None:
    url = f"https://api.telegram.org/bot{settings.TOKEN.get_secret_value()}/sendMessage"
    response = await client.post(url, json={"chat_id": user_to_send, "text": message})
    response.raise_for_status()




async def fetch_rate(client: httpx.AsyncClient) -> float | None:
    try:
        response = await client.get(settings.BANK_API)
        response.raise_for_status()
        data = response.json()
        rate = data["price"]
        logger.info("Course received: %s", rate)
        return float(rate)
    except httpx.HTTPError as e:
        logger.error("HTTP error occurred while fetching rate: %s", e)
        return None
    except KeyError:
        logger.error("Key not found, check the structure of the bank's response")
        return None
    except Exception as e:
        logger.exception("Unexpected error occurred while parsing bank response: %s", e)
        return None





async def run_everything(client: httpx.AsyncClient) -> None:
    rate = await fetch_rate(client)
    if rate is None:
        logger.warning("Rate unavailable, skipping this cycle")
        return
    await save_to_json(rate, settings.FILE_NAME)
    try:
        await notify(client, f"Rate USD: {rate}", settings.CHAT_ID)
    except httpx.HTTPError:
        logger.exception("Failed to send Telegram message")


async def main() -> None:
    async with httpx.AsyncClient(timeout=10) as client:
        while True:
            await run_everything(client)
            await asyncio.sleep(60)



if __name__ == "__main__":
    asyncio.run(main())
