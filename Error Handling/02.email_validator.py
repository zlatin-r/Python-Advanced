from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbol(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidNameError(Exception):
    pass


MIN_NAME_LENGTH = 4
VALID_DOMAINS = ".com", ".bg", ".net", ".org"

pattern_name = r"\w+"

email = input()

while email != "End":

    if email.count("@") > 1:
        raise MoreThanOneAtSymbol("Email must contain only one '@' symbol")
    elif "@" not in email:
        raise MustContainAtSymbol("Email must contain @")
    elif len(email.split("@")[0]) <= MIN_NAME_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")
    elif email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d for d in VALID_DOMAINS)}")
    elif findall(pattern_name, email.split("@")[0]) != email.split("@")[0]:
        raise InvalidNameError("Name must contain only letters, digits and underscores")

    print("Email is valid")

    email = input()
