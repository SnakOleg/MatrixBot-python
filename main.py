import os
import discord
from asyncio import sleep
from discord.ext import commands
from asyncio import tasks
import asyncio
import random
from time import sleep
import datetime
from PIL import Image, ImageFont, ImageDraw
import json
import sys
import platform
from discord import client
from discord.ext import commands
from discord.ext import commands, tasks
from config import acces
from discord_components import *
from discord_components import DiscordComponents, Button, ButtonStyle
from Cybernator import Paginator as pag
from discord_buttons_plugin import *

intents = discord.Intents.default()
intents.members = True
intents.all()

client = discord.Client()
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='m!', intents=intents)
client.remove_command('help')
buttons = ButtonsClient(client)

if not os.path.isfile("config.json"):
    sys.exit("'config.json 'не найден! Пожалуйста, добавьте его и попробуйте еще раз.")
else:
    with open("config.json") as file:
        config = json.load(file)

# Setup the game status task of the client


@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")
    print(f"Discord.py API version: {discord.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")
    DiscordComponents(client)
    status_task.start()


@tasks.loop(minutes=1.0)
async def status_task():
    statuses = ["Лисички🦊", f"{config['bot_prefix']}help", "Made by Snak#0017"]
    await client.change_presence(activity=discord.Game(random.choice(statuses))
                                 )


# Код в этом даже выполняется, когда бот готов


@client.command()
async def load(ctx, extension):
    user = ctx.author.id
    if user in acces:
        client.load_extension(f'cogs.{extension}')  #загружает расширение
        await ctx.send(f'Loaded "{extension}"')
        return
    else:
        return


@client.command()
async def unload(ctx, extension):
    user = ctx.author.id
    if user in acces:
        client.unload_extension(f'cogs.{extension}')  # выгружает расширение
        await ctx.send(f'Unloaded "{extension}"')
        return
    else:
        return


for filename in os.listdir('./cogs'):  # загружает все файлы (* .py)
    if filename.endswith('.py'):
        client.load_extension(
            f'cogs.{filename[:-3]}'
        )  # загружает файл без ".py", например: cogs.ping


@client.event
async def on_message(message):
    # Игнорирует выполнение команды ботом или самим ботом
    if message.author == client.user or message.author.bot:
        return
    # Игнорирует, если команда выполняется пользователем из черного списка
    with open("blacklist.json") as file:
        blacklist = json.load(file)
    if message.author.id in blacklist["ids"]:
        return
    await client.process_commands(message)


@client.event
async def on_command_completion(ctx):
    fullCommandName = ctx.command.qualified_name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])
    print(
        f"Написал {executedCommand} команду в {ctx.guild.name} (Guild ID: {ctx.message.guild.id}) написал {ctx.message.author} (Author ID: {ctx.message.author.id}) (Канал: {ctx.channel.name})"
    )


#Остальные команды


@client.command()  #пинг бота
async def ping(ctx):
    embed: discord.Embed = discord.Embed(
        title="🏓 Понг!",
        description=
        f"<a:ping_signal:881200232052965388> Мой пинг {round(client.latency * 1000)}мс.",
        color=discord.Color.purple())
    embed.set_author(name="")
    embed.add_field(name="Есть проблемы? Сервер тех. поддержки",
                    value="[(тык-тык)](https://discord.gg/ZVA59cZmM7)",
                    inline=True)

    await ctx.send(embed=embed)


