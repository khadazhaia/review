# Implement a function that removes the email from each string in a LIST.
# Return the empty list if an empty list is provided.
# Return -1 if an improper data type is provided.
def remove_domain(email: list[str]) -> list[str]:
    """
    A function to remove the email domain from the input list

    Args:
        email (list[str]): the list of emails
    Returns:
        list[str]: The list with modified strings
    """
    
    if email == [""]:
           return email
    first_half = []
    for e in email:
        if e == str(e) and "@" in e:
            removed = e.split("@")
            first_half.append(removed[0])
        elif e == str(e) and "@" not in e:
            return email
        else:
             return -1
    return first_half
        
print(remove_domain(['1@yahoo.com']))