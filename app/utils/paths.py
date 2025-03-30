from pathlib import Path

HOME = "/home/OMS-TN/mashkinas/"
NAME = "pp"

WORKDIR = HOME + NAME + "/"
TEMP =  HOME + "." + NAME + "/"
ENV =  WORKDIR + "venv/bin/python3"
APP = WORKDIR + "app/"

DATA = WORKDIR + "data/"
UPDATES = WORKDIR + "updates/"

LOG_FILE = WORKDIR + NAME + ".log"
JSON_FILE = "info.json"


_home = Path.home()
_name = _home / NAME
_workdir = Path(WORKDIR)
_temp = Path(TEMP)
_env = Path(ENV)
_app = Path(APP)
_data = Path(DATA)
_updates = Path(UPDATES)
_log_file = Path(LOG_FILE)

if __name__ == "__main__":
    for path in (_workdir, _temp, _app, _data, _updates):
        if not (path.exists() and path.is_dir()):
            path.mkdir(parents=True, exist_ok=True)
