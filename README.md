# 🔐 Hash Toolkit (2025)

A powerful and simple Python toolkit for:

- Detecting hash types
- Generating MD5 hashes
- Cracking hashes using a wordlist (MD5, SHA1, SHA256, SHA512)

This project is designed for cybersecurity students and researchers who want a lightweight and fast hashing utility.

---

## 📂 Project Structure

```
├── LICENSE
├── IronHash.py
├── results.txt
├── wordlists/
│   └── /usr/share/wordlists/rockyou.txt
└── .gitignore
```

---

## ⚙️ Features

- Auto-detects common hash types using length
- Supports MD5, SHA1, SHA256, SHA384, SHA512
- Crack hashes with any wordlist
- Works on Windows, Linux, and macOS
- Easy to customize and extend

---

## 🧰 Installation

### 🔸 Windows

1. Install Python 3 from the official website.
2. Open **CMD**.
3. Navigate to the project directory:

```
cd path\to\IronHash
```

4. Run the tool:

```
python IronHash.py
```

---

### 🔸 Linux / Kali Linux

1. Install Python 3 if not installed:

```
sudo apt install python3
```

2. Navigate to the project location:

```
cd /path/to/IronHash
```

3. Run the tool:

```
python3 IronHash.py
```

---

## 🔍 Usage Examples

### ✔️ Detecting a hash type
```
Enter hash: 5f4dcc3b5aa765d61d8327deb882cf99
Detected: MD5
```

### ✔️ Generating an MD5 hash
```
Enter text: hello
MD5: 5d41402abc4b2a76b9719d911017c592
```

### ✔️ Cracking a hash using a wordlist
```
Enter hash: 5f4dcc3b5aa765d61d8327deb882cf99
Enter wordlist path: wordlists/example.txt
[✔] Found (MD5): password
```

---

## 📜 License

This project uses the MIT License. See the `LICENSE` file for details.

---

## ⭐ Contributing

Feel free to submit pull requests or open issues to improve the project.

---

## ❤️ Author

Developed by **theknower (2025)**.
