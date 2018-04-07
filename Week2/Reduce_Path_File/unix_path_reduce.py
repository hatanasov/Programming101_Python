# path = '/../../etc/passwd/./..'


def reduce_file_path(path):
    path_to_dir = [directory for directory in path.split('/') if directory]
    reduced_pat = []
    for directory in path_to_dir:
        # if directory == '.':
        #     continue
        if directory == '..' and reduced_pat:
            reduced_pat.pop()
        else:
            if directory != '..' and directory != '.':
                reduced_pat.append(directory)

    reduced_pat = '/' + '/'.join(reduced_pat)
    return reduced_pat


# print(reduce_file_path(path))