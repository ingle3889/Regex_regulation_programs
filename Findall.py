
# Program find string in given input
import re

def Findall(string):
    pattern = '\d+'
    result = re.findall(pattern, string) 
    print(result)

def main():
    string = 'hello 12 hi 89. Howdy 34'
    Findall(string) 

if __name__=="__main__":
    main()