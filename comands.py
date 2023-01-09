import disnake
from disnake.ext import commands


with open('cogs\\censored_words.txt','r',encoding='utf-8') as f:
    censored_words = []
    for lst in f:
        censored_words += lst.split(',')


def simplify_words(word):
    result = ''
    last_sumvol = ''
    word = word.lower()
    for sumvol in word:
        if sumvol != last_sumvol:
            last_sumvol = sumvol
            result += last_sumvol
    return result


def poisk_polozneniya_mata_and_zamena(message):
    content = message.split()
    yprpshenn_content = [simplify_words(word) for word in content]
    j = 0
    id_mats = []
    for word_1 in yprpshenn_content:
        vozmozno_mat_1 = ('')
        vozmozno_mat = []
        for word in censored_words:
            part_cencora = word.split()
            if word_1.lower() == word:
                print('мат обнаружен')
                id_mats.append(j)
            else:
                for i in part_cencora:
                    if word_1.lower() == i and i != '':
                        vozmozno_mat.append(word_1.lower())
                        vozmozno_mat_1 = ' '.join(vozmozno_mat)
                        id_mats.append(j)
                    if vozmozno_mat_1 == word:
                        print('мат обнаружен')
                        id_mats.append(j)
        j += 1

    j = 0
    odno_slovo = 0
    for i in range(0, int(len(content))):
        if i == int(len(content))-1 and odno_slovo ==1:
            content[i] = f"{content[i]},||"
            break
        if j == int(len(id_mats)):
            break
        if (i == int(len(content))-1 or j == int(len(id_mats))-1) and i == id_mats[j]:
            content[i] = f"||,{content[i]},||"
            break

        if i == id_mats[j] and odno_slovo == 1:
            content[i] = f'{content[i]}'

        if i == id_mats[j] and odno_slovo == 0:
            content[i] = f'||,{content[i]}'
            odno_slovo = 1

        if i != id_mats[j] and odno_slovo == 1:
            content[i] = f',||,{content[i]}'
            odno_slovo = 0

        if odno_slovo == 1:
            j += 1

    content_1 = ' '.join(content)
    content_2 = ' '.join(content_1.split(','))
    return content_2


class SlashComands(commands.Cog):
    def __init__(self,bot=commands.Bot):
        self.bot = bot


    @commands.slash_command(name='помощь', description='список доступных команд')
    async def help(self,inter):
        msg = "здравствуйте вы запросили помощь"
        await inter.response.send_message(msg)


    @commands.slash_command(name='информация')
    async def server(self,inter):
        await inter.response.send_message(
            f"сервер носит название:{inter.guild.name}\nколичество заложников равно:{inter.guild.member_count}"
        )


    @commands.slash_command(name='смерть', description='полное обнуление объекта')
    @commands.has_permissions(administrator=True)
    async def kick(self, inter,member: disnake.Member,*,reason="на то воля матрицы"):
        await inter.channel.send(f'пользователь {member.mention}был стерт из этой реальности ждем нового клона',delete_after=10)
        await member.kick(reason=reason)
        



    @commands.slash_command(name='интуиция', description='клик-клик и сожалей')
    async def ping(self,inter,):
        msg = ('||'+"ping"+'||')
        await inter.response.send_message(msg)


    @commands.slash_command(name='браниться_охота',description='возможность эмоционально выражать свои эмоции непотребный контент будет скрыт')
    async def get_values(self,inter,message):
        try:
            await inter.response.send_message(f'{poisk_polozneniya_mata_and_zamena(message)}')
        except:
            await message.channel.send(f'возникла непредвиденная ошибка при замене на спойлер запрещенного')


    @commands.slash_command(name='в_черный_список',
                            description='Введите слово или последовательность слов в нижнем регистре. Они будут добавлены в черный список')
    async def test(self, inter, message):
        with open('cogs\\censored_words.txt', 'r', encoding='utf-8') as f:
            censored_words = []
            for lst in f:
                censored_words += lst.split(',')
            print(censored_words)
            new_censored_words = message.split(',')
            i = 7
            for word in new_censored_words:
                censored_words.append(word)
                if int(len(censored_words)) // i:
                    censored_words.append('\n')
                    i += 7
            print(censored_words)
            with open('cogs\\censored_words.txt','w',encoding='utf-8') as outfile:
                outfile.writelines(','.join(str(stl) for stl in  censored_words))
                outfile.close()
            await inter.channel.send(f'слово успешно добавлено в черный список')







def setup(bot:commands.Bot):
    bot.add_cog(SlashComands(bot))
    print(f">Extension {__name__} is ready")