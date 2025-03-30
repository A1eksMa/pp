import pickle
import shelve
from pathlib import Path
###################################
HOME = "/home/OMS-TN/mashkinas/"
NAME = "pp"

WORKDIR = HOME + NAME + "/"
TEMP =  HOME + "." + NAME + "/"
ENV =  WORKDIR + "venv/bin/python3"
APP = WORKDIR + "app/"
DATA = WORKDIR + "data/"
UPDATES = WORKDIR + "updates/"

LOG_FILE = WORKDIR + NAME + ".log"
###################################


def get_list_of_updates(updates: str) -> list:
    if not Path(updates).exists():
        raise Exception("The path is not found!")
    else:
        list_of_updates: list = [file for file in Path(updates).glob("*.pkl")]
        return sorted(list_of_updates)


def read_update(update_name):
    with open(update_name,"rb") as file:
        buffer = pickle.loads(file.read()) 

    header = tuple(buffer.keys())[0]
    data = buffer[header]
    src = header[0]
    uid = header[1]
    dt = header[2]
    return data, src, uid, dt


def transform_data(data: dict, uid: str, dt: str) -> dict:
    """ 
    Transform the data to 4-level dictionary, where levels:
    1 - key - name of the atribute, label from first row of source table
    2 - id - unique position identificator of data
    3 - dt - date-time of data
    4 - value of data
    """
    if uid not in data.keys():
        raise Exception("The key unique identificator (uid) is not found!")
    else:
        key_id_dt_val: dict = dict()
        for key in data.keys():
            if key==uid:
                continue
            else:
                id_dt_val: dict = dict()
                length = len(data[key])

                for i in range(length):
                    dt_val: dict = dict()
                    _dt = dt
                    _val = data[key][i]
                    dt_val = { _dt : _val }

                    _id = data[uid][i]
                    id_dt_val[_id] = dt_val 

                key_id_dt_val[key] = id_dt_val
        return key_id_dt_val

    """  
def update_db(update: str):
    data, src, uid, dt = read_update(update)
    data = transform_data(data, uid, dt)

    # Write key (label of source) if not in shelve
    for key in data.keys():
        with shelve.open(DATA + src) as db:
            if key not in db.keys():
                db.update(db[key])
        

        for i in data:
            # key level
            if i not in db.keys():
                db[i] = data[i]
                continue
            for j in data[i]:
                # id level
                if j not in db[i].keys():
                    db[i][j] = data[i][j]
                    continue
                for k in data[i][j]:
                    # dt level : val
                    db[i][j][k] = data[i][j][k]
    """ 



