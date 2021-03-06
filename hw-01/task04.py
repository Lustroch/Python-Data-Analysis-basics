# Песенка "Курочка по зёрнышку" (Im Radio ist ein Kuken).
# С помощью этой песенки маленьких детей учат рекурсии, ну а мы потренируемся писать вложенные циклы.
#   Бабушка, бабушка, купим курочку!
#   Бабушка, бабушка, купим курочку!
#   Курочка по зёрнышку кудах-тах-тах.
#   Бабушка, бабушка, купим уточку! (2 раза)
#   Уточка та-ти-та-та,
#   Курочка по зёрнышку кудах-тах-тах.
# Далее персонажи такие:
# ...индюшонка - Индюшонок фалды-балды,
# ...кисоньку - А кисуня мяу-мяу,
# ...собачонку - Собачонка гав-гав,
# ...коровёнку - Коровёнка муки-муки,
# ...поросёнка - Поросёнок хрюки-хрюки,
# и заканчивается всё последним куплетом:
#    Бабушка, бабушка, купим телевизор! (2 раза)
#   Телевизор надо, надо, ведь у нас такое стадо!
# Примечание. "(2 раза)" - это два раза повторить одну строку.
# Hапишите программу, которая генерирует текст песенки.
# Здесь может потребоваться подстановка строк. Действительно, не всегда бывает удобно собирать строку из кусочков, а тем
# более, выводить строку по кусочкам. Для этого используйте любой способ для форматирования строк, который вам удобен.
# Также уделите внимание вот какому аспекту - эта народная потешка имеет много вариаций, начиная со списка участников, и
# заканчивая языком (русским, немецким, каким угодно). Поэтому ваша задача - написать такой код, который как можно проще
# переделывается под новую вариацию.
# Вынесите все данные в отдельное место в программе, чтобы при изменениях текста песни не пришлось выискивать строки,
# разбросанные по коду.

grandma_call = 'Бабушка, бабушка, купим '  # calling grandma
animals_list = ['курочку', 'уточку', 'индюшонка', 'кисоньку', 'собачонку', 'коровёнку', 'поросёнка']
animal_sound = ['Курочка по зёрнышку кудах-тах-тах. \n', 'Уточка та-ти-та-та, \n', 'Индюшонок фалды-балды, \n',
                'А кисуня мяу-мяу, \n', 'Собачонка гав-гав, \n', 'Коровёнка муки-муки, \n',
                'поросёнка - Поросёнок хрюки-хрюки, \n']  # list of the animal's sounds
pre_ending = 'Бабушка, бабушка, купим телевизор! \n'  # suggesting to buy a TV to grandma
ending = 'Телевизор надо, надо, ведь у нас такое стадо! \n'  # a joke about number of animals
# output 8 couplets
for couplet in range(len(animals_list)):
    # calling grandma to buy someone twice
    for _ in range(2):
        print(grandma_call, animals_list[couplet] + '!')
    # repeating sounds of the current animal and the previous ones
    for sounds in range(couplet+1, 0, -1):
        counter = sounds - 1
        print(animal_sound[counter], end='')
        counter -= 1
    print()
    counter = 0
# calling grandma to buy a TV for some reason
for _ in range(2):
    print(pre_ending, end='')
print(ending)
