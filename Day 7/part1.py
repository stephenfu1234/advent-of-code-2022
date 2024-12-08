import time

def read_file(filename):
    return open(filename).read()

def solve(filename):
    start_time = int(time.time() * 1000)

    raw_input = read_file(filename)

    # split on $ to have a list of commands
    # ls output can then be parsed separately
    # remove opening $ which wont get removed by the split \n$
    data = [[j.strip().replace('$ ', '') for j in i.split('\n')] for i in raw_input.split('\n$')]

    # model the filesystem as a dict
    # each element is either a number (size of a given file) or another string which is a key to another directory
    filesystem = parse_output(data, 0, {}, '')

    # replace sub directories with the total filesize by looking up respective keys
    # start with the lowest level directories and then build out back to root
    ordered_keys_by_dir_depth = get_dir_path_ordered_by_depth_desc(filesystem)

    for _, key in ordered_keys_by_dir_depth:
        # if directory contains another dir then look up its total size and replace the reference
        for item in filesystem[key]:
            if type(item) == str:
                dir_size = sum(filesystem[item])

                # now replace the reference
                for dir, contents in filesystem.items():
                    for idx, ref_item in enumerate(contents):
                        if ref_item == item:
                            contents[idx] = dir_size
                            filesystem[dir] = contents
   
    # filtered_dirs contains the directories that are less than 100000 in filesize
    filtered_dirs = list(filter(filter_dir, filesystem.items()))

    # now sum up the directory filesizes
    res = [filesizes for dir, filesizes in filtered_dirs]
    print(sum(sum(res, [])))
    
    end_time = int(time.time() * 1000)
    print(f'Time taken for {filename} (ms): {end_time - start_time}')

# recursive function
def parse_output(output, idx, filesystem, current_path):
    if len(output) < idx + 1:
    # if it's the last output then finish
        return filesystem

    # print(idx, ':', 'cwd:', current_path, ':',output[idx][0])

    # split current line into individual strings
    tokens = output[idx][0].split(' ')
    if tokens[0] == 'cd':
        new_path = get_new_path(current_path, tokens[1])

        # then move to the directory
        return parse_output(output, idx + 1, filesystem, new_path)

    if tokens[0] == 'ls':
        # get all the dirs/files and add details to filesystem
        # ['ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d']
        # get all the contents which is 2nd element onwards and store in filesystem
        # print('performing ls, got', output[idx][1:])

        dir_contents = []
        for item in output[idx][1:]:
            if item.split(' ')[0] == 'dir':
                full_dir_path = (current_path + '/' + item.split(' ')[1]).replace('//', '/')
                dir_contents.append(full_dir_path)
            else:
                filesize = item.split(' ')[0]
                dir_contents.append(int(filesize))
        
        filesystem[current_path] = dir_contents

        # then move to next command
        return parse_output(output, idx + 1, filesystem, current_path)

def get_new_path(current_path, dir_cmd):
    # goto root directory
    if dir_cmd == '/':
        return '/'
    
    if dir_cmd == '..':
        # remove all text after last /
        before, _,_ = current_path.rpartition('/')
        return before
    
    # build up current working path, remove double slash which is introduced at root dir
    return (current_path + '/' + dir_cmd).replace('//', '/')

def get_dir_path_ordered_by_depth_desc(filesystem):
    # order filesystem keys by total directories desc
    ordered_keys_by_dir_depth = []

    # for each key count how many directories
    for key in filesystem.keys():
        ordered_keys_by_dir_depth.append([key.count('/'), key])

    # then order by the count of dirs
    ordered_keys_by_dir_depth.sort(key = lambda x: x[0])

    # then order desc
    ordered_keys_by_dir_depth.reverse()
    return ordered_keys_by_dir_depth

def filter_dir(contents):
    return sum(contents[1]) < 100000

solve('test.txt')
solve('input.txt')