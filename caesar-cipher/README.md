# Caesar Cipher in Python

A simple and clean implementation of the Caesar Cipher written in Python.  
This project allows you to encrypt and decrypt messages using a configurable shift, while preserving spaces, numbers, and symbols.

---

## About the Project

The Caesar Cipher is one of the oldest and simplest encryption techniques.  
It works by shifting each letter of the alphabet by a fixed number of positions.

This implementation focuses on:
- Clarity of logic
- Proper handling of edge cases
- Readable and maintainable code
- Clean project structure suitable for GitHub

---

## Features

- Encrypt messages using a shift value
- Decrypt messages using the same shift
- Automatic wrap-around using modular arithmetic
- Preserves spaces, numbers, and symbols
- Case-insensitive input
- ASCII art logo displayed on startup

---


## How It Works

- Letters are shifted within the alphabet using modular arithmetic
- If the shift exceeds the alphabet length, it wraps around automatically
- Characters that are not part of the alphabet are kept unchanged

Example:
- Input: `hello world`
- Shift: `5`
- Output: `mjqqt btwqi`

---

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/your-username/caesar-cipher.git
   ```

2. Navigate into the project directory:
   ```
   cd caesar-cipher
   ```

3. Run the program:
   ```
   python main.py
   ```

4. Follow the prompts to:
   - Choose encryption or decryption
   - Enter your message
   - Enter the shift number

---

## Example

```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
attack at dawn
Type the shift number:
3

Here is the encoded result: dwwdfn dw gdzq
```

---

## Requirements

- Python 3.x
- No external libraries required

---

## Notes

- The cipher only applies to lowercase English letters
- All other characters are preserved to ensure reversibility
- The project is intended for educational purposes

---

## License

This project is released under the MIT License.
