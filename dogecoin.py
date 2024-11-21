import hashlib
import time

def scrypt_hash(data):
    """
    Simulação de hash baseada em Scrypt. 
    (Obs.: Para mineração real, uma biblioteca Scrypt otimizada é necessária.)
    """
    return hashlib.sha256(data.encode()).hexdigest()

# Função para minerar um bloco
def mine_block(data, difficulty):
    prefix = '0' * difficulty
    nonce = 0
    start_time = time.time()

    while True:
        # Combina os dados com o nonce
        block = f"{data}{nonce}"
        block_hash = scrypt_hash(block)

        # Verifica se o hash atende à dificuldade
        if block_hash.startswith(prefix):
            end_time = time.time()
            print(f"\nBloco minerado!")
            print(f"Hash: {block_hash}")
            print(f"Nonce: {nonce}")
            print(f"Tempo: {end_time - start_time:.2f} segundos")
            break

        nonce += 1

# Função principal
def main():
    print("Iniciando a mineração de Dogecoin...")
    block_data = input("Digite os dados do bloco: ")
    difficulty = int(input("Digite a dificuldade (ex: 4): "))
    mine_block(block_data, difficulty)

if __name__ == "__main__":
    main()
