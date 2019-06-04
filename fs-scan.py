import os

def getFolderSize(folder):
    path, dirs, files = next(os.walk(folder))

    total_size = os.path.getsize(folder)
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)

    print("{0}\t| {1}\t| {2}\t| {3}".format(len(files), len(dirs), total_size, path))
    return total_size

def getLabeledSize(size):

    B = "B"
    KB = "KB"
    MB = "MB"
    GB = "GB"
    TB = "TB"
    UNITS = [B, KB, MB, GB, TB]
    HUMANFMT = "%f %s"
    HUMANRADIX = 1024.

    for u in UNITS[:-1]:
        if size < HUMANRADIX : return HUMANFMT % (size, u)
        size /= HUMANRADIX

    return HUMANFMT % (size,  UNITS[-1])

print("Files\t| Dirs\t| Size\t| Path")

getFolderSize("D:/wspc/New folder")
