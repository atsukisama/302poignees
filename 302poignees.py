import sys

CUSTOM_ERROR_CODE = 84


def main():
    if len(sys.argv) > 3:
        print ' '.join(sys.argv)
        sys.exit(0)
    elif len(sys.argv) > 2:
        print ' '.join(sys.argv)
        sys.exit(0)
    elif '-h' in sys.argv or '--help' in sys.argv:
        # todo Print usage
        sys.exit(0)
    else:
        # todo Print usage
        sys.exit(CUSTOM_ERROR_CODE)


if __name__ == '__main__':
    main()
