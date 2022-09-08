import phonenumbers
from phonenumbers import geocoder, carrier

p_number = phonenumbers.parse("+55119########")  # Phone number
carrier = carrier.name_for_number(p_number, lang='pt-br')
region = geocoder.description_for_number(p_number, lang='pt-br')

print(f"Carrier: {carrier}")
print(f"Region: {region}")
