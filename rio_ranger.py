import random
import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os

TOKEN = 'OTE4ODQ0MDAwMjY4NTkxMTU1.YbNKKA.uSFGJ2CeKa_QCBmhHkSsyclW8Zo'

bot = commands.Bot(command_prefix = ('Рио, '))
bot.remove_command('help')

@bot.command()
async def привет(ctx):
    phrase_number = random.randint(1, 5)
    if phrase_number == 1:
        await ctx.send('...')
    if phrase_number == 2:
        await ctx.send('Я буду поддерживать вас на этом этаже! Наилучшие пооооожелания!')
    if phrase_number == 3:
        await ctx.send('Бооже, жуть.')
    if phrase_number == 4:
        await ctx.send('Я Наряжающаяся Кукла, Рио Рейнджер!')
    if phrase_number == 5:
        await ctx.send('Я... папин шедевр... Рио Рейнджер...')

@bot.command()
async def рулетка(ctx):
    n = random.randint(1, 6)
    kill = random.randint(1, 6)
    count = 0
    kill_rio = random.randint(1, 10)
    if n == kill or n == count or count == kill:
        await ctx.send('Неудачник, ты мёртв!')
        count = 0
    elif kill_rio == 4:
        await ctx.send('https://cdn.discordapp.com/attachments/918951122830491688/918956692690075668/ENac8EfXYAEea_2.png')
        await ctx.send('Не надо... Сафалин... Не надо... пожалуйста...!! Мне не нужно сердце... не сейчас...!! Я просто... должен умереть... но ты...!! Хватит...!! ХВААААААААТИТ...!! Аааххх... Меня захлёстывают... эти ненужные эмоции... Нет...!! Это не...!! Простите меня... просто...!!')
        await ctx.bot.logout()
    else:
        await ctx.send('Похоже, тебе повезло, какая жалость')
        count += 1
    if count == 8:
        count = 0

@bot.command()
async def быть(ctx, *, arg):
    await ctx.send('Тебе, придурок, не быть, конечно же.')

@bot.command()
async def хд(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/918951122830491688/919151640278351922/800936f5bd8e67dc.jpg')


@bot.command()
async def как(ctx, *, arg):
    if arg == 'тебе не стыдно':
        await ctx.send('А с чего бы вдруг должно быть?')
    else:
        await ctx.send('Уж всяко лучше твоего.')

@bot.command()
async def я(ctx, *, arg = None):
    if arg == None:
        await ctx.send('Головка от хуя')
    else:
        await ctx.send('Мне нет до этого дела.')

@bot.command()
async def где(ctx, *, arg):
    await ctx.send('Убийственная игра, третий этаж.')

@bot.command()
async def смысл(ctx, *, arg = None):
    if arg == 'жизни':
        await ctx.send('Ты совсем дурак?')
    if arg == None:
        await ctx.send('Договаривай реплику либо заткнись.')

@bot.command()
async def расскажи(ctx, *, arg):
    if arg == 'о юттд':
        await ctx.send('Your Turn To Die -Смертельная Игра решением большинства- (Kimi ga Shine) бесплатная игра в жанре хоррор/приключения/переговоры, разработанная Nankidai и сделанная в RPG Maker MV')
    if arg == 'о себе':
        await ctx.send('Рио Рейнджер или Тото Ноэль (ト ト ・ ノ エ ル, Toto Noeru?), «Переодевающаяся Кукла», является Мастером третьего этажа в Смертельной Игре.')
    if arg == 'обо мне':
        await ctx.send('А тебя я знать не знаю')
    if arg == 'анекдот':
        joke = random.randint(1, 20)
        if joke == 1:
            await ctx.send('Люди, которые переходят на красный, вам так важно, чтобы в вашей смерти был виноват именно автомобилист?')
        if joke == 2:
            await ctx.send('Что бы я ни собирался делать, Гашу может рассказать такую же историю, в которой кто-то умер.')
        if joke == 3:
            await ctx.send('Игроки собираются сбежать. Инструктируют мастеров этажей:\n— Что бы ни случилось, делайте вид, что так и должно быть.\nПришли игроки к выходу, смотрят — вход завалило.\nГашу, посмотрев на часы:\n— Десять тридцать пять, точно по графику.')
        if joke == 4:
            await ctx.send('Кейджи, узнав, что цель кукол — убить:\n— Порублю, суки!\nКуклы испугались и скинулись по рублю.')
        if joke == 5:
            await ctx.send('Кью-таро рассказывает Гину про свои матчи:\n— Ну вот, бегу по полю, и тут ХУЯК, слева враги! ХУЯК! Справа враги!\nНао, бледнея:\n— Ты что такое говоришь? Это же ребёнок!\nКью-таро подскакивает:\n— Какой нахуй ребёнок?! Сборная Кореи, блять!')
        if joke == 6:
            await ctx.send('Джо: слушай, а чего там волхвы принесли новорождённому Иисусу?\nСара: даров\nДжо: привет!')
        if joke == 7:
            await ctx.send('Шин: мне не нравится, как вы игнорируете меня\nСара: ну так скажи, как игнорировать, чтобы тебе нравилось')
        if joke == 8:
            await ctx.send('Я тебе не клоун.')
        if joke == 9:
            await ctx.send('Майли: есть проблема, нужно решение\nСоу: у меня есть план\nМайли: он не должен привести к каким-либо странным последствиям\nСоу: у меня нет плана')
        if joke == 10:
            await ctx.send('Сара: Шин, ты заебал уже врать!\nШин: Я ключник.')
        if joke == 11:
            await ctx.send('Кейджи: сколько тебе лет?\nСоу: а сколько бы ты мне дал?\nКейджи: пожизненное')
        if joke == 12:
            await ctx.send('Приводит батя Сары Кая с женой знакомить:\n— это Кай, он будет нас защищать.\nОна спрашивает:\n— А где он жить будет?\nБатя Сары отвечает:\n— А он вообще жить не хочет.')
        if joke == 13:
            await ctx.send('Кейджи: простите, я потерял своего знакомого, Соу, на пляже. Можно я сделаю объявление?\nОхранник: конечно!\nКейджи, наклоняясь к микрофону: прощай, уёбок.')
        if joke == 14:
            await ctx.send('Сара: Кай так долго вечно сидит в своей комнате \nКейджи: он похож на депрессивного\nСара: режется значит\nКейджи: кое-что покруче\nСара: вскрывается')
        if joke == 15:
            await ctx.send('Гин ловил ртом капли с сосульки. Глупая и нелепая смерть.')
        if joke == 16:
            await ctx.send('Мишима: Ты кто?\nМайли: Твоя смерть.\nМишима: А почему в цветном платье, с рюшечками?\nМайли: Нелепая.')
        if joke == 17:
            await ctx.send('Реко: Есть здесь врач?!\nСафалин: Да, я патологоанатом.\nРеко: Мой брат умирает!\nСафалин: И уже скоро мы узнаём, какова причина смерти...')
        if joke == 18:
            await ctx.send('Гин, после яда: Доктор, я буду жить?\nСафалин: С вопросом, есть ли жизнь после смерти, пожалуйста, обращайтесь в церковь, а я врач.')
        if joke == 19:
            await ctx.send('Сара: можешь привести мне пример парадокса, одновременного грустного и смешного?\nДжо: клоун умер от скуки!')
        if joke == 20:
            await ctx.send('Шин признался друзьям в том, что они геи.')

@bot.command()
async def скучно(ctx):
    await ctx.send('Можем поиграть')

bot.run(TOKEN)