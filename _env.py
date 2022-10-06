import os


def load():
    # print(os.listdir(os.curdir))
    # os.chdir('src')
    print(os.path.realpath(os.curdir))
    if os.path.realpath('.').endswith('src'):
        path = '../.env'
    else:
        path = '.env'

    with open(path) as f:
        lines = f.readlines()

    for ln in lines:
        if '=' not in ln:
            continue
        sep = ln.split('=')
        if len(sep) != 2:
            continue

        os.environ.setdefault(sep[0], eval(sep[1]))


load()


