from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    dict = defaultdict(list)
    for s in strs:
        fr = [0] * 26
        for c in s:
            fr[ord(c) - ord('a')] += 1
        key = tuple(fr)
        dict[key].append(s)
    return dict.values()

if __name__ == '__main__':
    strs = input("Enter strings: ")
    strs = strs.split()
    anagrams = group_anagrams(strs)
    print(list(anagrams))