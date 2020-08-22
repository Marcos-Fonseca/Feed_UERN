import urllib
import urllib.request as request

def _enableUserAgent():
    client = request.build_opener()
    client.addheaders = [(
        'User-agent',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    )] # User Agent
    request.install_opener(client)

def downloadXML(urls, directory='.database') -> list:
    print('[RSS] Baixando xmls ...') # log
    userAgentState = False

    x = 0
    while True:
        failed = []
        for url in urls:
            try:
                request.urlretrieve(url, f'{directory}/file{x}.xml')
                x += 1
            except urllib.error.HTTPError:
                print(f'[RSS] Erro ao tentar baixar da url: {url}')
                failed.append(url)

        if len(failed) > 0 and userAgentState == False:
            print(f'[RSS] Tentando baixar novamente usando user-agent')
            _enableUserAgent()
            userAgentState = True
            urls = failed
        else:
            break

    return [f'{directory}/file{i}.xml' for i in range(x)]
