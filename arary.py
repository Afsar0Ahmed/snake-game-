def loud(text):
    return text.upper()
def quit(text):
    return text.lower()
def heloo(func):
    text  = func("hello world ")
    print(text)
heloo(loud)
heloo(quit)



