import discord
from discord.ext import commands
from datetime import datetime
import pytz
from string import Template
import sqlite3
from config import acces

class Prem(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gold(self, ctx, id : int):
        user = ctx.author.id
        if user not in acces:
            return

        def first2(s):
            return s[:2]
        def end2(s):
            return s[3:]
        def add(id, date):
            status = 1
            with  sqlite3.connect('base.db') as bd:
                cur = bd.cursor()
                cur.execute('INSERT INTO gold(guild_id, status, date) VALUES("{}", "{}", "{}")'.format(id, status, date))

        moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
        time = moscow_time.strftime('%d.%m')
        a = time
        b = first2(a)
        c = int(b)
        v = c + 30
        if v > 30:
            v -= 30
            result_day = v
            r = end2(a)
            f = int(r)
            result_month = f + 1
            result = f'0{result_day}.0{result_month}'
        add(id, result)
        embed = discord.Embed(color = 0xFFFAFA)
        embed.description = '👌'
        await ctx.send(embed = embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed (title = f'🔔 **Ошибка.**', color = 0xA52A2A)
            embed.description = f'**Пропущены** аргументы команды!'
            embed.set_footer(text= 'Error: 003')
            await ctx.send(embed = embed)
            return
        if isinstance(error, commands.CommandOnCooldown):
            i = int(error.retry_after)
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Бот имеет **задержку**, пожалуйста, подождите {} сек.'.format(i)
            embed.set_footer(text= 'Error: 004')
            await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Prem(client))