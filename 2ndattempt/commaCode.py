spam = ['apples', 'bananas', 'tofu', 'cats']
ham = ['giraffes', 'pigs', 'chickens', 'dogs', 'cats']


def joiner(list):
    for i in list:
        if i in list[:-1]:
            print(i, end=', ')
    else:
        print('and ' + str(list[-1]))


joiner(spam)
joiner(ham)