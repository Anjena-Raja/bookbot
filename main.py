from pathlib import Path
import stats
import sys

def main() -> None:
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    
    book_path = Path(sys.argv[1])
    book_text: str = get_book_text(book_path)
    num_words = stats.count_words(book_text)
    char_freq_dict: dict[str, int] = stats.compute_character_frequency_dict(book_text)
    sorted_frequencies: list[dict[str, str|int]] = stats.make_sorted_frequencies(char_freq_dict)
    print(pretty_print_str(book_path, num_words, sorted_frequencies))


def get_book_text(file_path: Path) -> str:
    file: 'File Object' = file_path.open('r')
    try:
        return file.read()
    finally:
        file.close()

def pretty_print_str(path_str: str, num_words: int, sorted_frequencies: list[dict[str, str|int]]) -> str:
    output_str = '============ BOOKBOT ============\n'
    output_str += f'Analyzing book found at {path_str}...\n'
    output_str += '----------- Word Count ----------\n'
    output_str += f'Found {num_words} total words\n'
    output_str += '--------- Character Count -------\n'
    for freq_entry in sorted_frequencies:
        output_str += f'{freq_entry["letter"]}: {freq_entry["count"]}\n'
    output_str += '============= END ==============='
    return output_str

if __name__ == '__main__':
    main()