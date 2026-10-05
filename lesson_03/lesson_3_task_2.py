from smartphone import Smartphone

catalog = [Smartphone ("Samsung", "S20", "+79563251154"),
    Smartphone ("Nokia", "S150", "+79563252781"),
    Smartphone ("TECNO", "Nova9", "+79693258511"),
    Smartphone ("Realme", "18+", "+79584551531"),
    Smartphone ("I-Phone", "17", "+79563248561")]

for Smartphone in catalog:
    print("Брэнд - ", Smartphone.mark, "Модель - ", Smartphone.model, "Номер - ",Smartphone.number)
