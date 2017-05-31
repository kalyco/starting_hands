import argparse
import csv

from hands import RANK

def parsed_args():
    desc = "Returns starting hand rank"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--hand', '-s',
                        help="Type 2-character hand. Include '!' for suited",
                        required=True)
    return parser.parse_args()


def main():
    args = parsed_args()
    hand = args.hand
    try:
        rank = RANK[hand.upper()]
        print "Your hand ranks {} out of 169".format(rank)
        percent = (((170 - float(rank)) / 169.0) * 100)
        print "Quality of hand is {}".format(str(round(percent,2)) + "%")
    except:
        print "input not accept. type 2-character hand. Include '!' for suited."        


if __name__ == '__main__':
    main()
