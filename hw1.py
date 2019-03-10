import re
import sys
import os
#r".+?(?=if (typeof uet == \'function\'))"
#genre = re.compile(r'[\n-][\w-]+\n')    #Genre regex



alltext = ""    # ALL FILE CONTENTS


movielist = []


def getfile(path):  # Write the file into alltext
    fin = open(path, "r")
    str = fin.read()
    alltext = "" + str
    return alltext



def list(alltext):
    # List all movie names.
    print("Listing ...")
    filmsre = re.compile(r'.+\s[(]\d{4}[)]')  # Matches movie names.
    movies = filmsre.findall(alltext)
    for i in movies:
        mov = i[1:-7]  # First element is " " remove date.
        movielist.append(mov)
        print(mov)

'''
def getmovies(filestr):
    filmsre = re.compile(r'.+\s[(]\d{4}[)]')  # Matches movie names.
    movies = filmsre.findall(alltext)
    for i in movies:
        mov = i[1:-7]   # First element is " " remove date.
        movielist.append(mov)
        print(mov)

    for mov in filmsre.findall(alltext):
        print(mov)

        my_regex = re.escape(mov) + r".+?(?=if \(typeof)"  # Gets all info about mivoe from all text
        snippet = re.compile(my_regex, re.DOTALL)
        text = snippet.findall(alltext)  # Assign it to text

        txt = "".join(text)  # Convert to alltext
        print(text)

        #print(txt)
        genre = re.compile(r'\n[ ]?[A-Za-z\-]+\n')    #Genre regex



        synopsis = re.compile(r"\n\n[ ]{4}.*")

        desc = synopsis.findall(txt)



        desc = "".join(desc)  # Convert to alltext

        #print("REAL DESC BEFORE PARSING" + desc)

        desc = desc.strip() # TRIM

        director = re.compile(r"Directors?:.+?(?=Stars:)", re.DOTALL)

        stars = re.compile(r"(?<=Stars).+", re.DOTALL)


       # print("SYNOPSIS = " + desc)

        print(genre.findall(txt))

        print(director.findall(txt))

        print(stars.findall(txt))

        print("\n\tNEW MOVIE\n")
'''
def main():
    #parser.add_argument('file', type=argparse.FileType('r'), nargs='+')
    #getmovies(alltext)

    while True:
        user_input = input(">")

        command = user_input.split(" ")

        if command[0] == "INPUT":   # Read the file
            path = command[1]
            print(path)
            alltext = getfile(path)

        if user_input == "LIST":
            list(alltext)



if __name__ == "__main__":
    main()
