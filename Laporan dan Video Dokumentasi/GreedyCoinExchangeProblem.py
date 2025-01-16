coin_denominations = input("Masukkan pecahan/denominasi koin : ")
coins = list(map(int, coin_denominations.split()))
coins.sort(reverse=True)  # Urutkan dari besar ke kecil

def make_change(change_needed):
    result = []
    for coin in coins:
        while change_needed >= coin:
            result.append(coin)
            change_needed -= coin
            print(f"Pilih koin {coin}, sisa uang {change_needed}")
    return result

uang = int(input("Jumlah uang: "))

print(f"\nUang {uang} bisa ditukar menjadi: {make_change(uang)}")