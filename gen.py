def flat_generator(list_of_lists):
    flat_list = []
    for item in list_of_lists:
        for k in item:
            flat_list.append(k)
            yield k
