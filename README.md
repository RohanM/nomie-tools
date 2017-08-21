# Nomie Tools

https://nomie.io/

## Importing a list of trackers into Nomie

Ever come up with a plan for tracking a number of things across your life, but baulked at
adding 40-odd trackers one-by-one into Nomie?

With this tool, you put your trackers in a spreadsheet, and the tool adds them to Nomie for you.

### Warning

I wrote and tested this tool in an evening, and so it may well inexplicably fail to work,
destroy your data, and then say mean things about your cat. You have been warned.

### Assumptions

You're comfortable using the command line and running python scripts.

### Usage

1. Make a dropbox backup from Nomie (or if you're starting from scratch, you can use the provided `sample.nomie.json`).
2. Save this backup somewhere safe just in case everything goes wrong.
3. Fill out a `trackers.csv` file with the trackers you'd like to add, in the format `board,tracker`. See `trackers.sample.csv` for an example.
4. Run `python extend_backup.py -i <backup.nomie.json> -o <backup.new.nomie.json> -t <trackers.csv>`
5. Copy your augmented backup file into the Nomie dropbox folder.
6. Restore the backup into Nomie.
7. Go fourth and pretty up your freshly minted trackers.
