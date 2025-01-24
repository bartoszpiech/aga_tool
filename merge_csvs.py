import pandas as pd

# TODO:
# fix \/ errors

CSV_DIR = 'lco/csv'

CSV_FILENAMES = [
    'lco_2023_01',
    'lco_2023_02',
    'lco_2023_03',
    'lco_2023_04',
    'lco_2023_05',
    'lco_2023_06',
    'lco_2023_07',
    'lco_2023_08',
    'lco_2023_09',
    'lco_2023_10',
    'lco_2023_11',
    'lco_2023_12',
]

'''
CSV_DIR = 'csv'
CSV_FILENAMES = [
    #'2022_08',
    #'2022_09',
    #'2022_10', Error: Error, Did not found the same amount of first and last names in the document (313 != 314)
    #'2022_11',
    '2022_12_updated',
    '2023_01',
    '2023_02',
    '2023_03',
    '2023_04',
    '2023_05',
    '2023_06',
    '2023_07',
    '2023_08',
    '2023_09',
    '2023_10_updated',
    '2023_11_updated',
    #'2023_12',
]
'''

def read_records(month):
    df = pd.read_csv(f'{CSV_DIR}/{month}.csv', header=None)
    for _, row in df.iterrows():
        full_name = f'{row[0]} {row[1]}'
        if full_name in records:
            records[full_name][month] = row[2]
        else:
            records[full_name] = {month: row[2]}

records = {}
for file in CSV_FILENAMES:
    print(f'Reading records from file {file}')
    read_records(file)

#pd.DataFrame(records).T.to_csv('merged.csv')
pd.DataFrame(records).T.to_csv('lco_merged.csv')
