from fastapi import FastAPI

from random import choice, shuffle

words = ["apple", "penny", "gained", "saved", "earned", "given", "real", "pennied", "say", "said", "walked", "eaten", "pretty", "penniless", "day"]
phrases = [
    [3, "you know what they {0}, {1}, {2}"],
    [4, "you know what they say, a {0} {1} is a {2} {3}"],
    [4, "a {0} {1} is a {2} {3}"],
    [4, "a {0} penny is {1} and {2} {3}"]
]

app = FastAPI()

@app.get("/penny-saver")
@app.get("/penny-saver/")
async def translate():
    randomphrase = choice(phrases)
    count = randomphrase[0]
    phrasewords = []
    pennycount = 1
    for penny in range(pennycount):
        phrasewords.append("penny")
    for word in range(count-pennycount):
        phrasewords.append(choice(words))
    shuffle(phrasewords)
    final = randomphrase[1]
    for n in range(count):
        final = final.replace("{"+str(n)+"}", phrasewords[n])
    return final
