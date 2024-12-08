class ShoppingItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        price_formatted = f"{int(self.price):,}".replace(",", ".")
        total_formatted = f"{int(self.total_price()):,}".replace(",", ".")
        return f"{self.name} (x{self.quantity}) - Rp {price_formatted} (Total: Rp {total_formatted})"

    def total_price(self):
        return self.quantity * self.price


class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                print(f"Barang '{item_name}' telah dihapus dari daftar.")
                return
        print(f"Barang '{item_name}' tidak ditemukan di daftar.")

    def edit_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                print(f"Item ditemukan: {item}")
                try:
                    quantity = int(input(f"Masukkan jumlah baru untuk {item_name}: "))
                    price = float(input(f"Masukkan harga baru per unit {item_name}: Rp "))
                    item.quantity = quantity
                    item.price = price
                    print(f"Barang '{item_name}' telah diperbarui.")
                except ValueError:
                    print("Input tidak valid. Jumlah harus angka dan harga harus desimal.")
                return
        print(f"Barang '{item_name}' tidak ditemukan di daftar.")

    def display_items(self):
        if not self.items:
            print("Daftar belanja kosong.")
        else:
            print("Daftar Belanja Anda:")
            for item in self.items:
                print(item)

    def total_cost(self):
        total = sum(item.total_price() for item in self.items)
        return f"{int(total):,}".replace(",", ".")


def add_shopping_item(shopping_list):
    try:
        name = input("Masukkan nama barang: ")
        quantity = int(input(f"Masukkan jumlah {name}: "))
        price = float(input(f"Masukkan harga per unit {name}: Rp "))
        item = ShoppingItem(name, quantity, price)
        shopping_list.add_item(item)
        print(f"Barang '{name}' telah ditambahkan ke daftar.")
    except ValueError:
        print("Input tidak valid. Jumlah harus angka dan harga harus desimal.")


def remove_shopping_item(shopping_list):
    item_name = input("Masukkan nama barang yang ingin dihapus: ")
    shopping_list.remove_item(item_name)


def main():
    shopping_list = ShoppingList()

    while True:
        print("\nMenu Pengelola Daftar Belanja")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Lihat Daftar Belanja")
        print("4. Total Belanja")
        print("5. Edit Barang")
        print("6. Keluar")

        choice = input("Pilih opsi (1-6): ")

        if choice == '1':
            add_shopping_item(shopping_list)
        elif choice == '2':
            remove_shopping_item(shopping_list)
        elif choice == '3':
            shopping_list.display_items()
        elif choice == '4':
            print(f"Total biaya belanja: Rp {shopping_list.total_cost()}")
        elif choice == '5':
            item_name = input("Masukkan nama barang yang ingin diubah: ")
            shopping_list.edit_item(item_name)
        elif choice == '6':
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            print("Opsi tidak valid, coba lagi.")


if __name__ == "__main__":
    main()

                            
