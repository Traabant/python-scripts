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

    def find_integrity_check(self, client):
        """
        :param  ID: int
        :param name: string , clients name,
        :param data: list, contains lines from log file

        cycle thought list of lines from log file
        finds last integrity checks and appends self.last_update with parsed data from this line
        """
        cur_pos = len(client.logs)
        str_to_check = "TXTKontrola integrity - úspěšný konec operace"    
        while True:
            cur_pos -= 1
            cur_line = (client.logs[cur_pos])
            cur_line = cur_line.split("\x10")            
            if (cur_line[3] == str_to_check):    
                client.status = cur_line[3] 
                client.date_logged = datetime.datetime.strptime(cur_line[5], "VE2%Y%m%d")    
                client.last_update = datetime.datetime.strptime(cur_line[1], "DAT%Y%m%d")       
                self.last_updates.append(client)                
                break            

            if (cur_pos == 0):
                client.status = "not found"
                self.problems.append(client)
                break
        
    def analyze_last_updates(self):
        """
        checks if last update date is within range
        """
        threshold_size = datetime.timedelta(days=-60) 
        threshold_date = datetime.datetime.now() + threshold_size        
        for client in self.last_updates:
            if client.last_update < threshold_date:
                self.problems.append(client)
            else:
                self.is_OK.append(client)

    def talk_to_user(self):
        results_file = "JusticeAnalyzer\\results\\results" + datetime.datetime.now().strftime('%Y-%m-%d') + ".csv"
        with open(results_file, "a", encoding="UTF-8") as f:
            # f.write(f"date analyzed: {datetime.datetime.now().strftime('%Y-%m-%d')}\n")
            f.write(f"# num \tID\tname\tlast update\n")
            for i, client in enumerate(self.problems):                             
                if client.status == 'not found':
                    # print(f"#{i}\tID:{client.ID}\t last update not found\n")
                    f.write(f"{i}\t{client.ID}\t{client.name}\t not found\n")
                else:                
                    # print(f"#{i}\tID:{client.ID}\tlast update: {client.last_update}\n")
                    f.write(f"{i}\t{client.ID}\t{client.name}\t{client.last_update}\n")

    def get_ID_from_csv(self):
        """
        :return parsed_list: list of dicts
        """
        csv_name = "JusticeAnalyzer\ID.csv"
        parsed_list = []
        with open(csv_name, "r") as f:
            lines = f.readlines()
            for line in lines:
                c = Client(line)
                parsed_list.append(c)      
        return parsed_list

    def main(self):             
        clients = self.get_ID_from_csv()
        for client in clients:    
            try:
                with open(client.path) as f:        
                    client.logs = f.readlines()
                self.find_integrity_check(client)
            except FileNotFoundError:
                client.status = "not found"
                self.problems.append(client)
        pass
        


class Client():
    """
    :param source: str, Name;ID\\n

    stores information about Clients
    """

    def __init__(self, source):        
        
        files_location = "\\\\vzdalsprav\\_LOG\\"
        name, ID = source.split(";", 1)    
        ID = ID[0:5]
        path = os.path.join(files_location,ID) 
        path = path + ".log"        

        self.name = name
        self.ID = ID
        self.path = path

        self.logs = None
        self.last_update = None
        self.status = None
        self.date_logged = None    


if __name__ == "__main__":
    Log()   
