def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)

def character_count(file_contents):
    file_string = file_contents
    lowered_string = file_string.lower()
    count = {}
    for char in lowered_string:
        if char not in count:
            count[char] = 1
        else:
            count[char] +=1
    return count