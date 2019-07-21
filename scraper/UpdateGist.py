import github
import codecs

# Pushes the output.json file to a gist on github
def update():
    #Connects to a github acount
    g = github.Github("6e9298305c669d73192ae19c3d972f10841dba80")
    # Add the file to a gist
    with codecs.open('output.json', 'r', encoding='utf8') as f:
        g.get_gist("c93e0407cfe939d0a77137cc8ad210f8").edit(files = {"BestCheapestDrink.json" : github.InputFileContent(f.read())})