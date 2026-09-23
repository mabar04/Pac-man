import sys
from src import ParsingError, ParserClass


def main() -> None:
    if len(sys.argv) != 2:
        raise ParsingError("Parsing Error: Missing/Extra arguments")
    parser = ParserClass(sys.argv[1])
    parser.validate(parser.load())


if __name__ == "__main__":
    try:
        main()
    except ParsingError as e:
        print(f"Parsing error: {e}")
    except Exception as e:
        print(e)
