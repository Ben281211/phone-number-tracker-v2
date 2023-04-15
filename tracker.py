import phonenumbers
from phonenumbers import geocoder, carrier, timezone

while True:
    number = input("Enter phone number (or 'exit' to quit): ")
    if number.lower() == 'exit':
        break
    try:
        phone_number = phonenumbers.parse(number, None)
        print(f"Location: {geocoder.description_for_number(phone_number, 'en')}")
        print(f"Carrier: {carrier.name_for_number(phone_number, 'en')}")
        print(f"Time Zone: {timezone.time_zones_for_number(phone_number)}")
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Invalid phone number. Please try again.")
