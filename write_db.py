#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import libraries and dependencies
import sys
sys.path.insert(0, "/home/OMS-TN/mashkinas/pp/app")
from utils.paths import *

import logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)
logging.info("Start `main.py` script...")

logging.info("Import libraries...")
import json

logging.info("Import dependencies...")
from utils.functions import *
from utils.log_out import *

logging.info("Libraries and dependencies was succesfully imported!")


try:
    list_of_updates: list = get_list_of_updates(UPDATES)
    updates_log_out(list_of_updates, logging)

    for update in list_of_updates:
        logging.info(f"Start the update: {update}")
        data, src, uid, dt = read_update(update)

        # Create folder 'src' in DATA
        path = Path(DATA + src)
        if not (path.exists() and path.is_dir()):
            path.mkdir(parents=True, exist_ok=True)
        path_json = path / JSON_FILE

        # Get list of labels
        labels = list(data.keys())

        # Check uid exists
        if uid not in labels: raise Exception("The key unique identificator (uid) is not found!")
        logging.info(f"The next labels will be updated: {labels}")

        # Reg the label
        if path_json.exists():
            with open(path_json, 'r') as file:
                registered_labels:dict = dict(json.load(file))
                lenghth:int = len(list(registered_labels.keys()))
                for label in labels:
                    if label not in registered_labels.keys():
                        registered_labels[lenghth] = label
                        lenghth+=1
        else:
            registered_labels: dict = dict()
            lenghth: int = 1
            for label in labels:
                if label==uid:
                    registered_labels[0] = uid
                else:
                    registered_labels[lenghth] = label
                    lenghth+=1
        with open(path_json, 'w') as file:
            json.dump(registered_labels, file, ensure_ascii=False, indent=4)

        del registered_labels, lenghth, labels
       


        logging.info(f"Try to write data from {update} to `{get_source_name_from_update_name(str(update))}` shelve database...")
except Exception as e:
    logging.error(f"{e}")