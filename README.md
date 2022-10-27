# U-Campus Web Scraper

Small python web scraper utility created to get a list of available engineering courses of the Faculty of Physical and Mathematical Sciences of the University of Chile. It may be extended with new scripts for different use cases.

## Description

Currently there is only one python script that uses beautiful soup to scrap the [U-Campus FCFM course catalogue site](https://ucampus.uchile.cl/m/fcfm_catalogo/) to get both the code and the name of most available courses during a certain year and semester.

It supports most departments (and therefore courses codes) and dumps all the data to a `.json` file.

Also, please do not spam requests to the website 0-0

## Getting Started

### Main Dependencies

* Python3
* BeautifulSoup
  
### Installing

1. Clone this repository
2. Install the necessary modules via pip

    ```bash
    pip install -r requirements.txt
    ```

### Scripts

Here you can check how to use each script.

```bash
cd scripts
```

#### Courses | Usage

Scraps the U-Campus FCFM courses catalogue for a given year and semester.

```py
# usage, semester: 1 (autumn) | 2 (spring)
python courses.py <int:year> <int:semester>

# example, available courses for 2022 spring
python courses.py 2022 2
```

The data gets dumped to `output/courses.json`.

#### Courses | Help

**Could not get data for a certain department:**

This is just a warning but is relatively common since not all departments have courses each semester. It may also happen that the code beign used does not match a page for given year and semester.

You can modify codes or add support for more departments by adding them to the dictionary located at `scripts/scrapers/utilities/departments.py`

**Could not get requested data:**

Make sure that you are connected to the internet. It may also happen that U-Campus is not available, so might want to try again later.

## License

This project is licensed under the GPL 3.0 License - see the LICENSE.md file for details

## Contributing

Feel free to give any ideas or contribute to the project.
