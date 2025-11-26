import h5py, sys
p = r"week5-image-classifier/model/keras_model.h5"
try:
    with h5py.File(p, "r") as f:
        print("Opened:", p)
        def walk(g, path="/"):
            for k, v in sorted(g.items()):
                t = "Group" if isinstance(v, h5py.Group) else "Dataset"
                try:
                    shape = getattr(v, "shape", None)
                    dtype = getattr(v, "dtype", None)
                    print(path + k, ":", t, ("shape="+str(shape) if shape is not None else ""), ("dtype="+str(dtype) if dtype is not None else ""))
                except Exception as e:
                    print(path + k, ":", t, "(could not read shape/dtype)", e)
                if isinstance(v, h5py.Group):
                    walk(v, path + k + "/")
        walk(f)
except Exception as e:
    print("ERROR opening file:", e)
    sys.exit(1)
