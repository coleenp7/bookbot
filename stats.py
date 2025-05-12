#counts the words in a file using the blanks spaces as seperators
def count_words(file):
    words = file.split()
    return len(words)
# print (count_words(file_contents))

#counts the characters in a file based on the lower case versions
def count_characters(contents):
    lowered_contents = contents.lower()
    dict = {}
    for character in lowered_contents:
        if character in dict:
            dict[character] += 1
        else:
            dict[character] = 1
    return dict            
# print (count_characters(file_contents))

def sort_on(d):
    return d["num"]

#puts the character counts in order
def look_pretty(dictionary):
    sorted = []
    for key in dictionary:
        sorted.append({"char": key, "num": dictionary[key]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted