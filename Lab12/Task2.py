import time, csv, json, os

def load_books_csv(filename):
    with open(filename, newline='', encoding='utf-8') as f:
        return [{'title': r['title'], 'author': r['author']} for r in csv.DictReader(f)]

def load_books_json(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)

def linear_search(books, keyword):
    keyword = keyword.lower()
    return [b for b in books if keyword in b['title'].lower() or keyword in b['author'].lower()]

def binary_search(books_sorted, keyword):
    # Assumes books_sorted is sorted by title (case-insensitive)
    keyword = keyword.lower()
    left, right = 0, len(books_sorted) - 1
    results = []
    # Find leftmost match
    while left <= right:
        mid = (left + right) // 2
        title = books_sorted[mid]['title'].lower()
        if keyword in title:
            # Expand to find all matches
            l, r = mid, mid+1
            while l >= 0 and keyword in books_sorted[l]['title'].lower():
                l -= 1
            while r < len(books_sorted) and keyword in books_sorted[r]['title'].lower():
                r += 1
            results.extend(books_sorted[l+1:r])
            break
        elif keyword < title:
            right = mid - 1
        else:
            left = mid + 1
    return results

def build_hash_map(books):
    # Map every word in title/author to list of books
    hash_map = {}
    for b in books:
        words = set(b['title'].lower().split()) | set(b['author'].lower().split())
        for word in words:
            if word not in hash_map:
                hash_map[word] = []
            hash_map[word].append(b)
    return hash_map

def hash_search(hash_map, keyword):
    return hash_map.get(keyword.lower(), [])

def print_books(books, max_n=10):
    print(f"{'Title':<40} {'Author':<30}")
    print('-'*70)
    for b in books[:max_n]: print(f"{b['title'][:38]:<40} {b['author'][:28]:<30}")
    if len(books) > max_n: print(f"...and {len(books)-max_n} more results.")

def main():
    filename = input("Enter book dataset filename (CSV or JSON) [Enter for default]: ").strip()
    if not filename:
        candidates = [
            r"C:\Users\savin\OneDrive\Desktop\book.csv",
            r"C:\Users\savin\OneDrive\Desktop\AI Ass\LAB 12\boooks(Ai).csv",
            r"C:\Users\savin\OneDrive\Desktop\AI Ass\LAB 12\boooks(Ai).json",
        ]
        filename = next((p for p in candidates if os.path.exists(p)), '')
        if not filename:
            print("Default datasets not found.")
            return
    else:
        if not os.path.exists(filename):
            print("File not found.")
            return
    if filename.lower().endswith('.csv'):
        books = load_books_csv(filename)
    elif filename.lower().endswith('.json'):
        books = load_books_json(filename)
    else:
        print("Unsupported file format.")
        return

    print(f"Loaded {len(books)} books.")

    # Prepare for searches
    books_sorted = sorted(books, key=lambda b: b['title'].lower())
    hash_map = build_hash_map(books)

    while True:
        keyword = input("\nEnter keyword to search (or 'exit'): ").strip()
        if keyword.lower() == 'exit':
            break

        # Linear search
        t0 = time.time(); linear_results = linear_search(books, keyword); print(f"\nLinear Search: {len(linear_results)} results in {time.time()-t0:.6f} s")
        print_books(linear_results)

        # Binary search (title only)
        t0 = time.time(); binary_results = binary_search(books_sorted, keyword); print(f"\nBinary Search (title only): {len(binary_results)} results in {time.time()-t0:.6f} s")
        print_books(binary_results)

        # Hash search (word match)
        t0 = time.time(); hash_results = hash_search(hash_map, keyword); print(f"\nHash Search (word match): {len(hash_results)} results in {time.time()-t0:.6f} s")
        print_books(hash_results)

        print("\n--- Efficiency Comparison ---")
        print("Linear search: O(n), checks every entry.")
        print("Binary search: O(log n), but only finds exact substring matches in sorted titles.")
        print("Hash search: O(1) for word match, but only finds exact word matches in title/author.")

if __name__ == "__main__":
    main()
