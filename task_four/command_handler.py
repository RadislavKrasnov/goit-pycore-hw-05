"""Helper bot command handler"""

from error_handler import input_error_decorator

@input_error_decorator(
    value_error_message='Give me name and phone please.'
)
def add_contact(args: list, contacts: dict) -> str:
    """Adds contact into dictionary.

    Args:
        args:
            List with user name and phone.
        contacts:
            Dictionary with contacts (name and phone).
    
    Returns:
        String with notification that contact is added.

    Raises:
       ValueError: Not enough values to unpack (expected 2, got 0).
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error_decorator(
    value_error_message='Give me name and phone please.'
)
def change_contact(args: list, contacts: dict) -> str:
    """Change contact in dictionary.

    Args:
        args:
            List with user name and phone.
        contacts:
            Dictionary with contacts (name and phone).
    
    Returns:
        String with notification that contact is changed.

    Raises:
       ValueError: Not enough values to unpack (expected 2, got 0).
    """
    name, phone = args
    contacts[name] = phone
    return "Contact changed"

@input_error_decorator(
    key_error_message = 'Give me name please'
)
def show_phone(args: list, contacts: dict) -> str:
    """Shows phone number from dictionnary by user name.

    Args:
        args: 
            List containing the user's name.
        contacts:
            Dictionary with contacts (name and phone).
    
    Returns:
        A phone number string.

    Raises:
       KeyError: if no key found on the contacts dictionary.
    """
    name = args[0]
    return contacts[name]

def show_all(contacts: dict) -> None:
    """Shows all contacts from the dictionary.

    Args:
        contacts:
            Dictionary with contacts (name and phone).
    
    Returns:
        None.
    """
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
