from prettytable import PrettyTable
admin = {'name' : 'Fadhiilah', 'password' : 'fadhiil123', 'role' : 1}
user = {'name' : 'Andika', 'password' : 'andika1223', 'role' : 0}

produk = [
    {"CODE" : 1, "Harga": 5000, "Kuota": "3GB/24 jam", "Stock": 15},
    {"CODE" : 2, "Harga": 20000, "Kuota": "5GB/30 hari", "Stock": 20},
    {"CODE" : 3, "Harga": 25000, "Kuota": "7.5GB/30 hari", "Stock": 40},
    {"CODE" : 4, "Harga": 50000, "Kuota": "12GB/30 hari", "Stock": 50}
]

# read
def show():
    tabel = PrettyTable(["CODE", "Harga", "Kuota", "Stock"])
    for brg in produk:
        tabel.add_row([brg["CODE"], brg["Harga"], brg["Kuota"], brg["Stock"]])
    tabel.padding_width = 5
    print(tabel)

# create
def create():
    code = int(input("Masukkan code produk baru : "))
    harga = int(input("Masukkan harga : "))
    kuota = input("Masukkan kuota : ")
    stock = int(input("Masukkan jumlah stock : "))
    produk.append({"CODE": code, "Harga": harga, "Kuota": kuota, "Stock": stock})
    print("Produk berhasil ditambahkan")

def update():
    code = int(input("Masukkan CODE produk : "))
    for brg in produk:
        if brg["CODE"] == code:
            brg["Harga"] = int(input("Masukkan Harga Produk : "))
            brg["Kuota"] = input("Masukkan kuota : ")
            brg["Stock"] = int(input("Masukkan jumlah stock : "))
            print("Produk berhasil diupdate!")
            return
    else:
        print("CODE Tidak Ditemukan")

def delete():
    code = int(input("Masukkan CODE produk : "))
    for brg in produk:
        if brg["CODE"] == code:
            produk.remove(brg)
            print("Produk Berhasil Dihapus!")
            return
    else:
        print("CODE Tidak Ditemukan")    

def transaksi():
    keranjang = []
    total_harga = 0

    while True:
        print("======================================================\n")
        show()
        kode = int(input("Masukkan CODE produk yang ingin dibeli (ketik 0 untuk selesai) : "))

        if kode == 0:
            break

        # mencari produk berdasarkan kode
        terpilih = None
        for p in produk:
            if p["CODE"] == kode:
                terpilih = p
                break

        if terpilih:
            jumlah = int(input("Masukkan jumlah yang ingin dibeli : "))
            if jumlah <= terpilih["Stock"]:
                terpilih["Stock"] -= jumlah
                keranjang.append({"Kuota" : terpilih["Kuota"], "Harga" : terpilih["Harga"], "Jumlah" : jumlah})
                total_harga += terpilih["Harga"] * jumlah
                print("Produk berhasil ditambahkan ke keranjang")
            else:
                print("Produk Tidak Mencukupi")
        else:
            print("Kode Tidak Valid. Coba Lagi")
    print("\n======================================================")
    print("Rincian Transaksi")
    tabel_trans = PrettyTable(["Kuota", "Harga", "Jumlah Total", "Total Harga"])
    for item in keranjang:
        nama = item["Kuota"]
        harga = item["Harga"]
        jumlah = item["Jumlah"]
        total_item = harga * jumlah
        tabel_trans.add_row([nama, harga, jumlah, total_item])
    print(tabel_trans)
    print("Total Harga : Rp", total_harga)
    print("======================================================")

def login():
    while True:
        username = input("Masukkan nama : ")
        password = input("Masukkan password : ")

        if username == admin['name'] and password == admin['password']:
            user_role = admin['role']
            break
        elif username == user['name'] and password == user['password']:
            user_role = user['role']
            break
        else:
            print("Nama atau password salah")
    return user_role

print("======================================================")
role_user = login()
print("======================================================\n")
show()
# menu admin
if role_user == 1:
    while True:
        print("1. Menambahkan produk")
        print("2. Mengupdate produk")
        print("3. Menghapus produk")
        print("4. Keluar")
        pilih = int(input("Pilih (1-4) : "))
        if pilih == 1:
            create()
        elif pilih == 2:
            update()
        elif pilih == 3:
            delete()
        elif pilih == 4:
            break
        else:
            print("Pilihan Tidak Valid")
        print("\n======================================================\n")

        show()
# menu user
elif role_user == 0:
    print("SELAMAT DATANG", user['name'])
    while True:
        print("1. Mulai Transaksi")
        print("2. Keluar")
        pilih = int(input("Pilih (1/2) : "))

        if pilih == 1:
            transaksi()
            break
        elif pilih == 2:
            print("Terima Kasih!")
            break
        else:
            print("Pilihan Tidak Valid")
        

