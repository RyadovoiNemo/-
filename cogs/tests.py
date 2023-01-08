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



print(poisk_polozneniya_mata_and_zamena('мармелад дорога небо баклажан небо я небо веселый баклажан ну вот и супер мармелад' ))








