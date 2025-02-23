def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    print(f"{get_num_words(file_contents)} words found in the document")
    print(character_count(file_contents))

from stats import get_num_words

from stats import character_count

if __name__ == "__main__":
    main()
