import sys
from stats import get_words
from stats import get_chars
from stats import create_report

def get_book_text(filepath) :
    with open(filepath) as f:   
        file_content = f.read() 
    return file_content  

def main() :
    if len(sys.argv) > 1:
        text = get_book_text(sys.argv[1])
        n_words = get_words(text)
        n_chars = get_chars(text)
        report = create_report(n_chars, n_words)
        print(report)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



main()
