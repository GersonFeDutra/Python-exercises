import discord
# import asyncio
# import random
from private_tokens import *

client = discord.Client()
prefix = "?"

ID = key.server_id()
ROXO = 0x690FC3

roleType0 = 'Membros'
roleType1 = {'name': 'Pixel Dev', 'emoji': '👾'}
roleType2 = {'name': 'Animador', 'emoji': '🎞'}
roleType3 = {'name': 'Hi-bit', 'emoji': '🌠'}
roleType4 = {'name': 'Retro', 'emoji': '🕹'}
roleType5 = {'name': 'Aprendiz', 'emoji': '🎓'}

"""
def get_channel(target_name): # Função que retorna o canal através do seu nome
    for each in client.get_server(ID).channels:
        if each.name == target_name:
            return each
    return None
"""

@client.event
async def on_ready():
    print('BOT ONLINE - Ola Mundo!')
    print(client.user.name)
    print(client.user.id)
    print('----------ByLinky----------')

@client.event
async def on_message(message):
    if message.content.lower().startswith("{}cargos".format(prefix)):
        incorpada = discord.Embed(
            title="Determine suas skills!",
            color=ROXO,
            description="🔹 {} = {}\t\t\t".format(roleType1['name'], roleType1['emoji']) +
                        "🔹 {} = {}\t\t\t".format(roleType2['name'], roleType2['emoji']) +
                        "🔹 {} = {}\n".format(roleType3['name'], roleType3['emoji']) +
                        "🔹 {} = {}\t\t\t\t".format(roleType4['name'], roleType4['emoji']) +
                        "🔹 {} = {}".format(roleType5['name'], roleType5['emoji']),)

        botmsg = await client.send_message(message.channel, embed=incorpada)
        await client.add_reaction(botmsg, roleType1['emoji'])
        await client.add_reaction(botmsg, roleType2['emoji'])
        await client.add_reaction(botmsg, roleType3['emoji'])
        await client.add_reaction(botmsg, roleType4['emoji'])
        await client.add_reaction(botmsg, roleType5['emoji'])

        global msg_id
        msg_id = botmsg.id


        global msg_user
        msg_user = message.author


    if message.channel == client.get_channel(CHANNEL_1):  # A partir daqui todos os métodos só funcionam no canal indicado
        role = discord.utils.find(lambda r: r.name == roleType0, message.server.roles)
        await client.add_roles(message.author, role)  # Função que add um cargo ao autor da mensagem
        await client.add_reaction(message, '✌')

    if message.channel == client.get_channel(CHANNEL_2) and message.content.lower().startswith("#tema_semanal"):
        await client.add_reaction(message, '🔼')
        await client.add_reaction(message, '🔽')


    """
    if message.content.lower().startswith('{}'.format(prefix)) and message.channel != client.get_channel(CHANNEL_3): # Teste de location
        await client.send_message(client.get_channel(CHANNEL_3),
                                  "{} eu só respondo aqui camarada 😒.".format(message.author.mention))
    """

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == str(roleType1['emoji']) and msg.id == msg_id and user == msg_user:
        role = discord.utils.find(lambda r: r.name == roleType1['name'], msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == roleType2['emoji'] and msg.id == msg_id and user == msg_user:
        role = discord.utils.find(lambda r: r.name == roleType2['name'], msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == roleType3['emoji'] and msg.id == msg_id and user == msg_user:
        role = discord.utils.find(lambda r: r.name == roleType3['name'], msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == roleType4['emoji'] and msg.id == msg_id and user == msg_user:
        role = discord.utils.find(lambda r: r.name == roleType4['name'], msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == roleType5['emoji'] and msg.id == msg_id and user == msg_user:
        role = discord.utils.find(lambda r: r.name == roleType5['name'], msg.server.roles)
        await client.add_roles(user, role)
        print("add")

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == roleType1['emoji'] and msg.id == msg_id: # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == roleType1['name'], msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == roleType2['emoji'] and msg.id == msg_id: #and user == msg_user:
        role = discord.utils.find(lambda r: r.name == roleType2['name'], msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == roleType3['emoji'] and msg.id == msg_id: #and user == msg_user:
        role = discord.utils.find(lambda r: r.name == roleType3['name'], msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == roleType4['emoji'] and msg.id == msg_id: #and user == msg_user:
        role = discord.utils.find(lambda r: r.name == roleType4['name'], msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

    if reaction.emoji == roleType5['emoji'] and msg.id == msg_id: #and user == msg_user:
        role = discord.utils.find(lambda r: r.name == roleType5['name'], msg.server.roles)
        await client.remove_roles(user, role)
        print("remove")

# Música
"""
@client.event
async def on_ready():
    print(client.user.name)
    print("Bot Online - Ola Mundo!")

@client.event
async def on_message(message):
    if message.content.startswith('{}in'.format(prefix)):
        try:
            canal = message.author.voice.voice_channel
            await client.join_voice_channel(canal)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "Você precisa estar em um canal de voz!")

    if message.content.startswith('{}off'.format(prefix)):
        try:
            canalVoz = client.voice_client_in(message.server)
            await canalVoz.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "O bot não está conectado em nenhum canal de voz!")
"""

# Hello wolrd
"""
    if message.content.lower().startswith('?test'): # Hello wolrd
       await client.send_message(message.channel, "Ola Mundo! Estou vivo.")
"""

# Cara ou coroa
"""
    if message.content.lower().startswith('?flip'): # Flipa moeda
        if message.author.id == AUTHOR_1:
            choice = random.randint(1,2)
            if choice == 1:
                await client.add_reaction(message, '😀')
            if choice == 2:
                await client.add_reaction(message, '👑')
        else:
            await client.send_message(message.channel, "Você nao tem permiçao para usar este comando!")
"""


@client.event
async def on_member_join(member):
    CHwelcome = client.get_channel(CHANNEL_1)
    CHregras = client.get_channel(CHANNEL_4)
    msg = "Não seja tímida(o) {}, junte-se a nós!\n " \
          "Nos fale um pouco sobre você para ter acesso total aos canais.\n" \
          "Sinta-se livre para ler as nossas regras em {}".format(member.mention, CHregras.mention)
    await client.send_message(CHwelcome, msg)

@client.event
async def on_member_remove(member):
    msg = "Cansou de pixel art?\nSinta-se a vontade para retornar quando quiser!/n"
    await client.send_message(member, msg)

client.run(TOKEN)

"""  # Json
def pega_dados(obj):  # retorna uma instancia de uma classe que contenha o número de chaves do Json == número de parâmetros
    instancia = meuprograma.Entrevista(
        nome=obj['nome'],
        idade=obj['idade'],
        ano=obj['ano']
    )
    return instancia

try:
    arquivo_json = open('dados.json', 'r')
    dados_json = json.load(arquivo_json)
    entrevistas = dados_json['Entrevistas']

    lista_entrevistados = [ pega_dados(entrevista) for entrevista in entrevistas ]
except Exception as erro:
    print("Ocorreu um erro ao carregar o arquivo\n O erro é:{}".format(erro))
"""
