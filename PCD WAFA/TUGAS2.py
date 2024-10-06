import numpy as np
import imageio.v3 as imageio
import cv2
import os

paths = [
    r"C:\\Users\\ACER\\Downloads\\Burung-Merpati.jfif",
    r"C:\\Users\\ACER\\Downloads\\Burung-Kakak-Tua.jfif",
    r"C:\\Users\\ACER\\Downloads\\Burung-Hantu.jfif",
]

# Memproses setiap gambar
def process_image(path):
    # Membaca gambar
    image_source = imageio.imread(path)

    if image_source is None:
        print(f"Error: Gambar {path} tidak ditemukan atau gagal dibaca!")
        return

    if len(image_source.shape) != 3 or image_source.shape[2] != 3:
        print(f"Gambar {path} tidak dalam format RGB.")
        return

    red_ch = image_source[:, :, 0]
    green_ch = image_source[:, :, 1]
    blue_ch = image_source[:, :, 2]

    image_red = np.zeros_like(image_source)
    image_green = np.zeros_like(image_source)
    image_blue = np.zeros_like(image_source)

    image_red[:, :, 0] = red_ch 
    image_green[:, :, 1] = green_ch 
    image_blue[:, :, 2] = blue_ch

    # Konversi ke grayscale
    image_grayscale = cv2.cvtColor(image_source, cv2.COLOR_RGB2GRAY)

    # Konversi ke threshold (binner)
    _, image_threshold = cv2.threshold(image_grayscale, 127, 255, cv2.THRESH_BINARY)

    # Membuat nama file tanpa ekstensi untuk penyimpanan
    file_name = os.path.basename(path).split('.')[0]

    # Simpan gambar hasil representasi setiap channel dan konversi
    imageio.imwrite(f"{file_name}_red.jfif", image_red)
    imageio.imwrite(f"{file_name}_green.jfif", image_green)
    imageio.imwrite(f"{file_name}_blue.jfif", image_blue)
    imageio.imwrite(f"{file_name}_grayscale.jfif", image_grayscale)
    imageio.imwrite(f"{file_name}_threshold.jfif", image_threshold)

    print(f"Gambar {file_name} telah diproses.")

# Proses semua gambar satu per satu
for path in paths:
    process_image(path)

print("Selesai!")