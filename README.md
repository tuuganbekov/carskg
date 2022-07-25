# BeautifulSoup Web Scraping Tutorial

Simple Web Scraping Tutorial for beginners using Python's [BeautifulSoup](<https://www.crummy.com/software/BeautifulSoup/bs4/doc/> "BeautifulSoup") library.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements.
```bash
pip install -r requirements.txt
```

## Usage
1) Create postgres database 
2) Create .env file and write 
```
DB_NAME=database_name
HOST=database_host
PORT=database_port
DBUSER=database_user
PASSWORD=database_user
```
3) Run
```bash
python3 parser.py
```
And it will parse [cars.kg](<https://cars.kg/offers?direction=sale&vendor=57fa24ee2860c45a2a2c0905&model=58b876792860c409036ea149&generation=&price_from=&price_to=&year_from=&year_to=2021&running_length_from=&running_length_to=&kuzov=&capacity_from=&capacity_to=&color=&city=/>), write it to database and generate cars.json file with parsed data.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
