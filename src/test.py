import sys

def is_textedit_enabled():
    return '--textedit' in sys.argv[1:]

if is_textedit_enabled():
    print('Text editing mode is enabled.')
else:
    print('Text editing mode is disabled.')