#avatar command
@client.command()
async def avatar(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    icon_url = member.avatar_url

    avatarEmbed = discord.Embed(title=f"{member.name}\'s аватар")
    avatarEmbed.set_image(url=f"{icon_url}")
    await ctx.send(embed=avatarEmbed)


@client.command()
async def jack(ctx, *, text="Вы не чего не написали."):

    img = Image.open("jack.png")

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Nunito-Regular.ttf", 60)

    draw.text((60, 120), text, (0, 0, 0), font=font)

    img.save("text.png")

    await ctx.send(file=discord.File("text.png"))


#Тестовые команды

@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title=name + "\n📚Информация сервера",
                          description=description,
                          color=discord.Color.purple())
    embed.set_thumbnail(url=icon)
    embed.add_field(name="👑 | Овнер",
                    value=str(ctx.guild.owner.mention),
                    inline=False)
    embed.add_field(name="🆔 | Сервер ID", value=id, inline=False)
    embed.add_field(name="🌎 | Регион",
                    value=f"{ctx.guild.region}".replace("Russia", "").replace(
                        "Europe", ""),
                    inline=False)
    embed.add_field(name="😀 | Участников", value=memberCount, inline=False)
    embed.add_field(name="🔰 | Уровень защиты",
                    value=f"{ctx.guild.verification_level}".replace(
                        "very_high",
                        "Очень высокий").replace("high", "Высокий").replace(
                            "medium",
                            "Средний").replace("low", "Низкий").replace(
                                "None", "Отсутствует"),
                    inline=False)

    time = datetime.datetime.utcnow()
    embed.set_footer(
        text=time,
        icon_url=
        "https://images-ext-2.discordapp.net/external/LhmmB4OwWHYfNiB3wwXptPXaKBGX42p1ctaZD24xKjY/https/media.discordapp.net/attachments/809379533572145193/840469160857436162/monica2Bseggos.gif"
    )
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed1 = discord.Embed(
        title="📋 Стандартные команды",
        description=
        '• `m!ping` - Показывает пинг бота \n • `m!bug - m!idea` - отправка бага-идеи на тех. сервер \n • `m!links` - Полезные ссылки \n • `m!avatar` - показывает аватар участника \n • `m!about` - информация в боте '
    )
    embed2 = discord.Embed(
        title="🛡 Модерирование",
        description='• `m!console <ник участника>` - бан или кик участника')
    embed3 = discord.Embed(
        title="😁 Веселости",
        description=
        '• `m!automemes <id channel>` - Подключение автопубликации мемов на канал \n • `m!meme` - Присылает рандомный мем \n • `m!jack <Текст>` - жак фреско \n • `m!nsfw` - NSFW команды'
    )
    embed4 = discord.Embed(
        title="💎 Премиум команды",
        description=
        '• `m!bonus` -  Премиум подписка на бота \n • `m!piar` - Информация о заказе рекламы'
    )
    embed5 = discord.Embed(
        title="🎫 Команды разработчика",
        description=
        '• `m!blacklist <add-remove>` - добавляет участника в черный список бота \n • `m!shotdown` - экстренное отключение бота \n • `m!say` - сказать от имени бота \n • `m!embed` - сказать от имени бота в эмбеде'
    )

    embeds = [embed1, embed2, embed3, embed4, embed5]

    message = await ctx.send(embed=embed1)
    page = pag(client, message, only=ctx.author, color=0xF76C12, embeds=embeds)
    await page.start()


@client.command()
async def secretinvite(ctx):
	embed = discord.Embed(title=f"Инвайт {client.user.name}", color=0x4a16b9, description=f"Хочешь пригласить? {client.user.name}, тогда [кликни сюда](https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=536868679031&scope=bot)")
	await buttons.send(
		content = None,
		embed = embed,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					style = ButtonType().Link,
					label = "Инвайт",
					url = f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=536868679031&scope=bot"
				)
			])
		]
	)


@buttons.click
async def hibutton(ctx):
	await ctx.reply(f"Привет {ctx.member.name}")

@buttons.click
async def clickbutton(ctx):
	await ctx.reply(f"{ctx.member.name} Нажал на кнопку.")

@buttons.click
async def danger(ctx):
	await ctx.reply(f"{ctx.member}, Сказал не кликать!")

@buttons.click
async def lol(ctx):
	await ctx.reply("Лол")

@client.command()
async def hi(ctx):
	await buttons.send(
		content="Привет",
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(

					style = ButtonType().Primary,
					label = "Привет",
					custom_id = "hibutton",

				),

				Button(
					style = ButtonType().Success,
					label = "Клик",
					custom_id = "clickbutton"

				),
				Button(
					style = ButtonType().Danger,
					label = "Не кликай",
					custom_id = "danger",
				),
				Button(
					style = ButtonType().Secondary,
					label = "Привет",
					custom_id = "lol",
				)
			])
		]
	)


 


client.run("")
