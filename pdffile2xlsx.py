import argparse


def main(args):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--recursive", help="Search PDFs recursively", action="store_true")
    parser.add_argument("--path", help="Chose the origin directory", type=str)
    parser.add_argument("--out", help="Select the xlsx's output name", type=str)
    main(args)
