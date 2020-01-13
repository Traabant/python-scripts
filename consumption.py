import requests
# from ..models import Consumption
import matplotlib.pyplot as plt
import numpy as np
import datetime


class Consumption:
    def __init__(self, teshold_step):
        self.working_list = []
        self.treshold_step = teshold_step
        self.last_mileage = None
        self.first_mileage = None
        self.total_mileage = None
        self.date_added = None
        self.total_consuption = None
        self.total_fuel = None
        self.treshold = None
        self.response = None
        self.consuption_history = {
            "consuption": [],
            "date": [],
        }

        self.main()
    
  
    @staticmethod
    def delete_extra_characters(data_to_clean):
        # removes extra ". This is needed for next steps
        line_without_extra_chars = []
        list_without_extra_chars = []
        for line in data_to_clean:
            for row in line:
                row = row.replace('"', '')
                line_without_extra_chars.append(row)
            list_without_extra_chars.append(line_without_extra_chars)
            line_without_extra_chars = []
        return list_without_extra_chars

    def url_data_to_list(self, data_to_split):
        # splist every line in LIST into another LIST
        # returns two dimensional list
        csv_content_splited = []
        csv_content = data_to_split.content
        csv_content = csv_content.decode(encoding='utf-8')
        csv_content = csv_content.splitlines()
        for line in csv_content:
            splited_line = line.split(",")
            csv_content_splited.append(splited_line)
        csv_content_splited = self.delete_extra_characters(csv_content_splited)
        return csv_content_splited

    def find_data(self, list_to_analyze):
        list_to_return = []
        for line in list_to_analyze:
            if self.is_datetime(line[0]) is True:
                list_to_return.append(line)
        return list_to_return

    @staticmethod
    def is_datetime(string):
        # In Data from Fuelino, only filing gas entries starts with date time
        # Fuelino added time to date log, so i needed to alter test
        try:
            datetime.datetime.strptime(string, "%Y-%m-%d")
            return True
        except:
            try:
                datetime.datetime.strptime(string, "%Y-%m-%d %H:%M")
                return True
            except:
                return False

    def particial_history(self, list_with_correct_data):
        """
        :param list_with_correct_data: list with all parsed data
        :return: lsit witn shortened data, only data that mets creterium
        """
        list_with_shortened_data = []
        last_mileage = float(list_with_correct_data[0][1])
        self.treshold = last_mileage - self.treshold_step
        for item in list_with_correct_data:
            if float(item[1]) > self.treshold:
                list_with_shortened_data.append(item)
        return list_with_shortened_data

    def main(self):

        url = 'https://drive.google.com/uc?export=download&id=1_CST2emrtNu1EGvq9h35byyHW1nmKxbu'

        try:
            self.response = requests.get(url)
        except Exception as err:
            print(f'Error during downloding {url} occurred: {err}')
        if self.response.status_code == 200:
            list_with_raw_data = self.url_data_to_list(self.response)
            self.working_list = self.find_data(list_with_raw_data)
            if self.treshold_step is not None:
                self.working_list = self.particial_history(self.working_list)
            self.last_mileage = float(self.working_list[0][1])
            self.first_mileage = float(self.working_list[-1][1])
            self.total_mileage = int(round(self.last_mileage - self.first_mileage))
            self.date_added = self.working_list[0][0]
            self.total_fuel = 0
            for i, item in enumerate(self.working_list):
                self.total_fuel += float(self.working_list[i][2])
            self.total_consuption = (self.total_fuel / self.total_mileage) * 100
        else:
            print(f'Error downloading url {url} with status code {self.response.status_code}')

    def histroy(self):
        """
        prepares data for make_graf method.
        Creates list with dict with continuos consuption data for graf
        :return:
        """
        index = 2
        curent_fuel = float(self.working_list[-1][2])
        while index <= len(self.working_list):
            curent_last_mileage = float(self.working_list[-index][1])
            curent_firt_mileage = float(self.working_list[-1][1])
            current_milage = curent_last_mileage - curent_firt_mileage
            curent_fuel += float(self.working_list[-index][2])
            consumption = (curent_fuel / current_milage) * 100
            self.consuption_history["consuption"].append(consumption)
            self.consuption_history["date"].append(self.working_list[-index][0])
            index += 1
        del self.consuption_history["consuption"][0]   # first entry is off scale
        del self.consuption_history["date"][0]  # first entry is off scale

    def make_graf(self):
        grafLoacation = '/home/Traabant/Homepage/Homepage/homepage/blog/static/blog/graf.png'
        # grafLoacation = "d:\\SIBA\\Scripty\\Homepage\\homepage\\blog\static\\blog\\graf.png"

        self.histroy()

        # plot object
        fig = plt.figure()
        line = fig.add_subplot(1, 1, 1)
        line.plot(self.consuption_history["consuption"])

        # sets ticks for x axis from date list
        tick_marks = np.arange(len(self.consuption_history["date"]))
        plt.xticks(tick_marks, self.consuption_history["date"], rotation=45)

        # show every nth tick on X axis
        every_nth = 8
        for n, label in enumerate(line.xaxis.get_ticklabels()):
            if n % every_nth != 0:
                label.set_visible(False)

        # plt.savefig(grafLoacation, dpi=430)
        plt.show()


if __name__ == '__main__':
    Total_data = Consumption(None)
    last_10k_data = Consumption(10000)

    print(f"Last milage was: {Total_data.last_mileage} logged {Total_data.date_added}")
    print(f"Total Traveled: {Total_data.total_mileage} km")
    print(f'total consumption : {Total_data.total_consuption:.2f} l*100km-1')
    print(f'Total fuel consumed {Total_data.total_fuel:.02f}')
    print("")
    print(f'Consuption during last 10k km was {last_10k_data.total_consuption:.02f} l*100km-1')
    print(f'Fuel consumed last 10k km  {last_10k_data.total_fuel:.02f} liters')

    Total_data.make_graf()

pass
