# mURL
*A simple Python script providing a cURL alike command line interface to Mollom's REST API.*

## Installation

### No Python yet?

1. Download and install Python from http://python.org/download
1. Add `/path/to/pythonX` and `/path/to/pythonX/scripts` directories to your PATH environment variable.
1. Download and install Setuptools from https://pypi.python.org/pypi/setuptools via `ez_setup.py`:

        $ wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
        $ python ez_setup.py

1. Download and install Pip from https://pypi.python.org/pypi/pip via `get-pip.py`:

        $ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
        $ python get-pip.py


### mURL

1. Install dependent library: oauth2

        $ pip install oauth2

1. Run `python murl.py --help` to confirm.


## Usage Example

Replace `'mypublickey'` and `'myprivatekey'` with your API keys.

    $ python murl.py -k mypublickey -s myprivatekey /v1/site/18cd366b6b7de98e33be3b901430b4ab

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <siteResponse>
        <code>200</code>
        <site>
            <publicKey>...</publicKey>
            <privateKey>...</privateKey>
            <url>http://example.com</url>
            <email>...</email>
            ...
        </site>
    </siteResponse>
