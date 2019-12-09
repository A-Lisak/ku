#! /usr/bin/python3
from argparse import ArgumentParser


def need_restart():
    """
    Read the supplied file to see if reboot required.
    """
    reboot_needed = ""
    try:
        path = 'p_file.txt'
        p_file = open(path, 'r')
        reboot_needed = p_file.read()
    except IOError as e:
        print(e)
    if "*** system restart required ***" in reboot_needed:
        re_needed = "*** system restart required ***"
    else:
        re_needed = "No reboot required"

    print(re_needed)


if __name__ == '__main__':
    parser = ArgumentParser(description=
                            '''
              Read the supplied file to see if reboot required.
                            ''')
    parser.add_argument('-p', '--pfile', required=True,
                        help='''the full path to the pom.xml file to be processed''')
    args = parser.parse_args()
    need_restart()
