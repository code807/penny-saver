from fastapi import FastAPI
from random import choice
import string

FIXED_FIRST_WORD: bool = True
PHRASES: list[str] = [
    "You know what they {}, {}, {}.",
    "You know what they say, a {} {} is a {} {}.",
    "A {} penny is {} and {} {}.",
    "A {} {} is a {} {}.",
    "A {} {} is a {} towards a {}.",
    "A {} {} is a {} you can {} again.",
    "A wise {} {} is a wise {} {}.",
    "Better a small {} than an empty {}."
]
WORDS: list[str] = [
    "penny",
    "gained",
    "saved",
    "earned",
    "given",
    "real",
    "pennied",
    "say",
    "said",
    "walked",
    "eaten",
    "pretty",
    "penniless",
    "dream",
    "lose"
]

app: FastAPI = FastAPI()

@app.get("/penny-saver")
@app.get("/penny-saver/")
async def translate():
    phrase: str = choice(PHRASES)
    return phrase.format(*random_substitution_words(phrase))


def random_substitution_words(text: str) -> list[str]:
    random_words: list[str] = []
    fixed_word = FIXED_FIRST_WORD

    for placeholder_component in string.Formatter().parse(text):
        field_name: str | None = placeholder_component[1]
        if field_name is None:
            continue

        random_words.append(WORDS[0] if fixed_word else choice(WORDS))
        fixed_word = False

    return random_words


def test_translate():
    async def _test_translate():
        print()
        for _ in range(10):
            print(await translate())

    import asyncio
    asyncio.run(_test_translate())
