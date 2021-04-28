import json

# def load_json_file(filename = "new_json_file.json"):
#     with open(filename) as jsonfile:
#         pet = json.load(jsonfile)
#         # print(pet["name"])


class RatesParser:

    def __init__(self, rates_file):
        rates_info = self._open_json_file(rates_file)
        self.base = rates_info["base"]
        self.rates = rates_info["rates"]
        self.gbp = self.rates["GBP"]

    def _open_json_file(self, file):
        with open(file) as rates:
            return json.load(rates)


rates_reader = RatesParser("exchange_rates.json")
