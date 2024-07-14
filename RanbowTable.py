import hashlib
import secrets


def decrypt():
    with open("database-teste.txt", "r") as file:
        for linha in file:
            with open("rainbowtable.txt", "r") as file2:
                for linha2 in file2:
                    hash_clear = linha2.strip()
                    hash_teste = hashlib.sha256(hash_clear.encode()).hexdigest()
                    if hash_teste == linha.strip():
                        print(f"{linha} = {linha2}")
                        break
# def debug():
#     with open("rainbowtable.txt", "r") as file:
#         for linhas in file:
#             hash1 = linhas.strip()
#             hash = hashlib.sha256(hash1.encode()).hexdigest()
#             print(hash)
            
# def register(passwd):
#     password_hashed = hashlib.sha256(passwd.encode()).hexdigest()
#     with open("database-teste.txt", "a") as file:
#         file.write(f"{password_hashed}\n")
        
if __name__ == "__main__":
    decrypt()
  