# Fungsi untuk mengenkripsi teks menggunakan Vigenere Cipher
def encrypt_vigenere(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    
    for i in range(len(plain_text)):
        char = plain_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text

# Fungsi untuk mendekripsi teks menggunakan Vigenere Cipher
def decrypt_vigenere(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

# Contoh penggunaan enkripsi dan dekripsi Vigenere Cipher
key = "secretkey"
plain_text = "SYIFA"

encrypted_text = encrypt_vigenere(plain_text, key)
print("Teks terenkripsi:", encrypted_text)

decrypted_text = decrypt_vigenere(encrypted_text, key)
print("Teks terdekripsi:", decrypted_text)

# Simulasi login dengan enkripsi Vigenere Cipher
def login(username, password, key):
    # Mendekripsi password yang tersimpan
    stored_password = decrypt_vigenere(encrypted_password, key)
    
    if stored_password == password:
        print("Login berhasil!")
    else:
        print("Login gagal!")

# Simpan password yang sudah dienkripsi
encrypted_password = encrypt_vigenere("Password123", key)

# Coba login
login("user1", "Password123", key)