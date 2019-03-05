import sys
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

def get_data(url):
    """
    Uses selenium webdriver to return the page source html

    Args:
        (str): url
    """
    opts = Options()
    opts.headless = True
    browser = Firefox(options=opts)

    try:
        if not url.startswith('http'):
            raise Exception('Must be a valid url')
    
        browser.get(url)
        source = browser.page_source
    
        return source
    
    except Exception as err:
        print(err)
        sys.exit(1)
    
    finally:
        browser.close()

if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group('required arguments')
    required.add_argument('-u', '--url', action='store', dest='url', required=True,
                          type=str, help='Enter in the url you want to scrape.')
    args = parser.parse_args()

    print(get_data(args.url))