# ————————————————————————————————-------
#   Name: Zhiyuan Lu
#   ID: 1579050
#   CMPUT 274, Fall 2018
#
#   Assignment #1: Huffman Coding
# ---------------------------------------
import bitio
import huffman
import pickle


def read_tree(tree_stream):
    '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
      tree_stream: The compressed stream o read the tree from.

    Returns:
      A Huffman tree root constructed according to the given description.
    '''
    # read in the Huffman tree and construct the object "tree".
    tree = pickle.load(tree_stream)
    return tree.root


def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.

    Returns:
      Next byte of the compressed bit stream.
    """

    node = tree  # keep the current node value of the tree when traverse the tree
    try:
        while True:
            # if TreeLeaf object is found, stop traverse the tree
            # and the value of the byte is returned.
            if isinstance(node, huffman.TreeLeaf):
                return bytes([node.value])
            # read one bit at a time
            read_bit = bitreader.readbit()
            # if 0 is found, set the node to tree.left
            # if 1 is found, set the node to tree.right
            if read_bit == 0:
                node = node.left
            elif read_bit == 1:
                node = node.right
    except (EOFError, TypeError):
        return None


def decompress(compressed, uncompressed):
    '''First, read a Huffman tree from the 'tree_stream' using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.

    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.
    '''
    # read in the compressed file
    rd_tree = read_tree(compressed)
    # read the bits of the compressed file
    bit_read = bitio.BitReader(compressed)
    while True:
        # use the decode_byte function to decode the compressed file
        byte_value = decode_byte(rd_tree, bit_read)
        if byte_value is None:
            break
        else:
            # write the byte_value to uncompressed file
            uncompressed.write(byte_value)


def write_tree(tree, tree_stream):
    '''Write the specified Huffman tree to the given tree_stream
    using pickle.

    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    '''

    pickle.dump(tree, tree_stream)


def compress(tree, uncompressed, compressed):
    '''First write the given tree to the stream 'tree_stream' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.

    Flush the bitwriter after writing the entire compressed file.

    Args:
      tree: A Huffman tree.
      uncompressed: A file stream from which you can read the input.
      compressed: A file stream that will receive the tree description
          and the coded input data.
      tree_stream: A file stream where the tree data should be dumped.
    '''
    # write the tree to compressed file
    bit_value = huffman.make_encoding_table(tree.root)
    write_tree(tree, compressed)
    # write the bits to compressed file
    writer = bitio.BitWriter(compressed)
    while True:
        # read 1 bit one of a time in uncompressed file
        b = uncompressed.read(1)

        if not b:
            break
        byte_value = ord(b)
        coded = bit_value[byte_value]
        # Iterate the tuple in dictionary's value,
        # write 1 if 'bit' is true, 0 if 'bit' if false
        for c in coded:
            writer.writebit(c)
    # write the end symbol
    for end_char in bit_value[None]:
        writer.writebit(end_char)
    writer.flush()
