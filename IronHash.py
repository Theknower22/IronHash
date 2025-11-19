#!/usr/bin/env python3
import hashlib
import base64
import re
import sys
import time
import os

# ------------------------------------------
# 1) Detect hash type based on length
# ------------------------------------------
def detect_hash_type(hash_string):
    hash_string = hash_string.strip().lower()

    if not re.fullmatch(r"[a-f0-9]+", hash_string):
        return "❌ Invalid input: Hash must contain only hexadecimal characters."

    length = len(hash_string)
    types = {
        32: "MD5",
        40: "SHA1",
        56: "SHA224",
        64: "SHA256",
        96: "SHA384",
        128: "SHA512"
    }

    return f"Detected: {types.get(length, f'Unknown (length {length})')}"

# ------------------------------------------
# 2) Generate ANY hash type
# ------------------------------------------
def generate_hash(text, hash_type):
    hash_type = hash_type.lower()
    
    if hash_type == "md5":
        return hashlib.md5(text.encode()).hexdigest()
    elif hash_type == "sha1":
        return hashlib.sha1(text.encode()).hexdigest()
    elif hash_type == "sha256":
        return hashlib.sha256(text.encode()).hexdigest()
    elif hash_type == "sha512":
        return hashlib.sha512(text.encode()).hexdigest()
    elif hash_type.startswith("sha3_"):
        return getattr(hashlib, hash_type)(text.encode()).hexdigest()
    elif hash_type in ["blake2b", "blake2s"]:
        return getattr(hashlib, hash_type)(text.encode()).hexdigest()

    return "❌ Unsupported hash type"

# ------------------------------------------
# 3) Crack Hash using Wordlist
# ------------------------------------------
def crack_hash(hash_value, hash_type, wordlist_path):
    print("\n🔍 Starting hash cracking...\n")

    if not os.path.exists(wordlist_path):
        return "❌ Wordlist not found!"

    with open(wordlist_path, "r", errors="ignore") as f:
        words = f.readlines()

    total = len(words)

    for i, word in enumerate(words, 1):
        word = word.strip()
        attempt = generate_hash(word, hash_type)

        # Progress bar
        percent = int((i / total) * 100)
        print(f"\rProgress: [{percent}%] Trying: {word}", end="")

        if attempt == hash_value.lower():
            print("\n")
            return f"🎉 FOUND! → {word}"

    return "\n❌ Not found in wordlist."

# ------------------------------------------
# 4) Export result to file
# ------------------------------------------
def export_result(text, filename="results.txt"):
    with open(filename, "a") as f:
        f.write(text + "\n")
    return f"📁 Saved to {filename}"

# ------------------------------------------
# 5) Base64 Encode/Decode
# ------------------------------------------
def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    try:
        return base64.b64decode(text.encode()).decode()
    except:
        return "❌ Invalid Base64 string"

# ------------------------------------------
# Banner & Menu
# ------------------------------------------
def banner():
    print("\033[1;36m")
    print("╔═══════════════════════════════════════╗")
    print("║         🔐 Advanced Hash Toolkit       ║")
    print("╠═══════════════════════════════════════╣")
    print("║      by theknower | v2.0 | 2025        ║")
    print("╚═══════════════════════════════════════╝")
    print("\033[0m")

def menu():
    banner()
    print("1️⃣  Detect hash type")
    print("2️⃣  Generate hash")
    print("3️⃣  Crack hash using wordlist")
    print("4️⃣  Base64 Encode")
    print("5️⃣  Base64 Decode")
    print("6️⃣  Export last result")
    print("7️⃣  Exit")

# ------------------------------------------
# Main Program Loop
# ------------------------------------------
last_result = ""

while True:
    menu()
    choice = input("\nEnter choice: ").strip()

    if choice == "1":
        h = input("Enter hash: ")
        last_result = detect_hash_type(h)
        print(last_result)

    elif choice == "2":
        t = input("Enter text: ")
        ht = input("Enter hash type (md5/sha1/sha256/sha512/sha3_256/blake2b): ")
        last_result = generate_hash(t, ht)
        print("Result:", last_result)

    elif choice == "3":
        hv = input("Enter hash to crack: ")
        ht = input("Enter hash type: ")
        wl = input("Enter wordlist path: ")
        last_result = crack_hash(hv, ht, wl)
        print(last_result)

    elif choice == "4":
        t = input("Enter text: ")
        last_result = base64_encode(t)
        print("Base64:", last_result)

    elif choice == "5":
        t = input("Enter Base64 string: ")
        last_result = base64_decode(t)
        print("Decoded:", last_result)

    elif choice == "6":
        print(export_result(last_result))

    elif choice == "7":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid option")
