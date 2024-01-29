def solution(years):
    count=0
    for i in range(0,len(years)-1):
        if years[i]==years[i+1]:
            continue
        elif years[i]<years[i+1]:
            count+=1
        elif years[i]>years[i+1]:
            count+=2

    return count


def main():
    # Ask for the array
    input_string = input("Enter an array of numbers, separated by commas (e.g., 1, 2, 3): ")

    # Convert the string to an actual list of integers
    try:
        array = [int(item.strip()) for item in input_string.split(',')]
    except ValueError:
        print("Oops! That didn't look like a list of numbers. Let's try again.")
        return

    # Pass the array to the solution function
    print (solution(array))

if __name__ == "__main__":
    main()