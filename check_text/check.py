#this program ckecks curse words

'''
http://www.wdylike.appspot.com/?q=YOURWORD
free website by google to check profinity

replace YOURWORD with the word you would like to check 

'''
import urllib
def read_text():
    quotes = open("./quotes.txt")
    contents = quotes.read()
    
    #uncomment this to print the contents if the file
    #print(contents)
    
    quotes.close()
    check_profanity(contents)

def check_profanity(text):
    #urlopen() helps to connect a website
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = connection.read()
    if output == "true":
        print("There are curse words in this piece of text")
    else:
        print("There are no curse words in this piece of text")
    connection.close()


read_text()

