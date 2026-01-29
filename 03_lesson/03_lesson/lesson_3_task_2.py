from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "redmi note 10s", "+79991111111"),
    Smartphone("Nokia", "XR", "+79992222222"),
    Smartphone("Samsung", "galaxy s21", "+79993333333"),
    Smartphone("iPhone", "16 Pro", "+79994444444"),
    Smartphone("Huawei", "p30 lite", "+79995555555")
]
for smartphone in catalog:
    print(f"{smartphone.brend} - {smartphone.model} - {smartphone.number}")
