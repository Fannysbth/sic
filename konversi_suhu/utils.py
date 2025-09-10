def konversi_suhu(nilai, dari, ke):
    dari = dari.lower()
    ke = ke.lower()
    
    satuan_valid = ["c", "f", "k"]
    if dari not in satuan_valid or ke not in satuan_valid:
        return "Error: Satuan tidak valid. Gunakan 'C', 'F', atau 'K'."
    
    if dari == "k" and nilai < 0:
        return "Error: Suhu dalam Kelvin tidak boleh negatif."
    
    if dari == ke:
        return nilai

    if dari == "c":
        c = nilai
    elif dari == "f":
        c = (nilai - 32) * 5/9
    elif dari == "k":
        c = nilai - 273.15

    if ke == "c":
        return round(c, 2)
    elif ke == "f":
        return round(c * 9/5 + 32, 2)
    elif ke == "k":
        return round(c + 273.15, 2)
