import codecs, sys, imp, marshal, os

arg = sys.argv
if len(arg) > 2:
    file = open(arg[1],'rb').read()
    if imp.get_magic() in file:
        file = marshal.loads(file[16:])
    else:
        file = compile(file,'','exec')
    while True:
        if 'rot_13' in file.co_consts or 'bz2_codec' in file.co_consts or 'utf-16_be' in file.co_consts:
            x = codecs.decode(file.co_consts[0].co_consts[1],file.co_consts[2])
            print(len(x))
            file = compile(x,'','exec')
        else:
            if isinstance(x, bytes):
                x = x.decode()
            open(arg[2],'w').write(x)
            print(x)
            break
else:
    exit('usage : ddc.py [file] [out]')