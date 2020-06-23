# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Analyze licence expire date
# 

# %%
import os
import datetime
import pandas as pd


# %%
class Client():
    """
    :param source: str, Name;ID\\n

    stores information about Clients
    """

    def __init__(self, source):        
        
        # files_location = "\\\\vzdalsprav\\_LOG\\"
        files_location = "d:\\SIBA\Poznámky k zakazníkum\\Justice\LOG\\"
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

# %% [markdown]
# ## GET IDS FROM CSV

# %%
csv_name = ".\ID.csv"
clients = []
with open(csv_name, "r", encoding="UTF-8") as f:
    lines = f.readlines()
    for line in lines:
        c = Client(line)
        clients.append(c) 

# %% [markdown]
# ## Find lic info from logs

# %%
# str_to_check = "TXTKontrola integrity - úspěšný konec operace"
list_dics = []
problems = []
for client in clients:    
    try:
        with open(client.path) as f:        
            client.logs = f.readlines()
        # check for data
        lic_date = find_lic(client)
        list_dics.append(lic_date)
        df = pd.DataFrame.from_dict(list_dics)
        
    except FileNotFoundError:
        client.status = "not found"
        problems.append(client)
    pass


# %%
def find_lic(client):
    cur_pos = len(client.logs)
    list_dics = []
    while True:
        cur_pos -= 1
        cur_line = (client.logs[cur_pos])
        lic_beg = cur_line.find('LI2')     
        lic_date = cur_line[lic_beg+3:lic_beg+13]   
        # print (f"{client.name}, {client.ID}, {lic_date}")
        dic = {
            "ID": client.ID,
            "Name": client.name,
            "Lic_Date": lic_date
        }
        # list_dics.append(dic)
        # df = pd.DataFrame.from_dict(list_dics)
        return dic
        break

# %% [markdown]
# ## Saves data as CSV

# %%
df.to_csv('./justice_lic.csv', index = False)

