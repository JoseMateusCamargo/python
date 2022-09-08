# Anagrams check function

def is_anagram(one, two):
    return sorted(one) == sorted(two)


print(f'Anagrams: {is_anagram("python", "php")}')
