import gzip
import os
import shutil


# filepath = "A:\\var\\log\\" # Windows test
filepath = "/var/log/" # Path to folder whose contents should be compressed


for dirpath, dirnames, filenames in os.walk(filepath): # go trough contents of filepath
    for filename in filenames:
        if filename.endswith(".gz"):   # Ignore files that are already compressed
            continue
        base, extension = os.path.splitext(filename)
        if not os.path.exists(filepath + base + extension + '.gz'):
            with open(dirpath + base + extension, 'rb') as f_in:    # compress eligible files and
                with gzip.open(filepath + base + extension + '.gz', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
                    f_in.close()
                    f_out.close()
                    os.unlink(dirpath + base + extension)
                    continue
        else:  # file exists
            ii = 1
            while True: # iterrate until unused name is found
                new_name = os.path.join(filepath + base + " (" + str(ii)+ ")"+ extension + '.gz')
                if os.path.exists(new_name):
                    ii += 1
                    continue
                with open(dirpath + base + extension, 'rb') as f_in: # compress file with unused name
                    with gzip.open(new_name, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                        f_in.close()
                        os.unlink(dirpath + base + extension)
                        ii += 1
                        break
