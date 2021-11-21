from webserver import keep_alive
from asyncio import tasks
import asyncio
import random
from time import sleep
import datetime
import discord
from PIL import Image, ImageFont, ImageDraw
from discord import *
import os
import json
import sys
import platform
from discord import client
from discord.ext import commands
from discord.ext import commands, tasks
from discord_components import *
from config import acces

intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.bans = True

client = discord.Client()
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='m!', intents=intents)
client.remove_command('help')

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
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
    await client.change_presence(activity=discord.Game(random.choice(statuses)))


# Код в этом даже выполняется, когда бот готов  

@client.command()
async def load(ctx, extension):
    user = ctx.author.id
    if user in acces:
        client.load_extension(f'cogs.{extension}') #загружает расширение
        await ctx.send(f'Loaded "{extension}"')
        return
    else:
        return

@client.command()
async def unload(ctx, extension):
    user = ctx.author.id
    if user in acces:
        client.unload_extension(f'cogs.{extension}') # выгружает расширение
        await ctx.send(f'Unloaded "{extension}"')
        return
    else:
        return


for filename in os.listdir('./cogs'): # загружает все файлы (* .py)
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}') # загружает файл без ".py", например: cogs.ping

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
        f"Написал {executedCommand} команду в {ctx.guild.name} (Guild ID: {ctx.message.guild.id}) написал {ctx.message.author} (Author ID: {ctx.message.author.id}) (Канал: {ctx.channel.name})")

#Остальные команды 


@client.command() #пинг бота 
async def ping(ctx):
    embed: discord.Embed = discord.Embed(
        title="🏓 Понг!", description=f"<a:ping_signal:881200232052965388> Мой пинг {round(client.latency * 1000)}мс.", color=discord.Color.purple()
    )
    embed.set_author(name="")
    embed.add_field(name="Есть проблемы? Сервер тех. поддержки", value="[(тык-тык)](https://discord.gg/ZVA59cZmM7)", inline=True)

    await ctx.send(embed=embed)

@client.command() #Команда хелп
async def help3(ctx): 
    embed = discord.Embed(
        title="<:rules:841294551066476564>` Версия бота!` `1.7`",
        description="**`-` Стандартные команды** \n • `m!automemes <id channel>` - Подключение автопубликации мемов на канал \n • `m!meme` - Присылает рандомный мем \n • `m!ping` - Показывает пинг бота \n • `m!bug - m!idea`  бага-идеи на тех. сервер \n • `m!links` - Полезные ссылки \n • `m!avatar` - показывает аватар участника \n • `m!jack <Текст>` - жак фреско \n \n `-` **Премиум команды** \n • `m!bonus` -  Премиум подписка на бота \n • `m!piar` - Информация о заказе рекламы \n \n `-` **Команды для разработчика** \n • `m!blacklist` - добавляет участника в черный список бота \n • `m!shotdown` - экстренное отключение бота \n • `m!say` - сказать от имени бота \n • `m!embed` - сказать от имени бота в эмбеде",
        colour = discord.Colour.from_rgb(255, 140, 0)
    )
    await ctx.send(embed=embed)

#avatar command
@client.command()
async def avatar(ctx, member: discord.Member=None):
  if member == None:
    member = ctx.author
  
  
  icon_url = member.avatar_url

  avatarEmbed = discord.Embed(title = f"{member.name}\'s аватар")
  avatarEmbed.set_image(url = f"{icon_url}")
  await ctx.send(embed = avatarEmbed)


@client.command()
async def jack(ctx, *, text = "Вы не чего не написали."):

    img = Image.open("jack.png")

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Nunito-Regular.ttf", 60)

    draw.text((60,120), text, (0, 0, 0), font=font)

    img.save("text.png")

    await ctx.send(file = discord.File("text.png"))

#Тестовые команды

b = [
    [
        Button(style=ButtonStyle.grey, label='Забанить'),
        Button(style=ButtonStyle.grey, label='Кикнуть'),
        Button(style=ButtonStyle.grey, label='Закрыть'),
    ],
]
b_ban = [
    [
        Button(style=ButtonStyle.green,disabled=True, label='Забанить'),
        Button(style=ButtonStyle.grey,disabled=True, label='Кикнуть'),
        Button(style=ButtonStyle.grey,disabled=True, label='Закрыть'),
    ],
]
b_kick = [
    [
        Button(style=ButtonStyle.grey,disabled=True, label='Забанить'),
        Button(style=ButtonStyle.green,disabled=True, label='Кикнуть'),
        Button(style=ButtonStyle.grey,disabled=True, label='Закрыть'),
    ],
]
b_exit = [
    [
        Button(style=ButtonStyle.grey,disabled=True, label='Забанить'),
        Button(style=ButtonStyle.grey,disabled=True, label='Кикнуть'),
        Button(style=ButtonStyle.green,disabled=True, label='Закрыть'),
    ],
]
 
