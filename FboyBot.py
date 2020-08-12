import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = "$")

frases = ['Ontas?','Es solo una amiga no te preocupes','Ya siento que te amo','Mirala despidete bien','Mirala bien traviesa','Solo te hablo a ti','Oh chielos, 3AM']
quotes = ['𝗦𝗢𝗟𝗢 𝗦𝗜 𝗘𝗥𝗘𝗦 𝗩𝗜𝗥𝗚𝗘𝗡 𝗣𝗨𝗘𝗗𝗘𝗦 𝗟𝗘𝗘𝗥 𝗘𝗦𝗧𝗢 𝗘𝗡 𝗡𝗘𝗚𝗥𝗜𝗧𝗔𝗦','Todos los planes cambiaron. Era perro y me amarraron.',
          'Quiero ir al registro civil contigo, para poner esas pompas a mi nombre.','Te amo tanto como las familias mexicanas aman comer pollo asado los Domingos',
          'Contigo queda más que claro que Dios me escuchó. *enviar a todas*','Una platicadita con la ex de tu mejor amigo y se te reinicia la vida','Pásame tu ID de Zoom, quiero verte :heart_eyes:. *enviar a todas*',
          'Es que no necesitamos ser novios, ser novios es solo una etiqueta ok?','No te necesito. Te prefiero.','¿Hoy fueron dos personas al espacio? Yo voy y vuelvo a la Luna cada que tú me das un beso.']

@client.event
async def on_message(message):
    if message.content.startswith('$help'):
        await message.channel.send("Comandos: $hola, $fquote, $olvidos, $me besas?, $horny, $fboy, $compa")

    if message.content.startswith('$hola'):
        await message.channel.send(random.choice(frases))

    elif message.content.startswith('$fquote'):
        await  message.channel.send(random.choice(quotes))

    elif message.content.startswith('$olvidos'):
        await message.channel.send('Olvidosssssss 😏')

    elif message.content.startswith('$me besas?'):
        await message.channel.send('No se besar, me besas? 🥺')

    elif message.content.startswith('$horny'):
        await  message.channel.send('Donde andas mensa? 😈🍆💦🥰👌')

    elif message.content.startswith('$fboy'):
        await message.channel.send(file=discord.File('fboy.png'))

    elif message.content.startswith('$compa'):
        await message.channel.send(file=discord.File('chapulin.jpeg'))

client.run('Your Token')