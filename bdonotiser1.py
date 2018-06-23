import discord
import asyncio
from discord import Game
from discord.ext.commands import Bot
import datetime
import os
import pytz
tz = pytz.timezone('Asia/Bangkok')


counter = -6
client = discord.Client()
tier = 't0'
h = 0
m = 0
mt = ''
checkevent = 0
frun = 0
AT = ''
Trole = ''

@client.event
async def on_ready():
    global counter
    global AT
    print('Logged in')
    print('Name : {}'.format(client.user.name))
    print('ID : {}'.format(client.user.id))
    print(discord.__version__)

@client.event
async def on_message(message):
    global counter
    global tier
    global h
    global m
    global mt
    global checkevent
    global Trole
    global AT
    st = message.content.split()
    if len(st) == 3:
        server = st[0]
        t = st[1]
        time = st[2]
        if server.upper() == '!S' or server.upper() == 'S' or server.upper() == 'ห' or server.upper() == 'เซ' or server.upper() == 'ซ':
            if t.upper() == 'T1' or t.upper() == 'T2' or t.upper() == 'T3' or t.upper() == 'T4' or t.upper() == 'T5' or t.upper() == 'T6' or t.upper() == 'T7' or t.upper() == 'T8' or t.upper() == '1' or t.upper() == '2' or t.upper() == '3' or t.upper() == '4' or t.upper() == '5' or t.upper() == '6' or t.upper() == '7' or t.upper() == '8':
                if (int(time) < 61 and int(time) > 3) or (int(time) == -6):
                    await client.add_reaction(message, "👌")
                    if len(t) == 1:
                        tier = 'T' + t
                    else:
                        tier = t
                    Trole = discord.utils.find(lambda r: r.name == tier.upper(), message.server.roles)
                    AT = discord.utils.find(lambda r: r.name == 'AllTier', message.server.roles)
                    counter = int(time)
                    now = datetime.datetime.now(tz)
                    hour = (now.hour)
                    mi = (now.minute)
                    h = int(hour)
                    m = int(mi)
                    if m + int(time) >59:
                        if h+1 > 23:
                            h = h + 1 - 24
                        else:
                            h += 1
                        m = m + int(time) -60
                    else:
                        m = m + int(time)
                    if m<10:
                        mt = '0'+str(m)
                    else:
                        mt = str(m)
                    checkevent = 1
                    if counter > 0:
                        counter -= 1
    if len(st) == 2:
        server = st[0]
        t = st[1]
        if server.upper() == '!S' or server.upper() == 'S' or server.upper() == 'ห' or server.upper() == 'เซ' or server.upper() == 'ซ':
            if t.upper() == 'DEL':
                counter = -6
                checkevent = 1


async def my_background_task():
    await client.wait_until_ready()
    global counter
    global tier
    global h
    global m
    global mt
    global checkevent
    global frun
    global Trole
    global AT
    while not client.is_closed:
        if counter > 0:
            await client.change_presence(game=discord.Game(name=tier.upper() + ' at '+ str(h) +':'+ mt +' (' +str(counter)+' min)' ))
            if counter == 3:
                frun = 1
                msg2 = await client.send_message(discord.Object(id='450622239566462996'), AT.mention+' ' + Trole.mention + ' Ser-1 Open in 3 min')
                msg3 = await client.send_message(discord.Object(id='450622261343289356'), AT.mention+' ' + Trole.mention + ' Ser-1 Open in 3 min')
            elif counter == 2:
                msg2 = await client.edit_message(msg2, AT.mention+' ' + Trole.mention + ' Ser-1 Open in 2 min')
                msg3 = await client.edit_message(msg3, AT.mention+' ' + Trole.mention + ' Ser-1 Open in 2 min')
            elif counter == 1:
                msg2 = await client.edit_message(msg2, AT.mention+' ' + Trole.mention + ' Ser-1 Open in 1 min')
                msg3 = await client.edit_message(msg3, AT.mention+' ' + Trole.mention + ' Ser-1 Open in 1 min')
            counter -= 1
        elif counter == 0:
            re = counter + 5
            await client.delete_message(msg3)
            msg1 = await client.send_message(discord.Object(id='446025258366140427'), AT.mention+' ' + Trole.mention + ' Ser-1 OPEN NOW!!!! (Remaining ' + str(re) + ' min)')
            msg2 = await client.edit_message(msg2, AT.mention+' ' + Trole.mention + ' Ser-1 OPEN NOW!!!! (Remaining ' + str(re) + ' min)')
            msg3 = await client.send_message(discord.Object(id='450622261343289356'), AT.mention+' ' + Trole.mention + ' Ser-1 OPEN NOW!!!! (Remaining ' + str(re) + ' min)')
            await client.change_presence(game=discord.Game(name=tier.upper() + ' Open Register '+str(re)+' min'))
            counter -= 1
        elif counter > -5:
            re = counter + 5
            msg1 = await client.edit_message(msg1,AT.mention+' ' + Trole.mention + ' Ser-1 OPEN NOW!!!! (Remaining ' + str(re) + ' min)')
            msg2 = await client.edit_message(msg2,AT.mention+' ' + Trole.mention + ' Ser-1 OPEN NOW!!!! (Remaining ' + str(re) + ' min)')
            msg3 = await client.edit_message(msg3,AT.mention+' ' + Trole.mention + ' Ser-1 OPEN NOW!!!! (Remaining ' + str(re) + ' min)')
            await client.change_presence(game=discord.Game(name=tier.upper() + ' Open Register '+str(re)+' min'))
            counter -= 1
        elif counter == -5:
            msg1 = await client.edit_message(msg1, AT.mention+' ' + Trole.mention + ' Ser-1 Closed!')
            msg2 = await client.edit_message(msg2, AT.mention+' ' + Trole.mention + ' Ser-1 Closed!')
            msg3 = await client.edit_message(msg3, AT.mention+' ' + Trole.mention + ' Ser-1 Closed!')
            await client.change_presence(game=discord.Game(name=tier.upper() + ' Close Register'))
            counter -= 1
        elif counter == -6:
            await client.change_presence(game=discord.Game(name='Waiting Command'))
            counter = -7
        if counter > -6:
            lp = 0
            while lp < 60:
                await asyncio.sleep(1)
                if checkevent == 1:
                    lp = 60
                    checkevent = 0
                else:
                    lp += 1
        else:
            lp = 0
            while lp < 60:
                if checkevent == 1:
                    lp = 60
                    checkevent = 0
                    if frun == 1:
                        await client.delete_message(msg1)
                        await client.delete_message(msg2)
                        await client.delete_message(msg3)
                        frun = 0
                else:
                    lp += 1
                await asyncio.sleep(1)

client.loop.create_task(my_background_task())
client.run(os.getenv('TOKEN'))
