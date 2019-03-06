import sys
import logging
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def get_data(url):
    """
    Uses selenium webdriver to scrape html from a page.

    Args:
        url(str) - The url of the site to scrape.

    Returns:
        (str) - Returns the whole html source.
    """
    try:
        if not url.startswith('http'):
            raise Exception('Must be a valid url')

        opts = Options()
        opts.headless = True

        with Firefox(options=opts) as browser:
            browser.get(url)
            source = browser.page_source

            return source

    except Exception as err:
        logging.error(f'{err}', exc_info=True)
        print(f'ERROR: {err}. Check error.log for tracestack.')
        sys.exit(1)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    required = parser.add_argument_group('required arguments')
    required.add_argument('-u', '--url', action='store', dest='url', required=True,
                          type=str, help='Enter in the url you want to scrape.')
    args = parser.parse_args()

    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='error.log',
                        datefmt='%d-%b-%y %H:%M:%S')

    source = get_data(args.url)
    print(source)
