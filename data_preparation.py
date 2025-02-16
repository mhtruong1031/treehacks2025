from random import choice

# Fragments patient dna into num_fragments fragments
def fragment_patient_dna(probability_dist_function, full_patient_gene: str, num_fragments: int, fragment_len: int) -> list:
    sample_indices = []
    dna_fragments  = []
    
    for i in range(num_fragments):
        sample_indices.append(choice()) # TODO: add choice arugument
        pass

    for index in sample_indices:
        dna_fragments.append(full_patient_gene[index, index+fragment_len])

    # use those indices to take chunks of the full patient gene

    # get num_fragments number of chunks

    # return a list


    
    return dna_fragments