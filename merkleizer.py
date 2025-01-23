# TODO: Create merkleizer that takes in greenlist tokens and can create proofs within MMR following spec document

class Merkle:
    def __init__(self, leaves, height, hash_func):
        self.leaves = leaves,
        self.height = height,
        self.hash = hash_func

    def print_info(self):
        print("Merkle")
        print("Leaves:", self.leaves)
        print("Height:", self.height)
        print("Hash function:", self.hash)


if __name__ == "__main__":
    merkle = Merkle([], 10, "sha256")
    merkle.print_info()