import pandas as pd

# TODO:
# fix \/ errors

CSV_DIR = 'tmp'

CSV_FILENAMES = [
    '2024_01',
    '2024_02',
    '2024_03',
    '2024_04',
    '2024_05',
    '2024_06',
    '2024_07',
    '2024_08',
    '2024_09',
    '2024_10',
    '2024_11',
    '2024_12',
]

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

pd.DataFrame(records).T.to_csv('merged.csv')
#pd.DataFrame(records).T.to_csv('lco_merged.csv')
