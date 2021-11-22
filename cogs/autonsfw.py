import discord
from discord.ext import commands
import random
import json
import sqlite3
import asyncio
from datetime import datetime
import pytz
from string import Template
from config import piar


url = []
with open('url.json', 'r') as f: #открыли файл с данными
    url = json.load(f)
timeout = 60 * 60

class Auto(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):    
        channels_m = [] # канала мем
        check_m = [] # проверка мемов

        def check_meme(channels_m):
            with  sqlite3.connect('basensfw.db') as bd:
                cur = bd.cursor()
                cur.execute('SELECT meme FROM auto')
                for result in cur:
                    channels_m.append(result[0])
                return channels_m
        
        def check_time(time):
            a = None
            with  sqlite3.connect('basensfw.db') as bd:
                cur = bd.cursor()
                cur.execute('SELECT date FROM gold WHERE date = "{}"'.format(time))
                for result in cur:
                    a = result[0]
                return a

        def get_server(time):
            a = None
            with  sqlite3.connect('basensfw.db') as bd:
                cur = bd.cursor()
                cur.execute('SELECT guild_id FROM gold WHERE date = "{}"'.format(time))
                for result in cur:
                    a = result[0]
                return a

        def check_gold(guild):
            a = None
            with sqlite3.connect('basensfw.db') as bd:
                cur = bd.cursor()
                cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                for result in cur:
                    a = result[0]
                return a

        def delete(time, delete):
            with  sqlite3.connect('basensfw.db') as bd:
                cur = bd.cursor()
                cur.execute('DELETE from gold where date= "{}"'.format(time))

        def prem():
            moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
            time = moscow_time.strftime('%d.%m')
            result = check_time(time)
            if result != None:
                delete_result = get_server(time)
                delete(time, delete_result)


        await self.client.change_presence(activity = discord.Game('h!help'))
        channels_mem = check_meme(channels_m)
        chance = [1, 2]
        while True:
            prem()
            # начало блока мемов
            meme = url["anal"]
            check_m = check_meme(check_m)
            for element in check_m:
                if element not in channels_mem:
                    channels_mem.append(element)
            for channel_id in channels_mem:
                await self.client.wait_until_ready()
                try:
                    channel = self.client.get_channel(int(channel_id))
                except:
                    pass
                result_gold = check_gold(channel_id)
                result_chance = random.choice(chance)
                result_meme = random.choice(meme)
                ran = result_meme
                emb = discord.Embed (title = '**Auto hentai**', color = 0x000000)
                emb.set_image(url = ran)
                if result_chance == 1 and result_gold != 1:
                    emb.set_footer(text=f'{piar}')
                if channel.is_nsfw():
                    try:
                        await channel.send(embed = emb)
                    except:
                        pass
                else:
                    embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
                    embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
                    embed.set_footer(text= 'Error: 005')
                    await channel.send(embed = embed)
            # конец блока мемов
            await asyncio.sleep(timeout)
    

    @commands.command()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def auto(self, ctx, arg):
        # подключить postgresql или просто добавить перменную bd и подключаться к бд 1 ра

        def add(arg):
            with  sqlite3.connect('basensfw.db') as bd:
                guild_id = ctx.message.guild.id
                user = ctx.message.author.id
                moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
                date = moscow_time.strftime('%d.%m.%y | %H:%M')
                cur = bd.cursor()
                cur.execute('INSERT INTO auto(guild_id, user_id, meme, date) VALUES("{}", "{}", "{}", "{}")'.format(guild_id, user, arg, date))
    
        def change(arg):
            with  sqlite3.connect('basensfw.db') as bd:
                guild_id = ctx.message.guild.id
                cur = bd.cursor()
                cur.execute('UPDATE auto SET meme = {} WHERE guild_id = {}'.format(arg, guild_id))

        status = None
        def check(arg, status):
            guild_id = ctx.message.guild.id
            with  sqlite3.connect('basensfw.db') as bd:
                cur = bd.cursor()
                cur.execute('SELECT meme FROM auto WHERE guild_id = {}'.format(guild_id)) 
                for result in cur:
                    status = result[0]
                return status
        result_meme = check(arg, status)

        members = ctx.guild.member_count
        hentai_list = [None, 'None']

        if len(arg) < 18:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Вы ввели **некоректный** id канала.'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)
            return
        elif arg.isdigit() == False:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Вы ввели **некоректный** id канала.'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)
            return
        elif result_meme != None:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'На сервер нельзя подключить более 1 автопубликации.'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)
            return
        elif members > 10:
            if result_meme in hentai_list:
                add(arg)
            else:
                change(arg)
            embed = discord.Embed(title = '✅ Успешно.', color = 0xFFFAFA)
            embed.description = f'Автопубликация **успешна подключена** участником {ctx.message.author.mention} на канал `{arg}`.'
            await ctx.send(embed = embed)
            return
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xFFFAFA)
            embed.description = 'Для **подключения** автопубликации на вашем сервере должно быть **более 10 участников** или вы можете оформить **золотой доступ** к автопубликации на нашем тех. сервере.[Оформить подписку (кликабельно)](https://discord.gg/ZVA59cZmM7).'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)
            return

def setup(client):
    client.add_cog(Auto(client))