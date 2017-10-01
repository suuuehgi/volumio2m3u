#!/usr/bin/python3

import sys, os
from ast import literal_eval

changelog = {}

# ================ Configuration =================

version = 0.1
changelog[0.1] = "Init"

# ================================================

if __name__ == "__main__":

    # =============== Argument parser=================

    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        print('Usage:')
        print('\t{} <filename.volumio>'.format(sys.argv[0]))
        print('\t-c, --changelog')
        print('\t-h, --help')
        print('\t-v, --version')
        sys.exit(0)
    
    if len(sys.argv) > 1 and sys.argv[1] in ['-v', '--version']:
        print("Version {}".format(version))
        sys.exit(0)
    
    elif len(sys.argv) > 1 and sys.argv[1] in ['-c', '--changelog']:
        for key in changelog:
            print(key,"\t",changelog[key])
        sys.exit(0)

    if not len(sys.argv) == 2:
        raise ValueError('Wront number of arguments!\nUsage: {} <filename.m3u>'.format(sys.argv[0]))

    elif not os.path.isfile(sys.argv[1]):
        raise ValueError('File {} not found!'.format(sys.argv[1]))
    
    elif not sys.argv[1].endswith('.volumio'):
        raise ValueError('Not a .volumio file!')

    # ================================================


    with open(sys.argv[1], 'r') as f:
        data = f.readlines()

    data = [l.strip() for l in data]    
    data = list(filter(None, data))

    data = literal_eval(data[0])

    print('#EXTM3U')

    for entry in data:

        trigger_www = 0
        if 'http://' in entry['uri'] or 'https://' in entry['uri']:
            trigger_www = 1

        if trigger_www:
            if 'name' in entry:
                print('#EXTINF:-1,{}'.format(entry['name']))
                print(entry['uri'])
            elif 'title' in entry:
                print('#EXTINF:-1,{}'.format(entry['title']))
                print(entry['uri'])
            else:
                print('Entry has neither title, nor name tag! Taking end of uri.', file=sys.stderr)
                title = entry['uri'].split('/')[-1].strip()
                print('#EXTINF:-1,{}'.format(entry['title']))
                print(entry['uri'])
                
        else:
            if not 'artist' in entry:
                artist = ''
            else:
                artist = entry['artist'].strip()

            if 'undefined' in entry['title']:
                print('Entry has no title! Taking end of uri.', file=sys.stderr)
                title = entry['uri'].split('/')[-1].strip()
                # Assuming file extention: Removing it
                title = ''.join(title.split('.')[:-1]).strip()
            else:
                title = entry['title'].strip()

            if not artist:
                print('#EXTINF:-1,{}'.format(title))
            else:
                print('#EXTINF:-1,{}'.format(' - '.join( [artist, title] )))
            print(entry['uri'])
