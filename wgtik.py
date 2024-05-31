def kenaRazia(tanggal, data_kendaraan):
    lokasi_ganjil_genap = ["Gajah Mada", "Hayam Wuruk", "Sisingamangaraja", "Panglima Polim", "Fatmawati", "Tomang Raya"]
    pelanggaran = []

    if tanggal < 1 or tanggal > 31:
        return "Tanggal harus berada antara 1 sampai 31"

    for kendaraan in data_kendaraan:
        if kendaraan['type'] == "Mobil":
            plat = kendaraan['plat']
            plat_number = int(plat.split()[1])
            rute_kendaraan = kendaraan['rute']
            is_ganjil_genap = plat_number % 2 == 0

            for lokasi in lokasi_ganjil_genap:
                if lokasi in rute_kendaraan and not is_ganjil_genap:
                    pelanggaran.append({"name": kendaraan['name'], "tilang": tanggal})
                    break

    return pelanggaran

data_kendaraan = [
    {
        "name": "Denver",
        "plat": "B 2791 KDS",
        "type": "Mobil",
        "rute": ["TB Simatupang", "Panglima Polim", "Depok", "Senen Raya"]
    },
    {
        "name": "Toni",
        "plat": "B 1212 JBB",
        "type": "Mobil",
        "rute": ["Pintu Besar Selatan", "Panglima Polim", "Depok", "Senen Raya", "Kemang"]
    },
    {
        "name": "Stark",
        "plat": "B 444 XSX",
        "type": "Motor",
        "rute": ["Pondok Indah", "Depok", "Senen Raya", "Kemang"]
    },
    {
        "name": "Anna",
        "plat": "B 678 DD",
        "type": "Mobil",
        "rute": ["Fatmawati", "Panglima Polim", "Depok", "Senen Raya", "Kemang", "Gajah Mada"]
    }
]

print(kenaRazia(27, data_kendaraan))
# Output: [{'name': 'Toni', 'tilang': 27}, {'name': 'Anna', 'tilang': 27}]