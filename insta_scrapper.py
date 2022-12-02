import argparse


''' Argument parsing details'''

description = 'Automate likes and comments on an instagram account'
usage = 'insta_scrapper.py [-u --username] [-p --password] [-t --target]'

examples = """
 Examples:
 insta_scrapper.py -u username -p password -t target
 """

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=description,
    usage = usage,
    epilog=examples,
    prog='insta_scrapper'
 )

''' Take a positional arguments to get the username and password'''
parser.add_argument('-u','--username', metavar='', type=str, help='Instagram username')
parser.add_argument('-p','--password', metavar='', type=str, help='Instagram password')
parser.add_argument('-t', '--target',  metavar='', type=str, help='target (account or tag)')
