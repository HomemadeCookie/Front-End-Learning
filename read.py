with open('text.txt', 'r+') as f:
    s = f.read()
    print(s)
    f.write('Hola espanol1')
    f.seek(0)
    s = f.read()
    f.seek(len(s))
    s = f.read()
    print('s2: ' + s)
    f.close()