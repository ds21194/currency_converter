import sys
import DataReader
from ConvertingRequest import *

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("description file is missing")
        sys.exit(1)

    try:
        data = DataReader.getData(sys.argv[1])
    except ValueError as err:
        print(err)
        sys.exit(1)

    request = ConvertingRequest(data)
    try:
        result = request.getResult()
    except ValueError as err:
        print(err)
        sys.exit(1)

    for num in result:
        print(f"{num:.2f}")





