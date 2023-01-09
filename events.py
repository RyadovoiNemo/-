import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv


def simplify_words(word):
    result = ''
    last_sumvol = ''
    word = word.lower()
    for sumvol in word:
        if sumvol != last_sumvol:
            last_sumvol = sumvol
            result += last_sumvol
    return result


class Events(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("бот готов к работе")


    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = disnake.utils.get(member.guild.roles,
                                       id=1060951298826063932)
        channal = member.guild.system_channel

        embed = disnake.Embed(
            title="Да здравствует свежее мясо",
            description=f"{member.name}#{member.discriminator}",
            color=0xfffff
        )

        await member.add_roles(role)
        await channal.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self,message):
        with open('cogs\\censored_words.txt', 'r', encoding='utf-8') as f:
            censored_words = []
            for lst in f:
                censored_words += lst.split(',')
        if message.author.bot:
            return
        content = [simplify_words(word) for word in message.content.split()]
        for word in censored_words:
            part_cencora = word.split()
            vozmozno_mat_1 = ('')
            vozmozno_mat = []
            for i in part_cencora:
                for word_1 in content:
                    if word_1.lower() == word:
                        try:
                            await message.delete()
                        except:
                            await message.channel.send(f'возникла непредвиденная ошибка при удаленние запрещенного')
                        await message.channel.send(f'{message.author.mention} не щелкай клешнями на меня')
                    elif word_1.lower() == i and i != '':
                        vozmozno_mat.append(word_1.lower())
                        vozmozno_mat_1 = ' '.join(vozmozno_mat)
                    if vozmozno_mat_1 == word:
                        try:
                            await message.delete()
                        except:
                            await message.channel.send(f'возникла непредвиденная ошибка при удаленние запрещенного')
                        await message.channel.send(f'{message.author.mention} длинный мат тебе не поможет. я умнее тебя  злобного краба')



def setup(bot:commands.Bot):
    bot.add_cog(Events(bot))
    print(f">Extension {__name__} is ready")