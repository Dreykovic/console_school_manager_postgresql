import datetime

def validate_text(text):
    """Valide si le texte ne contient que des lettres alphabétiques.

    Args:
        text (str): Texte à valider.

    Returns:
        int: Retourne 1 si le texte est valide, 0 sinon.

    """
    if text.isalpha():
        return 1
    else:
        return 0

def validate_phone_number(phone_number):
    """Valide si le numéro de téléphone est valide.

    Args:
        phone_number (int or str): Numéro de téléphone à valider.

    Returns:
        int: Retourne 1 si le numéro de téléphone est valide, 0 sinon.

    """
    phone_number = str(phone_number)
    if len(phone_number) == 8:
        if phone_number.isdigit():
            if phone_number[0] in ("9", "7") and phone_number[1] in (
                "0",
                "1",
                "2",
                "3",
                "6",
                "7",
                "8",
                "9",
            ):
                return 1
    else:
        return 0

def validate_number(number):
    """Valide si le nombre est un entier.

    Args:
        number (int or str): Nombre à valider.

    Returns:
        int: Retourne 1 si le nombre est valide, 0 sinon.

    """
    number = str(number)
    if number.isdigit():
        return 1
    else:
        return 0

def validate_date(my_date):
    """Valide si la date est au format YYYY-MM-DD.

    Args:
        my_date (str): Date à valider.

    Returns:
        int: Retourne 1 si la date est valide, 0 sinon.

    """
    date_format = "%Y-%m-%d"

    try:
        datetime.datetime.strptime(my_date, date_format)
    except ValueError:
        return 0
    return 1
