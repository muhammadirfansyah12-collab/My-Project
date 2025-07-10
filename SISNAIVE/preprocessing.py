def kategorikan_nilai(nilai):
    if nilai >= 85:
        return 2  # Tinggi
    elif nilai >= 70:
        return 1  # Sedang
    else:
        return 0  # Rendah

def kategorikan_kehadiran(persen):
    if persen >= 90:
        return 2
    elif persen >= 75:
        return 1
    else:
        return 0
