# Program to remove all whitespaces
import re

def Split(string):
    # matches all whitespace characters
    pattern = '\s+'

    # empty string
    replace = ''

    result = re.sub(pattern, replace, string)
    print(result)

    new_string = re.sub(r'\s+', replace, string, 1) 
    print(new_string)

def main():

    # multiline string
    string = 'abc 12\
    de 23 \n f45 6'

    Split(string) 

if __name__=="__main__":
    main()