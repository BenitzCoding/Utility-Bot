import os
import aiohttp

from discord import Object

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

async def sync_application(self):
    CORE_GUILD = Object(id = int(get_env("CORE_GUILD")))
    TRAINING_GUILD = Object(id = int(get_env("TRAINING_GUILD")))
    await self.tree.sync()
    await self.tree.sync(guild = CORE_GUILD)
    await self.tree.sync(guild = TRAINING_GUILD)

def get_env(constant: str) -> str:
    load_dotenv(find_dotenv())
    return os.getenv(constant)