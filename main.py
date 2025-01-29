def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    print(f"{word_count(file_contents)} words")

def word_count(file_contents):
    words = file_contents.split()
    return len(words)
    

if __name__ == "__main__":
    main()
