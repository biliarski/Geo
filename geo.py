from segpy.reader import create_reader
from segpy.writer import write_segy


import numpy as np


"""
Docs:
    Segpy https://segpy.readthedocs.io/en/latest/
    
    NumPy https://docs.scipy.org/doc/numpy-1.13.0/reference/index.html
"""


if __name__ == '__main__':
    with open('data/CUTE.sgy', 'rb') as segy_in_file:
        # The seg_y_dataset is a lazy-reader, so keep the file open throughout.
        seg_y_dataset = create_reader(segy_in_file)  # Non-standard Rev 1 little-endian
        print(seg_y_dataset.num_traces())
        # # Write the seg_y_dataset out to another file, in big-endian format
        # with open('seismic_big.sgy', 'wb') as segy_out_file:
        #     write_segy(segy_out_file, seg_y_dataset, endian='>')  # Standard Rev 1 big-endian

        data = []
        for i in range(0, seg_y_dataset.num_traces()):
            trace = seg_y_dataset.trace_samples(i)
            data.append(trace)

        data_matrix = np.array(data, np.int32)
        ## each row is a trace
        # print(data_matrix)
