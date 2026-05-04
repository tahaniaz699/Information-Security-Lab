import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Combines block contents into a single string to hash
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash)
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print(f"Index: {block.index} | Hash: {block.hash[:20]}... | Prev: {block.previous_hash[:20]}...")

# --- Execution ---
my_coin = Blockchain()
my_coin.add_block("Sent 1.5 BTC to Alice")
my_coin.add_block("Sent 0.5 BTC to Bob")
my_coin.add_block("Sent 10 BTC to Charlie")

print("--- Initial Chain ---")
my_coin.display_chain()

print("\n--- Tampering with Block 1 ---")
my_coin.chain[1].data = "Sent 100 BTC to Hacker" # Modifying data
print(f"New Hash of Block 1: {my_coin.chain[1].calculate_hash()[:20]}...")
print(f"Stored Previous Hash in Block 2: {my_coin.chain[2].previous_hash[:20]}...")

