import re
import requests

from decorators import benchmark, logging, counter, memo


@memo
@counter
@logging
@benchmark
def fibonacci(n: int):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


@memo
@counter
@logging
@benchmark
def word_count(word, url='https://www.gutenberg.org/files/2638/2638-0.txt'):
    raw = requests.get(url).text
    processed_book = re.sub('[\W]+', ' ', raw).lower()
    cnt = len(re.findall(word.lower(), processed_book))

    return f"Cлово {word} встречается {cnt} раз"


if __name__ == "__main__":
    print(word_count('whole', url='https://www.gutenberg.org/files/2638/2638-0.txt'))

    print(word_count('this', url='https://www.gutenberg.org/files/2638/2638-0.txt'))
    print(word_count('whole', url='https://www.gutenberg.org/files/2638/2638-0.txt'))