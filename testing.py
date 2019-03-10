import re
#director = re.compile(r"Directors?:.+?(?=Stars:)|(?=if)", re.DOTALL)
fin = open("april_coming.txt", "r")
alltext = fin.read()

movielist = []

genresdict = dict() # Key is movie name values are genres.
synopsisdict = dict()
starsdict = dict()
production_year = dict()    # Keeps production year of all movies

def getmovies(filestr):
    filmspat = re.compile(r'.*\s[(]\d{4}[)]')  # Matches movie names.
    movies = filmspat.findall(alltext)
    for i in movies:
        mov = i[1:-7]   # First element is " " remove date.
        movielist.append(mov)
        print(mov)

    datespat = re.compile(r"[A-Z][a-z]+[ ]\d\d?\xa0")
    dates = datespat.findall(alltext)

    print(dates)

    for mov in filmspat.findall(alltext):
        print(mov)

        my_regex = re.escape(mov) + r".+?(?=if \(typeof)"  # Gets all info about movie from all text
        snippet = re.compile(my_regex, re.DOTALL)
        text = snippet.findall(alltext)  # Assign it to text

        txt = "".join(text)  # Convert to alltext


        #print(txt)
        genrepat = re.compile(r'[0]?\n[\s]*?[A-Za-z\-]+\n.*?(?=Metascore\n)?', re.DOTALL)    #Genre regex

        print(text)

        descpat = re.compile(r"\n\n[ ]{4}.*")  #Synopsis regex

        desc = descpat.findall(txt)



        desc = "".join(desc)  # Convert to alltext
        desc = desc.strip() # TRIM
        print(desc)



        director = re.compile(r"Directors?:\n[|]?\n?.*(?=Stars:)", re.DOTALL)

        starspat = re.compile(r"Stars?:.+", re.DOTALL)

        stars = starspat.findall(txt)
        print(stars)
        stars = ([i.replace("\n", "") for i in stars])

        strstar = ",".join(stars)
        strstar = strstar.replace(",Metascore", "")
        print(strstar)
        starsdict[mov[1:-7]] = strstar


        # Genre refactoring part
        genre = (genrepat.findall(txt))


        genre = ([i.strip('\n') for i in genre])
        strgenre = ",".join(genre)
        strgenre = strgenre.replace(" ","")
        strgenre = strgenre.replace(",Metascore", "")


        genresdict[mov[1:-7]] = "Genre: " + strgenre
        print(genresdict.get(mov[1:-7]))



        print(director.findall(txt))



        print("\n\tNEW MOVIE\n")

def main():
    #parser.add_argument('file', type=argparse.FileType('r'), nargs='+')
    getmovies(alltext)




if __name__ == "__main__":
    main()
