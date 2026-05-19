import json
import asyncio
import discord

from discord.ext import commands
from discord import app_commands


class HappyMention(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        with open('database/emojis.json', 'r', encoding='utf-8') as f: data = json.load(f)
        self.emojis = data['happymention']

        self.react = app_commands.ContextMenu(name="happymention", callback=self.react_callback)

        self.bot.tree.add_command(self.react)

    async def add_reactions(self, message: discord.Message) -> int:
        added = 0

        try:
            msg = await message.channel.fetch_message(message.id)

            if len(msg.reactions) >= 20: return 0

            for emoji in self.emojis:
                msg = await message.channel.fetch_message(message.id)

                if len(msg.reactions) >= 20: return added

                try:
                    await msg.add_reaction(emoji)
                    added += 1
                    await asyncio.sleep(0.2)

                except discord.HTTPException: continue

        except Exception:
            return 0

        return added

    async def react_callback(self, interaction: discord.Interaction, message: discord.Message):
        await interaction.response.defer(ephemeral=True)

        count = await self.add_reactions(message)
        await interaction.followup.send(f"已添加 {count} 個表情符號", ephemeral=True)

    def cog_unload(self):
        self.bot.tree.remove_command(self.react.name, type=self.react.type)

async def setup(bot):
    await bot.add_cog(HappyMention(bot))