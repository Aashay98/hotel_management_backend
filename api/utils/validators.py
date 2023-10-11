import re


class ValidationError(Exception):
    pass

# To check if it is a valid phone number
def isUSPhone(phone):
    if phone:
        orig_phone = phone
        phone = re.sub(r"\D", "", phone)
        num_chars = len(phone)
        if num_chars == 7:
            raise ValidationError(f"No area code provided: {orig_phone}")
        if num_chars < 10 or num_chars > 11:
            raise ValidationError(f"Invalid US phone number: {orig_phone}")
        if num_chars == 11 and phone[0] != '1':
            raise ValidationError(f"Invalid country code for US: {orig_phone}")
    return True

#format the phone number if it is a us phone number
def cleanUSPhone(phone):
    if phone:
        phone = re.sub(r"\D", "", phone)
        num_chars = len(phone)
        if num_chars == 10:
            phone = f"+1{phone}"
        if num_chars == 11:
            phone = f"+{phone}"
        assert isUSPhone(phone)
    return phone

#CHeck if the provided is valid email
def isValidEmail(value):
    if value:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(regex, value):
            raise ValidationError(f"Invalid Email address: {value}")
    return True
