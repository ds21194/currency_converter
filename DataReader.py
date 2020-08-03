import sys


def getData(filepath):
    try:
        file = open(filepath, "r")
    except Exception:
        raise ValueError("can not open file")

    details = []
    for line in file:
        details.append(line.strip())
    return details

# if __name__ == '__main__': # TODO: delete
#     main(sys.argv[1:])
