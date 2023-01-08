def simplify_words(word):
    result = ''
    last_sumvol = ''
    word = word.lower()
    for sumvol in word:
        if sumvol != last_sumvol:
            last_sumvol = sumvol
            result += last_sumvol
    return result


with open('censored_words.txt', 'r', encoding='utf-8') as f:
    censored_words = []
    for lst in f:
        censored_words += lst.split(',')


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

    print(id_mats)

    j = 0
    odno_slovo = 0
    for i in range(0, int(len(content))):
        if i == int(len(content))-1 and odno_slovo ==1:
            content[i] = f"{content[i]},||"
            print('финал цикла сценарий 2', content[i])
            break
        if j == int(len(id_mats)):
            break
        if (i == int(len(content))-1 or j == int(len(id_mats))-1) and i == id_mats[j]:
            content[i] = f"||,{content[i]},||"
            print('финал цикла', content[i])
            break

        if i == id_mats[j] and odno_slovo == 1:
            content[i] = f'{content[i]}'
            print("середина спойлера")
        if i == id_mats[j] and odno_slovo == 0:
            content[i] = f'||,{content[i]}'
            odno_slovo = 1
            print("открытие спойлера")

        if i != id_mats[j] and odno_slovo == 1:
            content[i] = f',||,{content[i]}'
            odno_slovo = 0
            print("закрытие спойлера")

        if odno_slovo == 1:
            j += 1
            print("следующий индекс мата")

        print("это i",i)
        print("это j", j)
        print(odno_slovo)
        print(len(content))





    print(content)

    content_1 = ' '.join(content)
    content_2 = ' '.join(content_1.split(','))
    return content_2



print(poisk_polozneniya_mata_and_zamena('мармелад дорога небо баклажан небо я небо веселый баклажан ну вот и супер мармелад' ))





def poisk_polozneniya_mata(message):
    content = [simplify_words(word) for word in message.split()]
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
                    await message.channel.send(
                        f'{message.author.mention} длинный мат тебе не поможет. я умнее тебя  злобного краба')