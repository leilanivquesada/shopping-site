"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

def read_customer_data_from_file(filepath):
    """Read melon type data and populate dictionary of melon types.

    Dictionary will be {id: Melon object}
    """

    customers = {}

    with open(filepath) as file:
        for line in file:
            (
                first_name,
                last_name,
                email,
                password
            ) = line.strip().split("|")



            customers[email] = Customer(
                first_name, last_name, email, password
            )

    return customers


def get_by_id(email):
    """Return a melon, given its ID."""

    # This relies on access to the global dictionary `melon_types`

    return customers[email]


# Dictionary to hold types of melons.
#
# Format is {id: Melon object, ... }

customers = read_customer_data_from_file("customers.txt")
