
import numpy as np

def get_view(r):
    view = arr[:r,:csize]
    return view

def display_view(view):
    assert(type(view) == np.ndarray), "View type must be an array."
    r = len(view)
    print('------ Get View -----')
    for i in range(r):
        print(arr[i, :csize])
    print('---------------------')

def modify_contents(r, value):
    for c in range(csize):
        arr[r, c] = value
    r_content = arr[r, :csize]
    return r_content

def write_to_file(view, filename):
    assert(type(view) == np.ndarray), "Parameter must be an array."

    # open file to read and write
    with open(filename, 'r+') as f:
        lines = f.readlines()

        # append to lines
        for i in range(len(view)):
            lines.append('{}\n'.format(view[i]))

        # write to file 
        for line in lines:
            f.write(line)
    
    return filename

def load_data(filename, view):
    # Read file
    with open(filename, 'r') as f:
        insert = []
        lines = f.readlines()
        for line in lines:
            # Clean data of unwanted chars
            bad_chars = ['\n', '[', ']']
            for char in bad_chars:
                line = line.replace(char, '')
            
            # Put data back into the memory
            line = line.split(' ')
            clean_data = []
            for i in line:
                num = int(i)
                clean_data.append(num)
            insert.append(clean_data)

    #     for i in range(len(insert)):
    #         for j in range(len(arr)):
    #             if arr[j, 0] == 0:
    #                 arr[j] = clean_data

    return view

def clean_file(filename):
    with open(filename, 'w') as f:
        f.write('')
    return filename


# --------- Main ----------
filename = 'binary_file.mem'
clean_file(filename)

# Step 1
rsize = 6
csize = 6
arr = np.zeros(shape=(rsize, csize), dtype='int32')

# Step 2
view_a = get_view(2)

# Step 3
modify_contents(0, 22)
modify_contents(1, 44)
view_a = get_view(2)

# Step 4
write_to_file(view_a, filename)

# Step 5
view_b = get_view(3)

# Step 6
view_b = load_data(filename, view_b)

# Step 7
modify_contents(2, 33)
display_view(view_b)
display_view(arr)
