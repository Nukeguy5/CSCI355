import numpy as np
def get_view(r):
    view_a = arr[:r,:csize]
    return view_a

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
    np.save(filename, view)
    return filename

def load_file(filename):
    temp_mem = np.load(filename+'.npy')
    mem = []
    for row in temp_mem:
        mem.append(row)
    return mem

# def clean_file(filename):
#     with open(filename, 'w') as f:
#         f.write('')
#     return filename


# --------- Main ----------
filename = 'binary_file'
# clean_file(filename)

# Step 1
rsize = 6
csize = 6
arr = np.zeros(shape=(rsize, csize), dtype='int32')

# Step 2
view_a = get_view(2)
display_view(view_a)

# Step 3
modify_contents(0, 22)
modify_contents(1, 44)
view_a = get_view(2)

# Step 4
write_to_file(view_a, filename)

# Step 5
view_b = get_view(3)
load_file(filename)
# Step 6
modify_contents
