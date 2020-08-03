import requests
import json


class ConvertingRequest:

    def __init__(self, details):
        self.conversion = (details[0], details[1])
        self.numbers = []
        for i in range(2, len(details)):
            self.numbers.append(details[i])

    def getConverterParam(self):
        convDetails = f"{self.conversion[0]}_{self.conversion[1]}"
        reqLink = f"https://free.currconv.com/api/v7/convert?q={convDetails}&compact=ultra&apiKey=d4e565adab0cc031a667"
        res = requests.get(reqLink).text

        if res == "{}":
            raise ValueError("One of the languages parameters are wrong")

        return json.loads(res)[convDetails]

    def getResult(self):
        param = self.getConverterParam()
        return list(map(lambda x: float(x)*param, self.numbers))


if __name__ == '__main__':
    a = ConvertingRequest(['USD', 'ILS', '5', '7'])
    print(a.getResult())


