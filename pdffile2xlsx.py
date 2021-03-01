from pdf2image import convert_from_path
import tempfile
import argparse
import glob
import os


def main(args):
    path = args.path if args.path is not None else "."
    extension = args.extension if args.extension is not None else "pdf"
    fmt = "png"
    with tempfile.TemporaryDirectory() as tmpdirname:
        for fname in glob.glob(path + "/*." + extension):
            print(fname)
            file_name = os.path.split(fname)[1]
            final_name = tmpdirname + "/" + file_name.replace(extension, fmt)
            convert_from_path(fname, 350, fmt=fmt, output_file=final_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--recursive", help="Search PDFs recursively", action="store_true")
    parser.add_argument("--path", help="Chose the origin directory", type=str)
    parser.add_argument("--extension", help="Allow to change the extensions", type=str)
    parser.add_argument("--out", help="Select the xlsx's output name", type=str)
    args = parser.parse_args()
    main(args)
