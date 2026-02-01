from pathlib import Path
base = Path.home() / ("Scan_log_py.logs")
base.mkdir(exist_ok=True)

logfile = base / "Nmap_py.log"

with logfile.open("a") as f:
    f.write("Scan copmpleted\n")