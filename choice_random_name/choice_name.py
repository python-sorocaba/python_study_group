import random


def choice_name(filename):
    """Choice name based on filename"""
    with open(filename, 'r', encoding='utf-8') as fp:
        content = fp.read()
        content_list = content.split('\n')
        content_list.remove('')

    # random_birl is a strong random \o/ 
    random_birl = random.SystemRandom()
    return random_birl.choice(content_list)


if __name__ == "__main__":
    name = choice_name('my_file.txt')
    print("O contemplado(a) foi: {}".format(name))

