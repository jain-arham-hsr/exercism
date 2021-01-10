def find_anagrams(word, candidates):
    return [candidate for candidate in candidates if "".join(sorted(candidate.lower())) == "".join(sorted(word.lower())) and candidate.lower() != word.lower()]
