def count_words(text: str) -> int:
    'Returns the number of words in text'
    return len(text.split())

def compute_character_frequency_dict(text: str) -> dict[str, int]:
    '''
    Returns a dict where the keys are unique characters
    and the values are their frequencies within the text. 
    All letters are converted to lowercase.
    '''
    char_freq: dict[str: int] = dict()

    for char in text:
        lower_char = char.lower()
        if lower_char in char_freq:
            char_freq[lower_char] += 1
        else:
            char_freq[lower_char] = 1
    
    return char_freq

def make_sorted_frequencies(char_freq: dict[str, int]) -> list[dict[str, str|int]]:
    '''
    Returns a list of dictionaries containing the character and frequency 
    sorted in reverse order by frequency. 
    '''
    freq_list: list[dict[str, str|int]] = list()

    char: str
    frequency: int
    for char, frequency in char_freq.items():
        if char.isalpha():
            freq_list.append({"letter": char, "count": frequency})
    
    #Sorts in reverse order based on frequencies
    freq_list.sort(reverse=True, key=lambda char_dict_entry: char_dict_entry["count"])
    
    return freq_list


