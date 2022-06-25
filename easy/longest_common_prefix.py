def longest_common_prefix_sol1(strs: list[str]) -> str:
    if len(strs) == 0:
        return ""

    first, *remaining = strs

    for idx, char in enumerate(first):
        for string in remaining:
            if idx >= len(string) or string[idx] != char:
                return first[:idx]

    return first
