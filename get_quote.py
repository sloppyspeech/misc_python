import json
import sys
import requests as req
import chardet  #To get the charset type

def get_quote():
    json_data=req.post("http://api.forismatic.com/api/1.0/",data={"method":"getQuote","lang":"en","format":"json"})
    # print(chardet.detect(json_data.content)["encoding"])
    return json_data.json()["quoteText"],json_data.json()["quoteAuthor"]

def get_chuck_norrised():
    # Needed to install PyOpenSSL and idna to get this to work using requests
    # check link https://stackoverflow.com/questions/18578439/using-requests-with-tls-doesnt-give-sni-support/18579484#18579484
    json_data=req.get("https://api.chucknorris.io/jokes/random")
    # print(json_data.json())
    return json_data.json()["value"]

if __name__ == "__main__":
    quote, author = get_quote()
    quote  = "\033[1;36m" + "\"" + quote + "\"" + "\033[1;m"
    author = "\033[1;35m" + "--" + author       + "\033[1;m"
    output = quote + "\n\t\t" + author
    print(output)
    get_chuck_norrised()
    quote  = "\033[1;36m" + "\"" + get_chuck_norrised() + "\"" + "\033[1;m"
    author = "\033[1;35m" + "--" + "Chuck Norris"       + "\033[1;m"
    output = quote + "\n\t\t" + author
    print(output)

