import github
import codecs
import json

def update():
    #Github token or login
    g = github.Github("-")
    with codecs.open('output.json', 'r', encoding='utf8') as f:
        #Gist ID
        g.get_gist("-").edit(files = {"BestCheapestDrink.json" : github.InputFileContent(f.read())})