from difflib import SequenceMatcher

def get_response(to_fix, model):
    response = model(f"Q: What is the correct spelling of '{to_fix}' A:", stop=["Q:", "\n"], max_tokens=32, echo=True)
    
    result = response['choices'][0]['text']

    end_index = len(to_fix) + 40 #NOTE: To update this if the prompt is changed, subtract 8 ({to_fix}) from the new string's length
    result = result[end_index:].strip()
    similarity_score = get_similarity(to_fix, result)
    print(to_fix)
    print(result)
    print(similarity_score)
    if len(to_fix) * 1.5 < len(result) or len(to_fix) * 0.8 > len(result) or similarity_score < 0.65:
        return to_fix #Just return original string if the response dramatically alters the sentence's length #TODO: Possibly check the similarity of the characters
    else:
        return result #Return fixed string
    
def get_similarity(original, fixed):
    #TODO: Consider removing grammatical symbols from fixed result
    return SequenceMatcher(None, original, fixed.lower()).ratio()