import os

# This is file to start from.
starting_file = '__init__.py'

# This is output (inlined) file.
output_file = 'uberfile.py'

# ----------------------------------


modules = []
imports = []

out_file = open(output_file, mode='w', encoding='utf-8')


def count_from_start(string, char):
    """
    Count number of conclusive occurrences from start of specified character.
    :param string: string
    :param char: character
    :return: number of concluding occurrences
    """
    c = 0
    for e in string:
        if e == char:
            c += 1
        else:
            return c
    return c


def normalize_import(rel, base='./'):
    dots_from_start = count_from_start(rel, '.')
    down_path = rel[dots_from_start:].split('.')  # [common, abc]

    base_elements = base.split('/')
    while dots_from_start:
        base_elements.pop()
        dots_from_start -= 1

    final = base_elements + down_path
    file = '/'.join(final) + '.py'

    final.pop()
    folder = '/'.join(final)

    return file, folder + '/'


def emit_line(line):
    out_file.write(line)


def inline_file(file, base):
    if not os.path.isfile(file):  # try __init__.py file
        base = file[:-3] + '/'
        file = file[:-3] + '/__init__.py'

    if not os.path.isfile(file):
        print(f"file not found: {file}!")
        emit_line(f"# ----- file {file} begin -----\n")
        emit_line(f"# file {file} does not exists!")
        emit_line(f"# ----- file {file} end -----\n")
        return

    print(f"inline file: {file}")

    emit_line(f"# ----- file {file} begin -----\n")
    multiline_import = False

    with open(file, encoding='utf-8') as f:
        prev_line = ''
        for l in f:

            if multiline_import:
                emit_line('# ' + l)
                if ')' in l:
                    multiline_import = False
                continue

            if l.strip().startswith('import'):
                module = l.strip().split(' ')[1]

                if ' as ' in l.strip():  # ensure all aliases are imported
                    as_idx = l.strip().split(' ').index('as')
                    module = l.strip().split(' ')[as_idx + 1]

                is_try_except_import = 'try:' in prev_line or 'except ImportError:' in prev_line

                if module not in imports or is_try_except_import:
                    emit_line(l)
                    imports.append(module)
                else:
                    emit_line('# ' + l)
            elif l.strip().startswith('from'):
                # from __future__ import unicode_literals
                # from .module2 import TestA, super_sqrt
                # from .downloader.external import list_external_downloaders
                # from .compat import (
                #   compat_HTMLParseError,
                #   compat_HTMLParser
                # )

                if l.strip().split(' ')[1].startswith('.'):  # custom module?
                    module = l.strip().split(' ')[1]  # .common ..compat ..postporocessing.ffmpeg
                    file, folder = normalize_import(module, base)

                    if file not in modules:
                        modules.append(file)
                        inline_file(file, folder)
                    else:
                        emit_line('# ' + l)

                    # check for multiline imports
                    if '(' in l:
                        multiline_import = True
                else:
                    emit_line(l)
            else:
                emit_line(l)
            prev_line = l
    emit_line(f"# ----- file {file} end -----\n")


inline_file(starting_file, './')
out_file.close()
print("output file:", output_file)
