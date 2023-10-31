from difflib import SequenceMatcher

def get_response(to_fix, openai, keep_punctuation=False, enable_logging=False):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": f"Q: Proofread the following sentence, without changing its structure, or making significant changes to words: '{to_fix}'. A: The correct form of this sentence is:"
        }]
    )
    
    result = response['choices'][0]['message']['content']
    result = result.strip()  #Remove whitespace (' example ' => 'example')

    result_no_punct = result.lower()
    result_no_punct = ''.join(filter(filter_punctuation, result_no_punct))

    similarity_score = get_similarity(to_fix, result)

    #Enable Logging
    if enable_logging:
        print(to_fix)
        print(result)
        print(similarity_score)

    #Optionally remove punctuation
    if keep_punctuation == False:
        result = result_no_punct
        result = result.strip()  #Remove whitespace (' example ' => 'example')

    #Saving grace to fix a single word that's incorrectly translated
    #All but one word must be identical, and the new word must be of a substantially different length
    to_fix_array = to_fix.split()
    result_array = result.split()
    errors = 0
    if len(to_fix_array) == len(result_array):
        for i in range(len(to_fix_array)):
            if to_fix_array[i] != result_array[i]:
                errors += 1
            if errors > 1:
                break

            if len(result_array[i])*2 <= len(to_fix_array[i]) or len(result_array[i])*0.5 > len(to_fix_array[i]):
                result_array[i] = to_fix_array[i]
        if errors == 1:
            result =" ".join(result_array)

    #Try the conversion again with an adjusted prompt if not good enough
    if is_similar_enough(to_fix, result, enable_logging=enable_logging):
        response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": f"Q: Fix the typos in the following sentence: '{to_fix}'. A: The correct form of this sentence is:"
        }]
        )
        result = result.strip()
        similarity_score = get_similarity(to_fix, result)

    #Give up and return original if we can't get a proper translation
    if is_similar_enough(to_fix, result, enable_logging=enable_logging):
        result = to_fix #Just return original string if the response dramatically alters the sentence's length

    result = result.lower()

    return result #Return fixed string

def is_similar_enough(to_fix, result, enable_logging=False):
    similarity_score = get_similarity(to_fix, result)
    return len(to_fix) * 1.5 < len(result) or len(to_fix) * 0.8 > len(result) or similarity_score < 0.65

def get_similarity(original, fixed, enable_logging=False):
    #Converts both strings to lowercase, and removes puncuation to make the comparison 'fairer'
    if enable_logging:
        print("Initial: " + fixed)
    original = original.lower()
    fixed = fixed.lower()
    fixed = ''.join(filter(filter_punctuation, fixed))
    if enable_logging:
        print("Final: " + fixed)
    return SequenceMatcher(None, original, fixed.lower()).ratio()

def filter_punctuation(char):
    return char.isalpha() or char.isspace()