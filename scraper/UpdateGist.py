import github
import codecs

# Pushes the output.json file to a gist on github
def update():
    #Connects to a github acount
    g = github.Github("")
    # Add the file to a gist
    with codecs.open('output.json', 'r', encoding='utf8') as f:
        g.get_gist("").edit(files = {"BestCheapestDrink.json" : github.InputFileContent(f.read())})