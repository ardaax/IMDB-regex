import re
import datetime
import calendar
#director = re.compile(r"Directors?:.+?(?=Stars:)|(?=if)", re.DOTALL)


movielist = []

genresdict = dict() # Key is movie name values are genres.
synopsisdict = dict()
starsdict = dict()
directordict = dict()
production_yeardict = dict()    # Keeps production year of all movies
release_datedict = dict()

def getmovies(alltext):
    filmspat = re.compile(r'.+[ ][(]\d{4}[)]\s')  # Matches movie names.
    movies = filmspat.findall(alltext)
    for i in movies:
        mov = i[1:-8]   # First element is " " remove date.
        movielist.append(mov)
        #print(mov)

    datespat = re.compile(r"[A-Z][a-z]+[ ]\d\d?\xa0")   #GETS DATES
    dates = datespat.findall(alltext)



    # GETS RELEASE YEAR
    year_pat = re.compile(r"\xa0+\d{4}", re.DOTALL)
    #print(year_pat.findall(alltext))
    my_date = re.search(year_pat, alltext)
    rel_year = my_date.group(0) # Release year
    rel_year = rel_year.strip()


    ## THIS PART GETS DATES

    def dateformat(i, m):
        #print(dates[i])
        if m == 1:  # Small script for last element
            datepat = re.escape(dates[i]) + r".*" + dates[i + 1]
        else:
            datepat = re.escape(dates[i]) + r".*"
        date_range = re.compile(datepat, re.DOTALL)

        date_text = date_range.findall(alltext)
        date_text = "".join(date_text)  # Convert to alltext

        ## REFORMATING MONTH AND DAY ##

        day_pat = re.search(r"\d+", dates[i])  # Gets day. i.e from April 5 >> 5
        day = day_pat.group(0).zfill(2)  # Make it zero padded.
        #print(day)

        month_pat = re.search(r"\w+", dates[i])  # Get month
        month = month_pat.group(0)
        month = list(calendar.month_name).index(month)
        month = str(month).zfill(2)  # Make the month zero padded
        #print(month)

        date_obj = rel_year + "-" + month + "-" + day
        # date_obj = date_obj.replace("\xa0","")
        date_obj = (datetime.datetime.strptime(date_obj, "%Y-%m-%d"))
        #print(date_obj)

        release_date = str(date_obj)[:-9]  # Strip away the time

        # REFORMATING MONTH AND DAY FINISHED FINAL VAR IS date_obj ##

        for mov in movies:
            if mov in date_text:  # If the movie is in the date range
                release_datedict[mov[1:-8]] = release_date  # add the release dates as a str


    for i in range(len(dates)-1):   # Loop through month-days except last element
        dateformat(i,1)
    dateformat(len(dates)-1, 0) # last element

    print(release_datedict.keys())
    print(release_datedict.values())


    # THIS PART LOOKS FOR ALL THE RELEVANT TEXT FOR EACH MOVIE AND FILLS THE DICTS

    for mov in filmspat.findall(alltext):
        print(mov)

        prod_year = mov[-6:-2]  # Prodcution year
        production_yeardict[mov[1:-8]] = "Production year: " + prod_year
        print(production_yeardict[mov[1:-8]])


        my_regex = re.escape(mov) + r".+?(?=if \(typeof)"  # Gets all info about movie from all text
        snippet = re.compile(my_regex, re.DOTALL)
        text = snippet.findall(alltext)  # Assign it to text

        txt = "".join(text)  # Convert to alltext
        #print(text)


        #SYNOPSIS PART

        descpat = re.compile(r"\n\n[ ]{4}.*")  #Synopsis regex

        desc = descpat.findall(txt)

        desc = "".join(desc)  # Convert to alltext
        desc = desc.strip() # TRIM
        desc = "Synopsis: " + desc
        #print(desc)
        synopsisdict[mov[1:-8]] = desc


        #Stars part

        starspat = re.compile(r"Stars?:.+", re.DOTALL)

        stars = starspat.findall(txt)

        stars = ([i.replace("\n", "") for i in stars])

        strstar = ",".join(stars)
        print(strstar)
        starsdict[mov[1:-8]] = strstar


        # Genre refactoring part

        genrepat = re.compile(r'[0]?\n[\s]*?[A-Za-z\-]+\n.*?(?=Metascore\n)?', re.DOTALL)  # Genre regex
        genre = (genrepat.findall(txt))

        genre = ([i.strip('\n') for i in genre])
        strgenre = ",".join(genre)
        strgenre = strgenre.replace(" ","")
        strgenre = strgenre.replace(",Metascore", "")

        genresdict[mov[1:-8]] = strgenre
        print(genresdict.get(mov[1:-8]))


        #Director part

        if "Stars:" in txt:
            directorpat = re.compile(r"Directors?:\n[|]?\n?.*(?=Stars:)", re.DOTALL)
        else:
            directorpat = re.compile(r"Directors?:\n[|]?\n?.*", re.DOTALL)
        director = directorpat.findall(txt)
        director = ([i.replace('\n', "") for i in director])
        strdirector = ",".join(director)
        strdirector = strdirector.replace("|", ",")
        strdirector = strdirector.strip()
        directordict[mov[1:-8]] = strdirector
        print(strdirector)


        print("\n\tNEW MOVIE\n")


def info(movie):    # GETS ALL INFO ABOUT MOVIE
    print("INFO ...")
    print(movie)
    print(production_yeardict.get(movie))

    rele_date = "Release date: " + release_datedict.get(movie)
    print(rele_date)

    genre = "Genre: " + genresdict.get(movie)
    print(genre)

    print(synopsisdict.get(movie))
    director = directordict.get(movie)
    director = director.replace(":", ": ")
    director = director.replace(" ,", ", ")
    print(director)

    stars = starsdict.get(movie)
    stars = stars.strip()
    stars = stars.replace(":", ": ")
    print(stars)


def listgenre(genres):
    inputgenre = genres.split(",")
    genresnum = len(inputgenre)
    print(inputgenre)
    matched_mov = list()

    for mov in movielist:
        movgenre = genresdict.get(mov)
        movgenre = movgenre.split(",")
        count = 0
        for firstgenre in inputgenre:
            for secondgenre in movgenre:
                if firstgenre == secondgenre:
                    count = count + 1

        if count >= genresnum:
            matched_mov.append(mov)

    for matches in matched_mov:
        print(matches)

#def listfrom(date):

def listmovies(alltext):
    # List all movie names.
    print("Listing ...")
    for m in movielist:
        print(m)

def main():
    #parser.add_argument('file', type=argparse.FileType('r'), nargs='+')
    #getmovies(alltext)
    #info('Shazam!')
    print("\n")
    #info("Avengers: Endgame")
    listgenre("Action,Sci-Fi")


    while True:
        user_input = input(">")

        command = user_input.split(" ")
        if command[0] == "INPUT":   # Read the file
            path = command[1]
            print(path)
            fin = open("april_coming.txt", "r")
            alltext = fin.read()
            getmovies(alltext)
            listmovies(alltext)

        if user_input == "LIST":
            listmovies(alltext)

        if command[0] == "INFO":
            info(command[1])



if __name__ == "__main__":
    main()
