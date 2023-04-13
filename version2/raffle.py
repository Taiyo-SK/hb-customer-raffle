"""Randomly pick customer and print customer info"""

from random import choice
from customers import get_customers_from_file

def pick_winners(customers):
    """Picks a random winner from our list of customers."""

    chosen_customer = choice(customers)

    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")

def run_raffle():
    """Run the weekly raffle."""

    customers = get_customers_from_file('customers.txt')
    pick_winners(customers)

if __name__ == "__main__":
    run_raffle()