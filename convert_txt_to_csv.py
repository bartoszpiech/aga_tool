import re
import sys

# ąćęłńóśźż
replacement_dict = {
    '¥':    'Ą',
    'Æ':    'Ć',
    'Ê':    'Ę',
    '£':    'Ł',
    '³':    'Ł', # fixup
    'Ñ':    'Ń',
    'Ó':    'Ó',
    '': 'Ś',
    '': 'Ź',
    '¯':    'Ż',
}

def usage(program_name):
    print(f'Usage: {program_name} [FILE]')

if len(sys.argv) < 2:
    usage(sys.argv[0])
    exit(1)

file_path = sys.argv[1]
with open(file_path, 'r', encoding='latin-1') as file:
    file_content = file.read()

for old_char, new_char in replacement_dict.items():
    file_content = file_content.replace(old_char, new_char)

# old
#lastname_price = r'(?<=G)([A-ZĄĆĘŁŃÓŚŹŻ\-]+).*?(\d{1,10}?\s?\d{1,10},\d{2})'
lastname_price = r'(?<=G)([A-ZĄĆĘŁŃÓŚŹŻ\-]+).*?(\d{0,10}\s?\d{0,10},\d{2})'

# old (2022)
#firstname = r'(?<=G)([A-ZĄĆĘŁŃÓŚŹŻ]+).*Fund. Razem Koszty'
# new (2023)
firstname = r'(?<=G)([A-ZĄĆĘŁŃÓŚŹŻ]+).*odst. zdrowot. Podst. podat.'


lastname_price_matches = re.findall(lastname_price, file_content)
firstname_matches = re.findall(firstname, file_content)

if len(lastname_price_matches) != len(firstname_matches):
    print(f'Error, Did not found the same amount of first and last names in the document ({len(firstname_matches)} != {len(lastname_price_matches)})')
    exit(1)

matches = []
for i in range(len(firstname_matches)):
    # for debugging
    #print(f'{firstname_matches[i]} ', end='')
    #print(f'{lastname_price_matches[i][0]}')

    #print(f'{lastname_price_matches[i][0]} {firstname_matches[i]}')
    matches.append((lastname_price_matches[i][0], firstname_matches[i], lastname_price_matches[i][1]))

for match in matches:
    price = match[2].replace(',', '.').replace(' ', '')
    print(f'{match[0]},{match[1]},{price}')

#https://hecker.likesyou.org/1389209398
