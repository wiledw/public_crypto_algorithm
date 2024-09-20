def compute_merkle_tree_hash(certificates, K):
    """
    Compute the Merkle Tree hash for given certificates and modulus K.

    :param certificates: List of certificate values
    :param K: Modulus value for hash computation
    :return: Hash of the file (root of the Merkle Tree)
    """
    # Compute the initial hashes for individual certificates
    hashes = [c % K for c in certificates]

    # Recursively combine the hashes to compute the upper level hashes until we have the final hash
    while len(hashes) > 1:
        # Combine each pair of hashes and apply the modulus
        print(hashes)
        hashes = [(hashes[i] + hashes[i + 1]) % K for i in range(0, len(hashes), 2)]

    # The last remaining hash is the root hash of the Merkle Tree
    return hashes[0]


# For the given example in the second image, let's compute the hash
certificates_example = [5, 20, 115, 98]  # C1 to C4 values
# certificates_example = [9, 72, 199, 134, 200, 400, 600, 800] # C1 to C4 values
modulus_K_example = 32  # Given K value
print(compute_merkle_tree_hash(certificates_example, modulus_K_example))  # This should give us the hash of the file