@client.command()
@commands.has_permissions(administrator = True)
async def console(ctx, user : discord.Member):
    m = await ctx.send(content='Подождите...')
    delta = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
    e = discord.Embed(title=f'Выберите действие', description=f"Пользователь {user}",timestamp=datetime.datetime.utcnow())
    await m.edit(content='',components=b, embed=e)
    while m.created_at < delta:
        res = await client.wait_for('button_click')
        if res.author.id == ctx.author.id and res.message.embeds[0].timestamp < delta:
            if res.component.label == 'Закрыть':
                f = discord.Embed(title=f'Успешно!', description=f'Команда закрыта.',
                                    timestamp=datetime.datetime.utcnow())
                await res.respond(content='',embed=f,components=b_exit, type=7)
                break
            elif res.component.label == 'Забанить':
                f = discord.Embed(title=f'Успешно!', description=f'Пользователь {user} был забанен.',
                                    timestamp=datetime.datetime.utcnow())
                await res.respond(content='',embed=f, components=b_ban, type=7)
                await user.ban(reason=f"Забанен пользователем {ctx.author}")
                break
            elif res.component.label == 'Кикнуть':
                f = discord.Embed(title=f'Успешно!', description=f"Пользователь {user} был кикнут.",timestamp=datetime.datetime.utcnow())
                await res.respond(content='',embed=f, components=b_kick, type=7)
                await user.kick(reason=f"Кикнут пользователем {ctx.author}")
                break
            else:
                f = discord.Embed(title=f'Выберите действие', description=f'Пользователь {user}',timestamp=datetime.datetime.utcnow())
                await res.respond(content='', embed=f, components=b, type=7)

@client.command()
async def server(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)
  
  id = str(ctx.guild.id)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + "\n📚Информация сервера",
      description=description,
      color=discord.Color.purple()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="👑 | Овнер", value=str(ctx.guild.owner.mention), inline=False)
  embed.add_field(name="🆔 | Сервер ID", value=id, inline=False)
  embed.add_field(name="🌎 | Регион", value=f"{ctx.guild.region}".replace("Russia", "").replace("Europe", ""), inline=False)
  embed.add_field(name="😀 | Участников", value=memberCount, inline=False)
  embed.add_field(name="🔰 | Уровень защиты", value=f"{ctx.guild.verification_level}".replace("very_high", "Очень высокий").replace("high", "Высокий").replace("medium", "Средний").replace("low", "Низкий").replace("None", "Отсутствует"), inline=False) 
  embed.add_field(name="🏮 | Категорий", value=ctx.guild.categories.count, inline=False)
  embed.add_field(name="🏮 | Каналов", value=ctx.guild.channels.count, inline=False)
  embed.add_field(name="🏮 | Текстовых каналов", value=ctx.guild.text_channels.count, inline=False)
  embed.add_field(name="🏮 | Войс каналов", value=ctx.guild.voice_channels.count, inline=False)


  time = datetime.datetime.utcnow()
  embed.set_footer(text = time, icon_url = "https://images-ext-2.discordapp.net/external/LhmmB4OwWHYfNiB3wwXptPXaKBGX42p1ctaZD24xKjY/https/media.discordapp.net/attachments/809379533572145193/840469160857436162/monica2Bseggos.gif")
  await ctx.send(embed=embed)

@client.command()
async def userinfo(ctx,user: discord.Member):
  #roles = [role for fole in user.roles]

  embed=discord.Embed(color=0xFFFFFF,timestamp=ctx.message.created_at)

  embed.set_author(name=f"Юзер инфо - {user}")
  embed.set_thumbnail(url=user.avatar_url)
  embed.set_footer(text=f"Команда написана {ctx.author}",icon_url=ctx.author.avatar_url)

  embed.add_field(name="Ник на сервере", value=user.display_name, inline=True)
  embed.add_field(name="Ник и тег", value=f"{user.name}#{user.discriminator}")
  embed.add_field(name="Айди", value=user.id, inline=True)

  embed.add_field(name="Зашел на сервер", value=user.joined_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"), inline=True)
  embed.add_field(name="Аккаунт создан", value=user.created_at.strftime("%a, %#d, %B, %Y, %I:%M %p UTC"), inline=True)

  await ctx.reply(embed=embed,mention_author=False)

@client.command()                                                              
async def user(ctx, *, user: discord.User = None): # b'\xfc'
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)                                    
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)



