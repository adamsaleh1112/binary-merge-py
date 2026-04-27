import struct

def merge_binaries(f1_name, f2_name, out_name):
    fmt, size = 'i', 4
    with open(f1_name, 'rb') as f1, open(f2_name, 'rb') as f2, open(out_name, 'wb') as out:
        # Load the first pair
        b1, b2 = f1.read(size), f2.read(size)

        while b1 and b2:
            # if file1 num < file2 num
            if struct.unpack(fmt, b1)[0] <= struct.unpack(fmt, b2)[0]:
                out.write(b1)
                b1 = f1.read(size)
            # if file1 num > file2 num
            else:
                out.write(b2)
                b2 = f2.read(size)

        # writing the remainder of file 1
        out.write(b1 + f1.read())
        # writing the remainder of file 2
        out.write(b2 + f2.read())

merge_binaries('sorted1.bin', 'sorted2.bin', 'merged.bin')
print("Done")
