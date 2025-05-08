def is_intuitive(element, abreviation):
    """
    Brandon is learning the periodic table!
    
    However, he doesn’t like some of the elements because the symbol of the element contains letters which are not present in the name of the element.
    He finds this to be unintuitive, especially because in other contexts, he expects abbreviations to not introduce random letters.

    Given a string and a proposed abbreviation, determine if Brandon would find it intuitive.

    Brandon finds an abbreviation intuitive if and only if:

    Every letter that appears in the abbreviation appears in the original string.

    Any letter could be lower or uppercase to start, but your return statement will be case sensitive.

    The first paramater of the function will be a string with an element name. The second will be a proposed abbreviation.

    TODO: For each test case, if all the letters in the abbreviation appear in the name, return a line containing the string “YES”. Otherwise, return a line containing the string “NO”.
    """

    element_lower = element.lower()
    for char in abreviation.lower():
        if char not in element_lower:
            return "NO"
    return "YES"

# Sample Problem
if __name__ == "__main__":
    print(is_intuitive("Oxygen", "Ogn"))  # Print YES
    print(is_intuitive("Oxygen", "Od"))   # Print NO

# Run pytest test_problem_2.py to test the function