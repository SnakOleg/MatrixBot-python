import datetime
import json
import aiohttp
import discord
from discord.ext import commands
from config import prefix

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def about(self, ctx):
        guild_count = len(self.client.guilds)
        embed = discord.Embed(title="**Matrix Bot**", color= 0x38EFE1)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(name="😀 | Создатель:", value="`Snak#0017`", inline=True)
        embed.add_field(name="😉 | Контрибутор:", value="`S N I P#0001`", inline=True)
        embed.add_field(name="🗃 | Серверов:", value= '`{}`'.format(guild_count), inline=True)
        embed.add_field(name="📚 | Каналов:", value= '`{}`'.format(len(list(self.client.get_all_channels()))), inline=True)
        embed.add_field(name="🎄 | Новый год через:", value= '<t:1640898000>', inline=True)
        embed.add_field(name="🤖 | Бот создан:", value= '<t:1619712960:D>', inline=True)
        embed.set_footer(text="Что-бы отключить автопубликацию мемов обратитесь в тех. поддержку m!links")
        await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def links(self, ctx):
        emb = discord.Embed (title='📢 Пригласи бота к себе на сервер!', color = 0xFFFAFA)
        emb.add_field(name ='Инвайт ссылка на бота:', value = '[Ссылка (тык-тык)](https://discord.com/api/oauth2/authorize?client_id=838776891808415844&permissions=536868679031&scope=bot)', inline= False)
        emb.add_field(name ='Документация:', value = '[Ссылка (тык-тык)](https://docs.matrixbot.ga)', inline= False)
        emb.add_field(name ='Сайт бота:', value = '[Ссылка (тык-тык)](https://matrixbot.ga/)', inline= False)
        emb.add_field(name= 'Сервер тех. поддержки бота:', value= '[Ссылка (тык-тык)](https://discord.gg/ZVA59cZmM7)')
        await ctx.send(embed = emb)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bonus(self, ctx):
        emb = discord.Embed (color = 0xFFD700)
        emb.description = f'**Подключи возможности золотого сервера!**\n```1. Мемы без рекламы!```\n```2. Бонусная роль на тех. сервере!```\n[Приобрести премиум/заказать рекламу в мемах (тык-тык)](https://discord.gg/ZVA59cZmM7) '
        await ctx.send(embed = emb)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def piar(self, ctx):
        emb = discord.Embed (color = 0xEB4747)
        emb.description = f'**Реклама временно не доступна!**'
        await ctx.send(embed = emb)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nsfw(self, ctx):
        emb = discord.Embed (title = ':clipboard: Навигация по командам.', color = 0x000000)
        emb.add_field(name ='Хентай 18+', value = '`bdsm`, `anal`, `ahageo`, `bigass`, `bigtits`, `bikini`, `demon`, `elves`, `furry`, `angel`, `hmaid`, `mastur`, `monster`, `neko`, `police`, `pussy`, `smalltits`, `sport`, `tentacles`, `titsjob`', inline= False)
        emb.add_field(name ='Автопубликация.', value = '`auto`', inline= False)
        emb.description ='**Бот находится в тест режиме! Мы стараемся постепенно улучшать его!**'
        emb.set_footer(text= 'Пригласи меня к себе! m!links')
        await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Help(client))