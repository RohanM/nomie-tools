# Extend Backup
# Imports trackers from CSV into a Nomie backup file
#
# Usage:
# python extend_backup.py -i <backup.json> -o <backup.new.json> -t <trackers.csv>

import sys, getopt
import csv

from nomie_backup import NomieBackup

backup_filename = None
output_filename = None
trackers_filename = None

opts, args = getopt.getopt(sys.argv[1:], "i:o:t:")

for opt, arg in opts:
    if opt == '-i':
        backup_filename = arg
    elif opt == '-o':
        output_filename = arg
    elif opt == '-t':
        trackers_filename = arg

backup = NomieBackup(backup_filename)

with open(trackers_filename) as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        backup.add_tracker(row[0])

backup.save(output_filename)
