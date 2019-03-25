print("Hello World!")
data = "My name is omer"
words = data.split(' ')
for word in words:
    try:
        print(f"number of char in this word is: {len(word)}")
    except:
        print("number of char in this word is: {}".format(len(word)))
    print(word)
