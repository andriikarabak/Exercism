def distance(strand_a: str, strand_b: str) -> int:
    """ Returns the Hamming difference between two DNA strands.

    Args:
        strand_a: first DNA strand.
        strand_b: second DNA strand.

    Returns:
        A number of the nucleotides which are different from their equivalent
        in the other string by comparing two DNA strands.

    Raises:
        ValueError: If two given DNA strands have different length.

    >>> distance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT')
    7
    """

    if len(strand_a) == len(strand_b):
        return sum(nucl_a != nucl_b for nucl_a, nucl_b in zip(strand_a, strand_b))
    else:
        raise ValueError('Two given DNA strands have to be the same length')