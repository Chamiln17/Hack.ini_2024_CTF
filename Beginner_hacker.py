from random import seed, shuffle
from Crypto.Util.number import bytes_to_long

def decrypt(ciphertext, key):
    decrypted = bytearray([ciphertext[i] ^ key[i % len(key)] for i in range(len(ciphertext))])
    return decrypted

# Encrypted flag received from the encryption process
enc = b'\x9e\xddO\xd2\xc3\xddG\xd8\\\xc5\\\xd0\x97\xa2]\xd9\xdd\xc0D\xd9\\\xf3I\xe7L'

# Known parts of the original and shuffled flags
known_original = "shellmates{"
known_shuffled = "shellmates{"

# Extract the known parts of the original and shuffled flags
original_flag = "shellmates{redacted}"
shuffled_flag = "shellmates{abcdefg}"  # Replace with the actual shuffled flag

# XOR the known parts to obtain a partial key
partial_key = bytearray([ord(original_char) ^ ord(shuffled_char) for original_char, shuffled_char in zip(known_original, known_shuffled)])

# Complete the key by appending the remaining random bytes
mykey = partial_key + bytearray([0] * (12 - len(partial_key)))

# Decrypt the ciphertext
decrypted_flag = decrypt(enc, mykey)

# Unshuffle the decrypted flag
seed(bytes_to_long(mykey))
shuffled_list = list(decrypted_flag.decode()[11:-1])
shuffle(shuffled_list)
rest_of_the_flag = "".join(shuffled_list)

# Combine the known and recovered parts to get the original flag
original_flag = known_original + rest_of_the_flag

print("Decrypted Flag:", original_flag)
