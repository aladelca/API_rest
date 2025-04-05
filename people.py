from datetime import datetime
from flask import make_response, abort
def get_timestamp():
    """
    Returns the current timestamp in ISO format.
    """
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "Smith": {
        "fname": "Alice",
        "lname": "Smith",
        "timestamp": get_timestamp(),
    },
    "Johnson": {
        "fname": "Bob",
        "lname": "Johnson",
        "timestamp": get_timestamp(),
    },
    "Brown": {
        "fname": "Charlie",
        "lname": "Brown",
        "timestamp": get_timestamp(),
    },
}

def read():
    return [PEOPLE[key] for key in PEOPLE.keys()]

def create(person):
    """
    Adds a new person to the PEOPLE dictionary.
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)
    
    if lname not in PEOPLE and lname is not None:
        PEOPLE[lname] = {
            "fname": fname,
            "lname": lname,
            "timestamp": get_timestamp(),
        }
        return make_response(
            f"{lname} added successfully", 201
        )
    else:
        abort(
            406,
            f"Person with last name {lname} already exists or last name is missing",
        )

def read_one(lname):
    """
    Retrieves a person from the PEOPLE dictionary by last name.
    """
    if lname in PEOPLE:
        person = PEOPLE.get(lname)
    
    else:
        abort(404, f"Person with last name {lname} not found")
    
    return person

def update(lname, person):
    """
    Updates a person's information in the PEOPLE dictionary.
    """
    if lname in PEOPLE:
        PEOPLE[lname]["fname"] = person.get("fname")
        PEOPLE[lname]["timestamp"] = get_timestamp()
        return PEOPLE[lname]
    else:
        abort(404, f"Person with last name {lname} not found")

def delete(lname):
    """
    Deletes a person from the PEOPLE dictionary by last name.
    """
    if lname in PEOPLE:
        del PEOPLE[lname]
        return make_response(
            f"{lname} deleted successfully", 200
        )
    else:
        abort(404, f"Person with last name {lname} not found")




