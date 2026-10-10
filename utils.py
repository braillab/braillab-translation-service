import json

def load_json_map(lang_id: str):
    filepath = f"languages/{lang_id}.json"

    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data

def translate_sequence(text: str, lang_id: str):
    """
    input: text, lang_id
    output: result
    """
    full_lang = load_json_map(lang_id)
    has_contractions: bool = True if full_lang["language"]["grade_supported"] > 1 else False
    result = []
    text = str(text)

    words = text.split()

    for index, word in enumerate(words):
        in_number = False
        in_caps = False

        if index > 0:
            result.append(" ")

        if has_contractions:
            contractions = full_lang.get("contractions", {})
            if word in contractions:
                result.append(contractions[word])
                continue
    
        for i in range(len(word)):
            char = word[i]
            next_char = word[i + 1] if i + 1 < len(word) else None
            output, in_number, in_caps = translate_char(
                char, in_number, in_caps, full_lang, next_char
            )
            result.extend(output)
            
    cleaned_result = list(filter(None, result))
    return cleaned_result

def translate_char(braille_char: str, in_number: bool, in_caps: bool, full_lang: list, next_char: str):
    """
    input: char, is_in_number_sequence, is_in_mayus_sequence, full_lang, next_char
    output: braille_char, in_number, in_caps
    """

    if braille_char.isdigit():
        braille_char = full_lang["numbers"][braille_char]
        if not in_number:
            return [full_lang["indicators"]["number"], braille_char], True, False
        return [braille_char], True, False

    if braille_char.isalpha():
        prefix = []

        if braille_char.isupper() and not in_caps:
            if next_char.isupper():
                prefix = [full_lang["indicators"]["mayus"], full_lang["indicators"]["mayus"]]
                in_caps = True
            else:
                prefix = [full_lang["indicators"]["mayus"]]
        elif not braille_char.isupper():
            in_caps = False

        braille_char = full_lang["letters"][braille_char.lower()]

        return prefix + [braille_char], False, in_caps
        
    braille_char = full_lang["punctuation"][braille_char]
    return [braille_char], False, False
    
# TODO: to be build.
def get_braille_characters(dot_positions: list[int]):
    '''
    input: dot positions (array[int])
    output: character symbols (array[str])
    '''
    braille_map = {
        [1]: '⠁',
        [1,2]: '⠃',
        [1,3]: '⠉',
        [1,4,5]: '⠙',
        [1,5]: '⠑',
        [1,2,4]: '⠋',
    }