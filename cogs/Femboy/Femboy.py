import discord, asyncio

from discord.ext import commands
from discord import app_commands

class Femboy(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    async def _send(self, channel, user, count):
        for _ in range(count):
            await channel.send(f"{user.mention} 今天女裝了嗎")
            await asyncio.sleep(.2)
        
    @app_commands.command(name = "femboy", description = "royoo 要女裝了嗎~")
    async def femboy_slash(self, interaction: discord.Interaction, channel: discord.TextChannel = None, user: discord.User = None, count: int = 3):
        await interaction.response.defer()
        
        channel = channel or await self.bot.fetch_channel(1311094222656639018)
        user = user or self.bot.get_user(1328156380779118644)
        
        asyncio.create_task(self._send(channel, user, count))
        
        await interaction.followup.send("已開始執行 ✔️", ephemeral=True)
        
async def setup(bot: commands.Bot):
    await bot.add_cog(Femboy(bot))