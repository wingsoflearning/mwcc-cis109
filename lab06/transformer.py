import argparse

# 2. Transformation Functions
def transform_upper(text):
    """Returns the string in all caps."""
    return text.upper()

def transform_lower(text):
    """Returns the string in all lowercase."""
    return text.lower()

def get_word_count(text):
    """Returns the number of words in the string."""
    return len(text.split())

def filter_short(text, min_length):
    """Returns the string only if it is longer than min_length; otherwise, returns None."""
    if len(text) > min_length:
        return text
    return None

# Main execution block
def main():
    parser = argparse.ArgumentParser(description="Bulk Text Transformer Utility")
    
    parser.add_argument(
        "--action", 
        choices=["upper", "lower", "count", "filter"], 
        required=True, 
        help="The transformation action to perform"
    )
    parser.add_argument(
        "--data", 
        required=True, 
        help="A comma-separated list of strings to transform"
    )
    parser.add_argument(
        "--min-length", 
        type=int, 
        default=5, 
        help="Minimum length constraint used for the 'filter' action (default: 5)"
    )

    args = parser.parse_args()

    items = args.data.split(',')

    # Loop through the list and process each item
    for item in items:
        clean_item = item.strip() 
        
        if args.action == "upper":
            result = transform_upper(clean_item)
            print(result)
            
        elif args.action == "lower":
            result = transform_lower(clean_item)
            print(result)
            
        elif args.action == "count":
            result = get_word_count(clean_item)
            print(f"'{clean_item}' word count: {result}")
            
        elif args.action == "filter":
            result = filter_short(clean_item, args.min_length)
            if result is not None:
                print(result)

if __name__ == "__main__":
    main()