import sys
import json
from scrapers.courses import get_available_courses

PATH = "output/"
CURRENT_YEAR = 2022

if __name__ == "__main__":

    # check if number of arguments is correct
    if len(sys.argv) != 3:
        print("ERROR: Arity mismatch, make sure to give the correct number of arguments, check the README for details on usage.")
        exit()

    # getting parameters
    year, season = sys.argv[1], sys.argv[2]

    # check if year is permitted
    if int(year) > CURRENT_YEAR:
        print(f"ERROR: Please use years equal or lower than {CURRENT_YEAR}, check the README for details on usage.")
        exit()
    
    # check if season is permitted
    if int(season) > 2 or int(season) < 1:
        print(f"ERROR: Please use 1 or 2 for season, check the README for details on usage.")
        exit()

    # start scraping
    try:
        print(f"Searching for available courses during {year}-{season}")
        data = get_available_courses(year, season)

        print("Dumping data to json file")
        file_path = f"{PATH}courses-{year}-{season}.json"
        with open(file_path, "w", encoding ='utf8') as outfile:
            json.dump(data, outfile, indent = 4, ensure_ascii= False)
            outfile.close()
        print(f"All done, check {file_path}")

    except:
        print("ERROR: Could not get the requested data, check the README for details on common errors.")

    exit(0)