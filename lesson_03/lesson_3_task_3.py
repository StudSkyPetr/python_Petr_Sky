from Address import Address
from Mailing import Mailing

to_address = Address("467028", "г.Самара", "ул.Квартал 6", 5, 32)
# адрес получателя
from_address = Address("629603", "Муравленко", "ул.Муравленко", 35, 45)
# адрес отправителя

Mailing = Mailing(from_address, to_address, 789, "7895-7586252")

print(f"Почтовое отправление №  {Mailing.track}  отправленное ")
print(f"от   {Mailing.from_address.format_adr()}")
print(f"передано по адресу   {Mailing.to_address.format_adr()}")
print(f"стоимость отправления {Mailing.cost} рублей")
