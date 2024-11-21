#!/usr/bin/env python3
import hashlib
import time

# Função para minerar um bloco
def mine_block(data, difficulty):
    prefix = '0' * difficulty
    nonce = 0
    start_time = time.time()

    while True:
        block = f"{data}{nonce}"
        block_hash = hashlib.sha256(block.encode()).hexdigest()

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
    print("Iniciando a mineração...")
    block_data = input("Digite os dados do bloco: ")
    difficulty = int(input("Digite a dificuldade (ex: 4): "))
    mine_block(block_data, difficulty)

# Executa o script quando chamado
if __name__ == "__main__":
    main()
