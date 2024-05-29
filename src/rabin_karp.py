def hash_str(pattern, base, divisor):
    hash_value = 0
    for char in pattern:
        hash_value = (hash_value * base + ord(char)) % divisor
    return hash_value

def rabin_karp(haystack, needle, base=256, divisor=101):
    if not needle or not haystack or len(haystack) < len(needle):
        return []

    needle_hash = hash_str(needle, base, divisor)
    haystack_hash = hash_str(haystack[:len(needle)], base, divisor)
    indices = []

    for i in range(len(haystack) - len(needle) + 1):
        if haystack_hash == needle_hash and haystack[i:i + len(needle)] == needle:
            indices.append(i)
        if i < len(haystack) - len(needle):
            haystack_hash = (haystack_hash * base - ord(haystack[i]) * pow(base, len(needle), divisor) + ord(haystack[i + len(needle)])) % divisor

    return indices