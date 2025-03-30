def log_out(data, logging):
    """
    Print data (4-level dictionary) into log file
    """
    for i in data:
        # key level
        logging.info(f"\t{i}")
        for j in data[i]:
            # id level
            logging.info(f"\t\t{j}")
            for k in data[i][j]:
                # dt level : val
                logging.info(f"\t\t\t{k} : {data[i][j][k]}")


def updates_log_out(list_of_updates: list, logging):
    """
    Print list of updates to log
    """
    if list_of_updates:
        logging.info(f"The {len(list_of_updates)} updates was found:")
        for update in list_of_updates:
            logging.info("\t" + str(update))
    else:
        logging.info("Updates not found.")


def get_source_name_from_update_name(update_name: str) -> str:
    update_name = str(update_name)
    # get file name
    update_name = update_name.split("/")[-1]
    # split extension
    update_name = update_name[:-4]
    # devide on: date, time, ms, source name
    update_name = update_name.split("_")
    # cut the datetime
    update_name = update_name[3:]
    # get source name
    update_name = "".join(update_name)
    return update_name
