def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # print(file_contents)

    def count_words(file):
        words = file.split()
        return len(words)
    # print (count_words(file_contents))

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

    def look_pretty(dictionary):
        sorted = []
        for key in dictionary:
            sorted.append({"char": key, "num": dictionary[key]})
        sorted.sort(reverse=True, key=sort_on)
        return sorted
    
    word_count = count_words(file_contents)
    characters = count_characters(file_contents)
    sorted_list = look_pretty(characters)

    print("--Book Report--")
    print(f"{word_count} words found in the text")
    print()
    for item in sorted_list:
         if not item["char"].isalpha():
             continue
         print(f"The '{item['char']}' character was found {item['num']} times")

    print()
    print("--End of Report--")

main()
