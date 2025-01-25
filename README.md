# AGA Tool

It's a set of python scripts that converts exported txt files from AGA -- staff and salaries tool. It's a tool made specifically for future me 😊

# How to use AGA Tool

## Prerequisites

First you have to export lists of orders for each month that you want to make summary from. To do this you have to set "Sales" (ctrl-p) in AGA, then set a correct month (remember to -1, so you have to start from 12.202x to 11.202x+1). Then print "List of orders", in settings choose "Print to TXT" and change destination file to correct directory. Then you select "Print" and wait... You have to gather 12 files from separate months.

## Using scripts

- Install requirements.txt
```$ pip install -r requirements.txt```
- Run ```runner.sh```
```$ bash runner.sh```
- Run ```check_duplicates.py``` and then correct all errors,
```$ python check_duplicates.py```
- Run ```merge_csvs.py```
```$ python merge_csvs.py```
- Import the csv file and prettify it.

Just use the ```runner.sh``` script in ```/tmp``` directory. Check if everything's okay, use ```check_duplicates.py```
