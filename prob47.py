__author__ = 'Vince'

"""Caesar Shift cypher. I think that this could use a little work in
the way I manipulate the strings. Seems a little messier than I expected."""

def caesar_trans(message, shift):
    """Translates an encrypted message"""
    message = list(" ".join(message.splitlines()))
    print message
    for indx in range(len(message)):
        char_num = ord(message[indx])
        # If the character is a letter, decode it.
        if 64 < char_num < 123:
            trans_num = char_num - shift
            # Check that we don't go below 'A'. Correction if we do.
            if trans_num < 65:
                trans_num += 26
            message[indx] = chr(trans_num)
        else:
            message[indx] = chr(char_num)
    return "".join(message)

def main():
    inp = open('test.txt')
    n_and_shift = inp.readline().split()
    n = int(n_and_shift[0])
    key = int(n_and_shift[1])
    mess = "".join(inp.readlines())
    print mess
    print caesar_trans(mess, key)

if __name__ == "__main__":
    main()