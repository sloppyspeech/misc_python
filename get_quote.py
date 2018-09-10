import json
import sys
import requests as req
import chardet

def getQuote():
    json_data=req.post("http://api.forismatic.com/api/1.0/",data={"method":"getQuote","lang":"en","format":"json"})
    # print(chardet.detect(json_data.content)["encoding"])
    return json_data.json()["quoteText"],json_data.json()["quoteAuthor"]

if __name__ == "__main__":
    quote, author = getQuote()
    quote  = "\033[1;36m" + "\"" + quote + "\"" + "\033[1;m"
    author = "\033[1;35m" + "--" + author       + "\033[1;m"
    output = quote + "\n\t\t" + author
    print(output)
