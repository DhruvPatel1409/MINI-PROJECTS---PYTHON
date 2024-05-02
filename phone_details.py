import phonenumbers
from phonenumbers import geocoder,carrier,timezone
phone = input("Enter phone number with country code here : ")
phone_number = phonenumbers.parse(phone)

country_name =geocoder.description_for_number(phone_number,'en')
service_provider = carrier.name_for_number(phone_number,'en')
time_zone = timezone.time_zones_for_number(phone_number)

print(country_name)
print(service_provider)
print(time_zone)



