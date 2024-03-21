import sys
from aitrios_qt.app import Main


def main() -> int:
    ret = 0

    app = Main(sys.argv)
    ret = app.exec()

    return ret

if __name__ == "__main__":
    sys.exit(main())
    pass