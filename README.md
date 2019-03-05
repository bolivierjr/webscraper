# Webscraper

This is a webscraper that uses selenium webdriver to get the whole page source.

## Installation

You will need python 3.6 or higher.

```
git clone https://github.com/bolivierjr/webscraper.git
cd webscraper
pip3 install -r requirements.txt
```

You will also need to install the latest geckodriver([here](https://github.com/mozilla/geckodriver/releases)) and firefox.

For the geckodriver:

```
wget https://github.com/mozilla/geckodriver/releases/download/v0.23.0/geckodriver-v0.23.0-linux64.tar.gz
tar -xzvf geckodriver*.tar.gz
mv geckodriver ~/.local/bin/  OR  mv geckodriver /usr/local/bin/
rm geckodriver*.tar.gz
```

Install firefox from your normal repo.

## Usage

`python3 scrape.py -u "http://google.com"`

OR

`python3 scrapy.py --url "http://google.com"`
