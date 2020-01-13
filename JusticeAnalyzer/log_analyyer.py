import os
import datetime


class Log():

    def __init__(self):
        self.last_updates = []
        self.is_OK = []
        self.problems = []
        self.main()
        self.analyze_last_updates()
        self.talk_to_user()

    def parse_intergryty_data(self, ID, name, data):  
        """
        :param ID: int , clients ID,
        :param name: string , clients name,
        :param data: list, with spited single line from log
        :return context: dict
        """
        context = {
            "ID": ID,
            "name": name,
            "status": data[3],
            "last_update": datetime.datetime.strptime(data[5], "VE2%Y%m%d"),
            "date_logged": datetime.datetime.strptime(data[1], "DAT%Y%m%d"),
            }          
        
        return context

    def find_integrity_check(self, ID, name, data):
        """
        :param  ID: int
        :param name: string , clients name,
        :param data: list, contains lines from log file

        cycle thought list of lines from log file
        finds last integrity checks and appends self.last_update with parsed data from this line
        """
        cur_pos = len(data)
        str_to_check = "TXTKontrola integrity - úspěšný konec operace"    
        while True:
            cur_pos -= 1
            cur_line = (data[cur_pos])
            cur_line = cur_line.split("\x10")            
            if (cur_line[3] == str_to_check):                              
                self.last_updates.append(self.parse_intergryty_data(ID, name, cur_line))                
                break
                

            if (cur_pos == 0):
                context = {
                    "ID": ID,
                    "name": name,
                    "status": "not found"
                }
                self.problems.append(context)
                break
        
    def analyze_last_updates(self):
        """
        checks if last update date is within range
        """
        threshold_size = datetime.timedelta(days=-60) 
        threshold_date = datetime.datetime.now() + threshold_size        
        for item in self.last_updates:
            if item["last_update"] < threshold_date:
                self.problems.append(item)
            else:
                self.is_OK.append(item)

    def talk_to_user(self):
        results_file = "JusticeAnalyzer\\results\\results" + datetime.datetime.now().strftime('%Y-%m-%d') + ".csv"
        with open(results_file, "a", encoding="UTF-8") as f:
            # f.write(f"date analyzed: {datetime.datetime.now().strftime('%Y-%m-%d')}\n")
            f.write(f"# num \tID\tname\tlast update\n")
            for i, item in enumerate(self.problems):                             
                if item['status'] == 'not found':
                    # print(f"#{i}\tID:{item['ID']}\t last update not found\n")
                    f.write(f"{i}\t{item['ID']}\t{item['name']}\t not found\n")
                else:                
                    # print(f"#{i}\tID:{item['ID']}\tlast update: {item['last_update']}\n")
                    f.write(f"{i}\t{item['ID']}\t{item['name']}\t{item['last_update']}\n")

    def get_ID_from_csv(self):
        """
        :return parsed_list: list of dicts
        """
        csv_name = "JusticeAnalyzer\ID.csv"
        files_location = "\\\\vzdalsprav\\_LOG\\"
        parsed_list = []
        with open(csv_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                name, ID = line.split(";", 1)    
                ID = ID[0:5]
                path = os.path.join(files_location,ID) 
                path = path + ".log"
                context = {
                    "name": name,
                    "ID": ID,
                    "path": path
                }
                parsed_list.append(context)      
        return parsed_list

    def main(self):             
        IDs = self.get_ID_from_csv()
        for file in IDs:    
            try:
                with open(file['path']) as f:        
                    data = f.readlines()
                self.find_integrity_check(file['ID'], file['name'], data)
            except FileNotFoundError:
                context = {
                    "ID": file['ID'],
                    "status": "not found",
                    "name": file['name'],
                }
                self.problems.append(context)
        pass
        
if __name__ == "__main__":
    Log()   
