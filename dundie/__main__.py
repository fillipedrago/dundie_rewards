import argparse

def load(filepath):
    """Loads data from filepath to the database"""
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError as e:
        print(f"File not found: {e}")


def main():
    parser = argparse.ArgumentParser(
    description= "Dundie Mifflin Rewards CLI",
    epilog="Enjoy and use with caution",
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load", "show", "send"),
        default="help",
        required=False
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="Filepath to load",
        default=None
    )
    args = parser.parse_args()

    try:
        globals()[args.subcommand](args.filepath)
    except KeyError:
        print("Subcommand is invalid")

    print("Executing entry point for dundie...")


if __name__ == "__main__":
    main()
