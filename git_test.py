print("Hello World!")
data = input("Please type in something: ")
words = data.split(' ')
for word in words:
    try:
        print(f"number of char in this word is: {len(word)}")
    except:
        print("number of char in this word is: {}".format(len(word)))
    print(word)
