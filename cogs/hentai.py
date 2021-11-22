import discord
from discord.ext import commands
import json
import random
import sqlite3
from config import piar

url = []
with open('url.json', 'r') as f: #открыли файл с данными
    url = json.load(f)


class Hentai(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ahageo(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["ahageo"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Ahageo**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def anal(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["anal"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Anal**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)

        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def angel(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["angel"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Angel**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)
        
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def bdsm(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["bdsm"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Bdsm**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def bigass(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["bigass"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Big ass**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def bigtits(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["bigtits"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Big tits**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def bikini(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["bikini"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Bikini**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def demon(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["demon"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Demon**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def elves(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["elves"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Elves**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def furry(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["furry"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Furry**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def mastur(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["mastur"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Mastur**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def monster(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["monster"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Monster**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def neko(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["neko"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Neko**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def police(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["police"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Police**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def pussy(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["pussy"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Pussy**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def smalltits(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["smalltits"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Small tits**', color = 0x0696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def sport(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["sport"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Sport**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def tentacles(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["tentacles"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Tentacles**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0x52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def titsjob(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["titsjob"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Tits job**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0x52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)
    
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def uri(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["uri"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Yuri**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0x52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def yaoy(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["yaoy"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Yaoi**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0x52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            await ctx.send(embed = embed)

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def stocking(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["stocking"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Hose**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0x52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)
        
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def hmaid(self, ctx):
        if ctx.channel.is_nsfw():
            r = url["maid"]
            result = random.choice(r)
            emb = discord.Embed (title = '**Maid**', color = 0x696969)
            emb.set_image(url = result)
            def check_gold(guild):
                a = None
                with sqlite3.connect('base.db') as bd:
                    cur = bd.cursor()
                    cur.execute('SELECT status FROM gold WHERE guild_id = "{}"'.format(guild))
                    for result in cur:
                        a = result[0]
                    return a
            result_gold = check_gold(ctx.message.guild.id)
            chance = [1, 2]
            result_chance = random.choice(chance)
            if result_chance == 1 and result_gold != 1:
                emb.set_footer(text=f'{piar}')
            await ctx.send(embed = emb)
        else:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0x52A2A)
            embed.description = 'Данная команда предназначена только для **NSFW** каналов!'
            embed.set_footer(text= 'Error: 005')
            await ctx.send(embed = embed)



def setup(client):
    client.add_cog(Hentai(client))
