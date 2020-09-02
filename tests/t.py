import re

def split_file(src, dst, separator, regex, rpls):
    f = open(src, 'r', encoding='UTF-8')
    data = f.read()
    f.close()
    ext = src.split('.')[-1]

    data = re.sub(separator, r'_!_\1', data)

    contents = re.split('_!_', data)
    # print(contents)
    for i, v in enumerate(contents):
        n = str(i).rjust(3, '0')
        if v == '':
            continue
        f = open(dst + n + '.' + src.split('.')[-1], 'w', encoding='UTF-8')

        # replace rpls

        f.write(v.strip())
        f.close()


# f = open("samples/s.txt", 'r', encoding='UTF-8')
f = open("samples/jangho.txt", 'r', encoding='UTF-8')
data = f.read()
f.close()

data = re.sub('(\\n\d+\. +)', r'_!_\1', data)

contents = re.split('_!_', data)
# print(contents)
for i, v in enumerate(contents):
    n = str(i).rjust(3, '0')
    if v == '':
        continue
    f = open('samples/jangho/jangho' + n + '.txt', 'w', encoding='UTF-8')
    v = re.sub('─+', '', v)
    v = re.sub('\d{4,4}\.\d{2,2}\.\d{2,2}\.', '', v)
    f.write(v.strip())
    f.close()
