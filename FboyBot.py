import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix="$")

quotes = ['𝗦𝗢𝗟𝗢 𝗦𝗜 𝗘𝗥𝗘𝗦 𝗩𝗜𝗥𝗚𝗘𝗡 𝗣𝗨𝗘𝗗𝗘𝗦 𝗟𝗘𝗘𝗥 𝗘𝗦𝗧𝗢 𝗘𝗡 𝗡𝗘𝗚𝗥𝗜𝗧𝗔𝗦',
          'Todos los planes cambiaron. Era perro y me amarraron.',
          'Quiero ir al registro civil contigo, para poner esas pompas a mi nombre.',
          'Te amo tanto como las familias mexicanas aman comer pollo asado los Domingos',
          'Contigo queda más que claro que Dios me escuchó. *enviar a todas*',
          'Una platicadita con la ex de tu mejor amigo y se te reinicia la vida',
          'Pásame tu ID de Zoom, quiero verte :heart_eyes:. *enviar a todas*',
          'Es que no necesitamos ser novios, ser novios es solo una etiqueta ok?', 'No te necesito. Te prefiero.',
          '¿Hoy fueron dos personas al espacio? Yo voy y vuelvo a la Luna cada que tú me das un beso.','Ontas?',
          'Es solo una amiga no te preocupes', 'Ya siento que te amo', 'Mirala despidete bien',
          'Mirala bien traviesa', 'Solo te hablo a ti', 'Oh chielos, 3AM']


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Usar $ayuda'))


@client.command(aliases=['kiss'])
async def _kiss(ctx, username):
    await ctx.channel.send(f'{username} https://tenor.com/view/future-diary-mirai-nikki-yuno-yuki-first-gif-6203360')


@client.command(aliases=['compa'])
async def _compa(ctx, username):
    await ctx.channel.send(f'Mi compa el chapulin {username} https://imgur.com/5efzGp3')


@client.command(aliases=['bang'])
async def _bang(ctx):
    await ctx.channel.send('BANG! https://tenor.com/view/yuno-gasai-yuno-anime-future-diary-gun-gif-17876001')

@client.command(aliases=['ayuda'])
async def _ayuda(ctx):
    await ctx.channel.send("Comandos: $fquote, $olvidos, $me besas?, $horny, $compa")


@client.command(aliases=['fquote'])
async def _fquote(ctx):
    await ctx.channel.send(random.choice(quotes))


@client.command(aliases=['olvidos'])
async def _olvidos(ctx):
    await ctx.channel.send('Olvidosssssss 😏')


@client.command(aliases=['beso?'])
async def _beso(ctx):
    await ctx.channel.send('No se besar, me besas? 🥺')


@client.command(aliases=['ontas'])
async def _ontas(ctx):
    await ctx.channel.send('¿Dónde andas mensa? 😈🍆💦🥰👌')


@client.command(aliases=['binario'])
async def _binario(ctx, letter):
    number = ord(letter)
    binary_number = []
    for x in range(8):
        division = number / 2
        slot = number % 2
        slotInt = int(slot)
        number = division
        binary_number.insert(0, slotInt)
    await ctx.channel.send(f'Tu numero en binario es: {binary_number}')

client.run('Your token')
