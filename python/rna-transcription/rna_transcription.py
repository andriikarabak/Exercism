def to_rna(dna_strand:str) -> str:
    """ Returns a RNA complement to a given DNA strand.

    Args:
        dna_strand: DNA strand.

    Returns:
        A RNA strand which is formed by replacing each nucleotide in
        a given DNA strand with its complement.

    Raises:
        ValueError: If a given DNA is invalid - includes not only
        adenine (A), cytosine (C), guanine (G) and thymine (T) nucleotides.

    >>> to_rna('ACCGGTT')
    UGGCCAA
    """

    if set(dna_strand) - set ('ACGT') != set(''):
        raise ValueError('A given DNA has to include only ACGT nucleotides.')
    else:
        return dna_strand.translate(str.maketrans('ACGT','UGCA'))