@client.command()
async def info(ctx,member:discord.Member = None, guild: discord.Guild = None):
    await ctx.message.delete()
    if member == None:
        emb = discord.Embed(title="Информация о пользователе", color=ctx.message.author.color)
        emb.add_field(name="Имя:", value=ctx.message.author.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=ctx.message.author.id,inline=False)
        t = ctx.message.author.status
        if t == discord.Status.online:
            d = "<:on:886277431105826876> В сети"

        t = ctx.message.author.status
        if t == discord.Status.offline:
            d = "<:off:886277434717126676> Не в сети"

        t = ctx.message.author.status
        if t == discord.Status.idle:
            d = "<:notactive:886277436591984761> Не активен"

        t = ctx.message.author.status
        if t == discord.Status.dnd:
            d = "<:idle:886277429952393286> Не беспокоить"

        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=ctx.message.author.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{ctx.message.author.top_role}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="Информация о пользователе", color=member.color)
        emb.add_field(name="Имя:", value=member.display_name,inline=False)
        emb.add_field(name="Айди пользователя:", value=member.id,inline=False)
        t = member.status
        if t == discord.Status.online:
            d = "<:on:886277431105826876> В сети"

        t = member.status
        if t == discord.Status.offline:
            d = "<:off:886277434717126676> Не в сети"

        t = member.status
        if t == discord.Status.idle:
            d = "<:notactive:886277436591984761> Не активен"

        t = member.status
        if t == discord.Status.dnd:
            d = "<:idle:886277429952393286> Не беспокоить"
        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=member.activity,inline=False)
        emb.add_field(name="Роль на сервере:", value=f"{member.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        
        await ctx.send(embed = emb)

@client.command()
async def help(ctx):
    colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]
    contents = [
    discord.Embed(title='📋 Стандартные команды ',description= '• `m!ping` - Показывает пинг бота \n • `m!bug - m!idea`  бага-идеи на тех. сервер \n • `m!links` - Полезные ссылки \n • `m!avatar` - показывает аватар участника \n • `m!info, m!server, m!user` - ифно сервера и участника \n • `m!about` - информация в боте '
f'''
\n Страница [1/5] • Пригласить бота на сервер m!links    
''',color = random.choice(colors)),
    discord.Embed(title='🛡 Модерирование ',description='• `m!console <ник участника>` - бан или кик участника'
f'''
\nСтраница [2/5] • Пригласить бота на сервер m!links
''',color = random.choice(colors)),
    discord.Embed(title='😁 Веселости ',description='• `m!automemes <id channel>` - Подключение автопубликации мемов на канал \n • `m!meme` - Присылает рандомный мем \n • `m!jack <Текст>` - жак фреско \n • `m!nsfw` - NSFW команды'
f'''
\n Страница [3/5] • Пригласить бота на сервер m!links
''',color = random.choice(colors)),
    discord.Embed(title='💎 Премиум команды ',description='• `m!bonus` -  Премиум подписка на бота \n • `m!piar` - Информация о заказе рекламы'
f'''
\n Страница [4/5] • Пригласить бота на сервер m!links
''',color = random.choice(colors)),
    discord.Embed(title='🎫 Команды разработчика ',description='• `m!blacklist <add-remove>` - добавляет участника в черный список бота \n • `m!shotdown` - экстренное отключение бота \n • `m!say` - сказать от имени бота \n • `m!embed` - сказать от имени бота в эмбеде'
'''
\n Страница [5/5] • Пригласить бота на сервер m!links
''',color = random.choice(colors))
]

    pages = 5
    cur_page = 1
    message = await ctx.send(embed=contents[cur_page - 1])

    await message.add_reaction("<:left:888455111284756541>")
    await message.add_reaction("<:right:888455108906582046>")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["<:left:888455111284756541>", "<:right:888455108906582046>"]

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", check=check)

            if str(reaction.emoji) == "<:right:888455108906582046>" and cur_page != pages:
                cur_page += 1
                await message.edit(embed=contents[cur_page - 1])
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "<:left:888455111284756541>" and cur_page > 1:
                cur_page -= 1
                await message.edit(embed=contents[cur_page - 1])
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)

        except:
            break

keep_alive()
client.run(os.getenv("ODM4Nzc2ODkxODA4NDE1ODQ0.YJAB2g.UY6L9pO2Tbt1dGBgcaQseKBMnXk"))