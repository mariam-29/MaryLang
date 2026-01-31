import MaryLang
while True:
    text= input("MaryLang >> ")
    result, error = MaryLang.run(text)
    if error:
        print(str(error))
    else :
        print(result)
