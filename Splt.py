
import re

# Program split string in given input
def Split(string):
    pattern = '\d+'
    result = re.split(pattern, string) 
    print(result)

def main():
    string = 'Twelve:12 Eighty nine:89.'
    Split(string) 

if __name__=="__main__":
    main()