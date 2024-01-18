import multiprocessing

def calculate_square(num):
    square = num * num
    
    return num, square

def main():
    # Certain samples list of numbers
    numbers = [1, 2, 3, 4, 5]

    # Creating a multiprocessing Pool
    with multiprocessing.Pool() as pool:
        # Use starmap to apply the function to each number in parallel
        results = pool.starmap(calculate_square, [(num,) for num in numbers])

    # Printing the results
    for num, square in results:
        print(f"Number: {num}, Square: {square}  ")


# Calling main methods
if __name__ == "__main__":
    main()
