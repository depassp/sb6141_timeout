A simple scraper used to parse the logs from a SurfBoard 6141.

This was used to troubleshoot T3 and T4 timeouts.  It will likely work with
other Arris/Motorola SurfBoard modems.

Data is stored in a sqlite database.  run.sh is designed to run as a cronjob

pip install -r requirements.txt
./run.sh
