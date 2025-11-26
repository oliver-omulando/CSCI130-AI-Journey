import h5py, json, sys
p = r"week5-image-classifier/model/keras_model.h5"
try:
    with h5py.File(p, "r") as f:
        print("Opened:", p)
        print("Root attributes:")
        for k, v in f.attrs.items():
            try:
                vv = v.decode("utf-8") if isinstance(v, bytes) else v
            except Exception:
                vv = str(v)
            print(" -", k, ":", vv)
        # model_config can be either an attribute or a dataset
        if "model_config" in f.attrs:
            print("\\nFound 'model_config' in attributes:")
            mc = f.attrs["model_config"]
            try:
                mc = mc.decode("utf-8") if isinstance(mc, bytes) else mc
            except Exception:
                pass
            print(mc[:2000])
        elif "model_config" in f:
            print("\\nFound 'model_config' dataset:")
            try:
                raw = f["model_config"][()]
                raw = raw.decode("utf-8") if isinstance(raw, (bytes, bytearray)) else raw
                print(raw[:2000])
            except Exception as e:
                print("Could not read model_config dataset:", e)
        else:
            print("\\nNo 'model_config' found in attrs or datasets.")
except Exception as e:
    print("ERROR:", e)
    sys.exit(1)
