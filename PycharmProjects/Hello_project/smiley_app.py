
def emoji_converter(message):
    words= message.split(" ")
    emoji= {":)":"🥰", "):": "😇"}
    output= ""
    for word in words:
        output+= emoji.get(word, word) + " "
    return output


message= input(">" )
converted_message=emoji_converter(message)
print(converted_message)






