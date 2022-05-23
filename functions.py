import os
import aiohttp

from dotenv import load_dotenv, find_dotenv

async def validate_user(user: int) -> bool:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.senarc.org/token/has-token/{user}") as response:
            if response.status == 200:
                data = await response.json()
                
                if data["has_token"]:
                    return True

                else:
                    return False

            else:
                return False

def get_env(constant: str) -> str:
    load_dotenv(find_dotenv())
    return os.getenv(constant)