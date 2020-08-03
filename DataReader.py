import sys


def main(filepath):
    try:
        file = open(filepath[0], "r")
    except Exception:
        print("can not open file")
        return

    details = []
    for line in file:
        details.append(line)


if __name__ == '__main__':
    main(sys.argv[1:])
