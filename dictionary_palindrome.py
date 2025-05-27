from datetime import datetime
from Palindromes import is_palindrome

start_time = datetime.now()

_crypt_toll = 0
_total_grants = 13

codeword_map = {
    1: 'EchoOne', 2: 'Phantom2', 3: 'Cipher3', 4: 'NodeFour',
    5: 'DeltaFive', 6: 'HexaSix', 7: 'Sev3nKey', 8: 'OctoShade',
    9: 'NinerRun', 10: 'TenFold', 11: 'Prime11', 12: 'TwelveX', 13: 'Red13',
}

test_cases = [
    ("racecar", True, 2),
    ("hello", False, 2),
    ("A man, a plan, a canal, Panama", True, 3),
    ("Doc, note I dissent. A fast never prevents a fatness. I diet on cod.", True, 3),
    ("Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man — a prisoner up to new era", True, 3)
]

for text, expected, mk in test_cases:
    result = is_palindrome(text)
    if result == expected:
        print(f"✓ Test passed for: '{text[:30]}...' (+{mk})")
        _crypt_toll += mk
    else:
        print(f"✗ Test failed for: '{text[:30]}...'")

end_time = datetime.now()

print(f"\nTest session started at: {start_time.strftime('%H:%M:%S')}")
print(f"Test session ended at: {end_time.strftime('%H:%M:%S')}")
print(f"Access Code: {codeword_map.get(_crypt_toll, 'Unclassified')}")
