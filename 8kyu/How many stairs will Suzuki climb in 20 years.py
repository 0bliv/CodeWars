def stairs_in_20(stairs):
    flat_list = [item for sublist in stairs for item in sublist]
    return 20 * sum(flat_list)