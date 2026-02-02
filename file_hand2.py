from pathlib import Path
path = Path("/home/allinone/Scan_log_py.logs/Nmap_py.log")
with path.open("r") as f:
    f.readlines()