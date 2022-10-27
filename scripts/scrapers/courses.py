import requests
from bs4 import BeautifulSoup
from .utilities.departments import DEPARTMENTS

def get_available_courses(year, season):

    available_courses = {}
    
    for department in DEPARTMENTS:
        department_code = DEPARTMENTS[department]
        try:
            department_url = department_courses_url(department_code, year, season)
            department_courses = department_courses_data(department_url)
            available_courses[department] = department_courses
        except:
            print(f"WARNING: Could not get data for {department} (code: {department_code}) during {year}-{season}, check README for details.")
    
    return available_courses

# (deparment)str (year)str (season)str ->  (url)str 
# returns ucampus department's courses url given the semester parameters
def department_courses_url(department_code, year, season):
    return f'https://ucampus.uchile.cl/m/fcfm_catalogo/?semestre={year}{season}&depto={department_code}'

# scraps code and name of all available courses given a department
def department_courses_data(department_courses_url):
    
    # setup for BeautifulSoup
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
    # define user-agent
    headers = {'User-Agent': userAgent}
    # requesting page
    page = requests.get(department_courses_url, headers = headers)
    # parsed page
    soup = BeautifulSoup(page.content, 'html.parser')

    # get courses list
    courses = soup.find('div', {'id' : 'body'})

    # name of department
    department_name = courses.find('h1').contents[0]
    department_name = department_name.split('-')[1][1:].replace('\n', '')
    print(f"Currently checking: {department_name}")

    # getting info for each course
    courses_dict = {}
    courses = courses.find_all('div', {'class' : 'ramo'})
    for course in courses:
        course_raw_data = course.find('h2').contents[0]
        course_data = course_raw_data.split(' ', 1)
        course_code = course_data[0].replace('\n', '').replace('\t', '')
        course_name = course_data[1].replace('\n', '').replace('\t', '')
        courses_dict[course_code] = course_name
    
    return courses_dict
