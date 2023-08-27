import re

text = "Contact us at support@example.com or info@example.org"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

email_addresses = re.findall(email_pattern, text, re.IGNORECASE)
print(email_addresses)

text = "The event will take place on 2023-08-31."
date_pattern = r"\b\d{4}-\d{2}-\d{2}\b"

dates = re.findall(date_pattern, text)
print(dates)

phone_numbers = ["123-456-7890", "555-1234", "800-555-1234", "999-9999", "435634"]
phone_pattern = r"^\d{3}-\d{3}-\d{4}$|^\d{3}-\d{4}$"

valid_numbers = [number for number in phone_numbers if re.match(phone_pattern, number)]
print(valid_numbers)
