import hashlib
import argparse

def crack_hash(hash_to_crack, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            word = line.strip()
            hashed_word = hashlib.md5(word.encode()).hexdigest()
            print(f"[-] Trying: {word} -> {hashed_word}")
            if hashed_word == hash_to_crack:
                print(f"[+] Match found! Password is: {word}")
                return True
    print("[-] No match found in wordlist.")
    return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🔓 Simple MD5 Hash Cracker")
    parser.add_argument("-H", "--hash", required=True, help="Target MD5 hash to crack")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file")
    args = parser.parse_args()

    crack_hash(args.hash, args.wordlist)
