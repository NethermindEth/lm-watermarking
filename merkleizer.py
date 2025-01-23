# TODO: Create merkleizer that takes in greenlist tokens and can create proofs within MMR following spec document

class Merkle:
    def __init__(self, leaves, height, hash_func):
        self.leaves = leaves,
        self.height = height,
        # TODO: only accept SNARK friendly hashes (for now only poseidon)
        self.hash = hash_func
        self.root = None

    def get_leaves(self):
        return self.leaves

    def get_height(self):
        return self.height

    def get_hash(self):
        return self.hash

    # TODO: Should return current root
    def get_root(self):
        return self.root

    # TODO: create merkle tree and return root
    def construct_root(self):
        pass

    # TODO: create merkle proof for leaf
    def generate_proof(self, leaf):
        pass

    # TODO: take proof and verify it with the current root
    def verify_proof(self, proof):
        pass

    # TODO: Should print merkelizer information
    def print_info(self):
        print("Merkle")
        print("Leaves:", self.leaves)
        print("Height:", self.height)
        print("Hash function:", self.hash)



if __name__ == "__main__":
    merkle = Merkle([], 10, "poseidon")
    merkle.print_info()