def word_count(text: str):
    words = text.split()
    return len(words)

def get_char_count(text: str) -> dict:
    result = {}
    for c in list(text):
        lower_case = c.lower()
        if lower_case in result:
            result[lower_case] += 1
        else:
            result[lower_case] = 1

    return result

class CharCount:
    def __init__(self, char:str, count:int):
        self.char = char
        self.count = count

def sort_and_order_char_count(dictionary: dict[str, int]) -> dict[str, CharCount]:
    result: dict[str, CharCount] = {}

    for (key, val) in sorted(dictionary.items(), key=lambda x: x[1], reverse=True):
        result[key] = CharCount(char=key, count=val)
    
    return result