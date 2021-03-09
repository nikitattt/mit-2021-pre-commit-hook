import argparse
import io
from typing import Optional
from typing import Sequence


def fix_2020(filename: str) -> int:
    with open(filename, encoding='UTF-8', newline='') as f:
        content = f.read()

    new_content = content.replace('2020', '2021')

    if content != new_content:
        with open(filename, 'w', encoding='UTF-8', newline='') as f:
            f.write(new_content)
        return 1
    else:
        return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        return_value = fix_2020(filename)
        if return_value != 0:
            print(f'Changing 2020 in {filename}')
        retv |= return_value

    return retv

if __name__ == '__main__':
    exit(main())