from segpy.reader import create_reader
from segpy.writer import write_segy


if __name__ == '__main__':
    with open('data/CUTE.sgy', 'rb') as segy_in_file:
        # The seg_y_dataset is a lazy-reader, so keep the file open throughout.
        seg_y_dataset = create_reader(segy_in_file)  # Non-standard Rev 1 little-endian
        print(seg_y_dataset.num_traces())
        # # Write the seg_y_dataset out to another file, in big-endian format
        # with open('seismic_big.sgy', 'wb') as segy_out_file:
        #     write_segy(segy_out_file, seg_y_dataset, endian='>')  # Standard Rev 1 big-endian