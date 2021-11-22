import discord
from discord.ext import commands

class Other(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 900, commands.BucketType.user)
    async def bug(self, ctx, *, text = None):
        if not ctx.message.author.guild_permissions.administrator:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Для **отправки** бага на тех. сервер у вас должны быть **админ** права!'
            embed.set_footer(text= 'Error: 002')
            await ctx.send(embed = embed)
            return
        elif text == None:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Вы не **описали** баг!'
            embed.set_footer(text= 'Error: 003')
            await ctx.send(embed = embed)
            return
        elif '@everyone' or '@here' in text: # проверка на @everyone/@here и его удаление/замена
            global bi1
            global bi2
            if '@everyone' and '@here' in text:
                bi1 = text.replace('@everyone', ' ')
                bi2 =  bi1.replace('@here', ' ')
                text = bi2
            if '@everyone' in text:
                bi1 = text.replace('@everyone', ' ')
                text = bi1
            if '@here' in text:
                bi2 = text.replace('@here', ' ')
                text = bi2

        channel = self.client.get_channel(int(881123202179411978))
        embed = discord.Embed (title = f'🗣 **Новый баг!**', color = 0xFFFAFA)
        embed.description = f'**О баге:** `{text}`\nДоп. информация:\n||Server name: {ctx.guild.name}\nServer id: {ctx.guild.id}\nUser_nickname: {ctx.author.mention}\nUser_id: {ctx.author.id}||'
        await channel.send(embed = embed)
        emb = discord.Embed(color = 0x696969)
        emb.description = 'Баг отправлен на [тех. сервер](https://discord.gg/ZVA59cZmM7)!'
        await ctx.send(embed = emb)

    @commands.command()
    @commands.cooldown(1, 900, commands.BucketType.user)
    async def idea(self, ctx, *, text = None):
        if not ctx.message.author.guild_permissions.administrator:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Для **отправки** идеи на тех. сервер у вас должны быть **админ** права!'
            embed.set_footer(text= 'Error: 002')
            await ctx.send(embed = embed)
            return
        elif text == None:
            embed = discord.Embed(title = '🔔 Ошибка.', color = 0xA52A2A)
            embed.description = 'Вы не **описали** идею!'
            embed.set_footer(text= 'Error: 003')
            await ctx.send(embed = embed)
            return
        elif '@everyone' or '@here' in text: # проверка на @everyone/@here и его удаление/замена
            global bi1
            global bi2
            if '@everyone' and '@here' in text:
                bi1 = text.replace('@everyone', ' ')
                bi2 =  bi1.replace('@here', ' ')
                text = bi2
            if '@everyone' in text:
                bi1 = text.replace('@everyone', ' ')
                text = bi1
            if '@here' in text:
                bi2 = text.replace('@here', ' ')
                text = bi2

        channel = self.client.get_channel(int(881123202179411978))
        embed = discord.Embed (title = f'🗣 **Новая идея!**', color = 0xFFFAFA)
        embed.description = f'**О идеи:** `{text}`\nДоп. информация:\n||Server name: {ctx.guild.name}\nServer id: {ctx.guild.id}\nUser_nickname: {ctx.author.mention}\nUser_id: {ctx.author.id}||'
        await channel.send(embed = embed)
        emb = discord.Embed(color = 0x696969)
        emb.description = 'Идея отправлена на [тех. сервер](https://discord.gg/ZVA59cZmM7)!'
        await ctx.send(embed = emb)


def setup(client):
    client.add_cog(Other(client))