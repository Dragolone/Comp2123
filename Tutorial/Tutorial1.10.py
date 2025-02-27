k = int(input("K should between 1 and n\n"))

def identical_consecutive_characters(characters:str, k:int) -> bool:
    temp = characters[0]
    count = 0
    for char in characters:

        if temp == char:
            count += 1
            if count == k:
                return True
            continue

        else:
            temp = char
            count = 1
    return False

print(identical_consecutive_characters("abcalkjdfccssklsajfklsssssss", k))
