from queue import Queue
import requests
import threading
import sys


def get_words(wordlist: str,
              resume: str = None,
              extensions: list = None) -> Queue:
    """ Returns words Queue to test on the target.

        A list of extensions can be passed to this function to test when making requests. Default is None.
    
        The resume variable is the last path the brute forcer tried, and will resume from in case of network interruption. """

    def extend_words(word: str) -> None:
        if "." in word:
            words.put(f'/{word}')
        else:
            words.put(f'/{word}/')

        for extension in extensions:
            words.put(f'/{word}{extension}')

    with open(wordlist) as fh:
        raw_words = fh.read()

    found_resume = False
    words = Queue()
    for word in raw_words.split():
        if resume is not None:
            if found_resume:
                extend_words(word)
            elif word == resume:
                found_resume = True
                print(f'Resuming wordlist from: {resume}')
        else:
            print(word)
            extend_words(word)

    return words


def dir_bruter(
    words: Queue,
    target_url: str,
    agent:
    str = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"
) -> None:
    """ """
    headers = {'User-Agent': agent}
    while not words.empty():
        url = f'{target_url}{words.get()}'

        try:
            r = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
            sys.stderr.write('x'); sys.stderr.flush()
            continue

        if r.status_code == 200:
            print(f'\nSuccess ({r.status_code}: {url})')
        elif r.status_code == 404:
            sys.stderr.write('.');sys.stderr.flush()
        else:
            print(f'{r.status_code} => {url}')

if __name__ == '__main__':
    AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"
    TARGET = "http://testphp.vulnweb.com"
    THREADS = 5
    EXTENSIONS = ['.php', '.bak', '.orig', '.inc']
    WORDLIST = "all.txt"

    words = get_words(WORDLIST, None, EXTENSIONS)

    print('Press return to continue.')
    sys.stdin.readline()
    for _ in range(THREADS):

        t = threading.Thread(target=dir_bruter(words, TARGET, AGENT,))
        t.start()
    
