from difflib import SequenceMatcher

def get_response(to_fix, model, keep_punctuation=False, enable_logging=False):
    response = model(f"Q: Proofread the following sentence, without changing its structure, or making significant changes to words: '{to_fix}'. A: The correct form of this sentence is:", stop=["is:", "\n"], max_tokens=32, echo=True)
    #(+40) Q: What is the correct spelling of '{to_fix}' A:
    #(+64) Q: Update the following sentence to fix any typos: '{to_fix}' A:
    #(+114) Q: Proofread the following sentence, without changing its structure, or making significant changes to words: '{to_fix}' A:

    result = response['choices'][0]['text']

    end_index = len(to_fix) + 153 #NOTE: To update this if the prompt is changed, subtract 8 ({to_fix}) from the new string's length
    result = result[end_index:].strip()
    similarity_score = get_similarity(to_fix, result)

    if enable_logging:
        print(to_fix)
        print(result)
        print(similarity_score)

    if(keep_punctuation == False):
        result = result.lower()
        result = ''.join(filter(filter_punctuation, result))

    result = result.strip() #Remove whitespace (' example ' => 'example')

    if len(to_fix) * 1.5 < len(result) or len(to_fix) * 0.8 > len(result) or similarity_score < 0.65:
        return to_fix #Just return original string if the response dramatically alters the sentence's length
    else:
        return result #Return fixed string
    
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