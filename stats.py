import sys

def get_words(text) :
    counter = len(text.split())
    return counter

def get_chars(text) :
    words = text.split()
    #chars = words.split()
    new_chars = {}
    for w in words:
        lower = w.lower()
        chars = []
        
        for c in lower:
            chars.append(c)

        for c in chars: 
            if c in new_chars:
                new_chars[c] += 1
            else:
                new_chars[c] = 1

    return new_chars

def create_report(chars, count) :
    char_list = []
    
    def sort_on(list):
        return list["num"]
    
    for c in chars:
        if c.isalpha():
            char_list.append({"char":c,"num":chars[c]})
    char_list.sort(reverse=True, key=sort_on)

    def print_chars(c_list):
        c_string = ""
        for i in range(len(c_list)):
            if i == len(c_list)-1:
                c_string += f"{c_list[i]["char"]}: {c_list[i]["num"]}"
            else:
                c_string += f"{c_list[i]["char"]}: {c_list[i]["num"]}\n"
        return c_string

    return f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {count} total words
--------- Character Count -------
{print_chars(char_list)}
============= END ===============
"""
