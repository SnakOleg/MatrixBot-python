import json
import os
import sys

import discord
from discord import client
from discord.ext import commands

from helpers import json_manager


if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)


class owner(commands.Cog, name="owner"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="shutdown")
    async def shutdown(self, context):
        """
        Отключение бота
        """
        if context.message.author.id in config["owners"]:
            embed = discord.Embed(
                description="Выключение. Пока! :wave:",
                color=0x42F56C
            )
            await context.send(embed=embed)
            await self.bot.close()
        else:
            embed = discord.Embed(
                title="Denied!",
                description="У вас недостаточно прав чтоб использовать эту команду.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @commands.command(name="say", aliases=["echo"])
    async def say(self, context, *, args):
        """
        Бот скажет все, что угодно.
        """
        if context.message.author.id in config["owners"]:
            await context.send(args)
        else:
            embed = discord.Embed(
                title="Denied!",
                description="У вас недостаточно прав чтоб использовать эту команду.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @commands.command(name="embed")
    async def embed(self, context, *, args):
        """
        Бот скажет все, что вы хотите, но в эмбеде.
        """
        if context.message.author.id in config["owners"]:
            embed = discord.Embed(
                description=args,
                color=0x42F56C
            )
            await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Denied!",
                description="У вас недостаточно прав чтоб использовать эту команду.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @commands.group(name="blacklist")
    async def blacklist(self, context):
        """
        Позволяет добавить или удалить пользователя, который не может использовать бот.
        """
        if context.invoked_subcommand is None:
            with open("blacklist.json") as file:
                blacklist = json.load(file)
            embed = discord.Embed(
                title=f"В настоящее время есть {len(blacklist['ids'])} внесенные в черный список идентификаторы",
                description=f"{', '.join(str(id) for id in blacklist['ids'])}",
                color=0x0000FF
            )
            await context.send(embed=embed)

    @blacklist.command(name="add")
    async def blacklist_add(self, context, member: discord.Member):
        """
        Позволяет добавить пользователя, который не может использовать бот.
        """
        if context.message.author.id in config["owners"]:
            userID = member.id
            try:
                with open("blacklist.json") as file:
                    blacklist = json.load(file)
                if (userID in blacklist['ids']):
                    embed = discord.Embed(
                        title="Denied!",
                        description=f"**{member.name}** Юзер уже в черном списке.",
                        color=0xE02B2B
                    )
                    await context.send(embed=embed)
                    return
                json_manager.add_user_to_blacklist(userID)
                embed = discord.Embed(
                    title="Юзер в черном списке!",
                    description=f"**{member.name}** успешно добавлен в черный список",
                    color=0x42F56C
                )
                with open("blacklist.json") as file:
                    blacklist = json.load(file)
                embed.set_footer(
                    text=f"Есть сейчас {len(blacklist['ids'])} пользователи в черном списке"
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Denied!",
                    description=f"Произошла неизвестная ошибка при попытке добавить **{member.name}** в черный список.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Denied!",
                description="У вас недостаточно прав чтоб использовать эту команду.",
                color=0xE02B2B
            )
            await context.send(embed=embed)

    @blacklist.command(name="remove")
    async def blacklist_remove(self, context, member: discord.Member = None):
        """
        Позволяет удалить пользователя, который не может использовать бот.
        """
        if context.message.author.id in config["owners"]:
            userID = member.id
            try:
                json_manager.remove_user_from_blacklist(userID)
                embed = discord.Embed(
                    title="Юзер удален с черного списка",
                    description=f"**{member.name}** был успешно удален из черного списка",
                    color=0x42F56C
                )
                with open("blacklist.json") as file:
                    blacklist = json.load(file)
                embed.set_footer(
                    text=f"Есть сейчас {len(blacklist['ids'])} пользователи в черном списке"
                )
                await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Denied!",
                    description=f"**{member.name}** нет в черном списке.",
                    color=0xE02B2B
                )
                await context.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Denied!",
                description=" У вас недостаточно прав чтоб использовать эту команду.",
                color=0xE02B2B
            )
            await context.send(embed=embed)


def setup(bot):
    bot.add_cog(owner(bot))
