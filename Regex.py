import re
 
def find_date(s):
    """
    Find the date from the given string. The date must follow the pattern dd Mmm yyyy.
    Months are described by 3 letter abbreviations. Days and years can be omitted. 
    E.g., 1 Feb 2020, 13 Apr 2563, Dec 2019
    Input:  s = the input string
    Output: a list of date tuple, (day, month, year)
    """
    return re.findall(r'([0-9]+)?\s*\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\b\s*([0-9]{4})?', s)
 
 
def find_amount(s):
    """
    Find the amounts of money indicated by the dollar sign ($) from the given string, included
    the sign. The amount may be negative and may contain decimal points. The baht sign may
    appear in front of the amount or after. E.g., 500$, $1000.50, $-100000.
    Input:  s = the input string
    Output: a list of amounts of money in string
    """
    x = re.findall(r'(\$(-?\d+(\.\d+)?))|((-?\d+(\.\d+)?)\$)',s)
    if x != None:
        return [match[0].strip() if match[0] else match[3].strip() for match in x]
 
 
 
 
if __name__=="__main__":
    s1 = 'Sarun pay 500$ to Thammasat University on 13 Apr 2563'
    print(s1)
    print('\tDate  : ', find_date(s1))
    print('\tAmount: ', find_amount(s1))
    s2 = 'Rico gives Thammasat University Hospital $1000.50 on 1 Feb 2020'
    print(s2)
    print('\tDate  : ', find_date(s2))
    print('\tAmount: ', find_amount(s2))
    s3 = 'On Dec 2019, Thammasat University reports the profit in quarter 1 is $-100000'
    print(s3)
    print('\tDate  : ', find_date(s3))
    print('\tAmount: ', find_amount(s3))
    s4 = '8 Mar is International Women Day'
    print(s4)
    print('\tDate  : ', find_date(s4))
    print('\tAmount: ', find_amount(s4))