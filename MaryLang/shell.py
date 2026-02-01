from runner import run
while True:
    text = input("MaryLang >> ")

    if text.strip() == "":
        continue

    result, error = run(text)

    if error:
        print(error)
    else:
        print(result)