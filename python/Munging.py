# Munging.py
# Author: Taylor Marrion
# Date: 2/9/2020
"""This application formats existing address records and eliminates records with missing critical fields."""

import pandas as pd
import re

def get_formatted_name(value):
    """Returns formatted name or initial or empty string for invalid data"""
    #regex for name or initial
    template = (r'([A-Z]([a-z]*|.?))')
    
    result = value.capitalize()
    
    # check for match to template
    return result if re.fullmatch(template, result) else ''
# end get_formatted_last

def get_formatted_zip(value):
    """Returns formatted zip code or empty string for invalid data"""
    #regex for U.S. zip code
    template = (r'(\d{5})(-\d{4})?')
    
    result = re.fullmatch(r'(\d{5})(\d{4})', value)
    result = '-'.join(result.groups()) if result else value
    
    # check for match to template
    return result if re.fullmatch(template, result) else ''
# end get_formatted_zip

def   get_formatted_phone(value):
    """Returns formatted telephone number or empty string for invalid data"""
    # regex for U.S. telephone number
    template = (r'(\d{3})(-?)(\d{3})(-?)(\d{4})')
    
    result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
    result = '-'.join(result.groups()) if result else value

    # check for match to template
    return result if re.fullmatch(template, result) else ''
# end get_formatted_phone

# start main body of code
# print welcome message
print ('***************** Welcome to the Python Munging Application***********')

# create raw records data
records_raw = [
    ['Jim', 'Robertson', '21801','555-555-5555'], ['John', 'Adams', '223211143', '4444444444'],
    ['Helen', 'Cooper', 'edskd-2134', '323232'], ['', 'Franklin', '234511', '323-333-2211'],
    ['John', 'Goodname', '43214-1455', '614-888-9414'], ['thisis', 'goodtoo', '23219', '8047654321'],
    ['A', 'Little', '00000', '4153179045'], ['harder', 'now', '12345-6789', '987-654-3210'],
    ['F.', 'B.', '39023', '3o5-i32-8SE6'], ['Frodo', 'Baggins', 'E4589-oooo', '345-298-1721'],
    ['t.his', 'willnot', '70347', '194-502-6715'], ['show', 'this.', '21970', '305-211-5691'],
    ['noshow.', 'hopkins', '96744', '8088958670'], ['D.', 'niece', 'ERROR', '800-752-1365'],
    ['toomany', 'numbers', '555555', '555-555-55555'], ['not', 'enough', '12345-678', '555555555'],
    ['I\'m', 'out', '89236', '4023851228'], ['of', 'ideas', '29403-2391', '5482881288'],
    ['nextline', 'reversed', '39045', '8413044185'], ['1234567890', '12345', 'last', 'first'],
    ['J', 'T', '96740-1111', '808-123-4500'], ['j', 't', '43214', '6148581147'],
    ['A.', 'Z.', 'nope', 'one-800-5555'], ['a.', 'z.', '86-23', '8005551479'],
    ['J.h', 'T.dh', '', ''], ['a.hd', 'z.h', '', '']
    ]

records_df = pd.DataFrame(records_raw, columns=['First name', 'Last name', 'Zip', 'Phone'])

formatted_first = records_df['First name'].map(get_formatted_name)
records_df['First name'] = formatted_first

formatted_last = records_df['Last name'].map(get_formatted_name)
records_df['Last name'] = formatted_last

formatted_zip = records_df['Zip'].map(get_formatted_zip)
records_df['Zip'] = formatted_zip

formatted_phone = records_df['Phone'].map(get_formatted_phone)
records_df['Phone'] = formatted_phone

print (records_df)

# print goodbye message
print ('*************** Thanks for Munging with me! **********')
