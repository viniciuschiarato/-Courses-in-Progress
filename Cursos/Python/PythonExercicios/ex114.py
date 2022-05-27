def website_test_access(url):
    import urllib.request
    try:
        site = urllib.request.urlopen(url)

    except urllib.error.URLError:
        print(f'The site "{url}" is currently not accessible.')

    else:
        print('Ok. I can access.')
        read = str(input('Read? [Y/N]: ')).strip().upper()
        if read == 'Y':
            print(site.read())


website_test_access('https://www.python.org/')
