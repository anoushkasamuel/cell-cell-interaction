import argparse

def main():
    parser = argparse.ArgumentParser(description="Apply biological filters to Xenium data")
    parser.add_argument("--input", required=True, help="Path to .h5ad file")
    parser.add_argument("--contact-radius", type=float, default=20.0)
    parser.add_argument("--output", required=True, help="Path to save filtered .h5ad")
    args = parser.parse_args()

    print(f"Input: {args.input}")
    print(f"Contact radius: {args.contact_radius}")
    print(f"Output: {args.output}")

if __name__ == "__main__":
    main()
