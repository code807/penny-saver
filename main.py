from fastapi import FastAPI
from random import choice
import string

FIXED_FIRST_WORD: bool = True
PHRASES_FILE_PATH: str = "data/phrases.txt"
WORDS_FILE_PATH: str = "data/words.txt"
DATA_ERROR_FALLBACK: str = "pennyless"


def load_data(filename) -> list[str]:
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return [DATA_ERROR_FALLBACK]


app: FastAPI = FastAPI()
phrases: list[str] = load_data(PHRASES_FILE_PATH)
words: list[str] = load_data(WORDS_FILE_PATH)


@app.get("/penny-saver")
@app.get("/penny-saver/")
async def translate():
    phrase: str = choice(phrases)
    return phrase.format(*random_substitution_words(phrase))


def random_substitution_words(text: str) -> list[str]:
    random_words: list[str] = []
    fixed_word = FIXED_FIRST_WORD

    for placeholder_component in string.Formatter().parse(text):
        field_name: str | None = placeholder_component[1]
        if field_name is None:
            continue

        random_words.append(words[0] if fixed_word else choice(words))
        fixed_word = False

    return random_words


def test_translate():
    async def _test_translate():
        print()
        for _ in range(10):
            print(await translate())

    import asyncio
    asyncio.run(_test_translate())
