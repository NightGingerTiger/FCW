from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
from PIL import Image, ImageTk


def load_image(event):
    v = base_combobox.get()
    base_img = next(key for key, value in coins.items() if value == v)
    try:
        file_path = f'C://Users/icons/{base_img}.jpg'
        if file_path:
            image = Image.open(file_path)
            image = image.resize((70, 70))
            image_tk = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, anchor=NW, image=image_tk)
            canvas.image = image_tk
    except Exception as e:
        print(f'{e}')


def clear_label(event):
    label.config(text="")


def clear_label_base(event):
    label.config(text="")
    if base_combobox:
        load_image(event)


def exchange():
    try:
        t = target_combobox.get()
        target_code = next(key for key, value in currencis.items() if value == t)
        v = base_combobox.get()
        base_code = next(key for key, value in coins.items() if value == v)
        t2 = target_combobox2.get()
        target_code2 = next(key for key, value in currencis.items() if value == t2)

        if target_code and target_code2 and base_code:
            try:
                response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={base_code}&vs_currencies=usd,eur,rub')
                response.raise_for_status()

                data = response.json()

                if target_code in data[f'{base_code}']:
                    if target_code2 in data[f'{base_code}']:
                        exchange_rate = data[f'{base_code}'][target_code]
                        exchange_rate2 = data[f'{base_code}'][target_code2]
                        target_name = currencis[target_code]
                        target_name2 = currencis[target_code2]
                        base_name = coins[base_code]
                        label.config(text=f"Курс {exchange_rate:.2f} {target_name} за 1 {base_name}\n"
                                          f"Курс {exchange_rate2:.2f} {target_name2} за 1 {base_name}")
                    else:
                        mb.showerror("Ошибка", f"Валюта {target_code2} не найдена")
                else:
                    mb.showerror("Ошибка", f"Валюта {target_code} не найдена")

            except Exception as e:
                mb.showerror("Ошибка", f"Ошибка: {e}")
        else:
            mb.showwarning("Внимание", "Выберите валюту")
    except Exception:
        mb.showerror("Ошибка", "Выберите валюту")

coins = {
    "bitcoin": "Bitcoin",
    "ethereum": "Ethereum",
    "dogecoin": "Dogecoin",
    "ripple": "XRP",
    "solana": "Solana",
    "cardano": "Cardano",
    "stellar": "Stellar",
    "polkadot": "Polkadot",
    "celestia": "Celestia",
    "litecoin": "Litecoin",
    "internet-computer": "Internet Computer",
    "binance-peg-weth": "Binance-Peg WETH",
    "wrapped-bitcoin": "Wrapped Bitcoin",
    "binancecoin": "BNB",
    "avalanche-2": "Avalanche",
    "staked-ether": "Lido Staked Ether",
    "rocket-pool-eth": "Rocket Pool ETH",
    "wrapped-steth": "Wrapped stETH",
    "weth": "WETH",
    "tron": "TRON"
}

currencis = {
    "usd": "Американский доллар",
    "rub": "Российский рубль",
    "eur": "Евро"
}

jpegs = {
    "bitcoin": "bitcoin.jpg",
    "ethereum": "ethereum.jpg",
    "dogecoin": "dogecoin.jpg",
    "ripple": "ripple.jpg",
    "solana": "solana.jpg",
    "cardano": "cardano.jpg",
    "stellar": "stellar.jpg",
    "polkadot": "polkadot.jpg",
    "celestia": "celestia.jpg",
    "litecoin": "litecoin.jpg",
    "internet-computer": "internet-computer.jpg",
    "binance-peg-weth": "binance-peg-weth.jgp",
    "wrapped-bitcoin": "wrapped-bitcoin.jpg",
    "binancecoin": "binancecoin.jpg",
    "avalanche-2": "avalanche-2.jpg",
    "staked-ether": "staked-ether.jpg",
    "rocket-pool-eth": "rocket-pool-eth.jpg",
    "wrapped-steth": "wrapped-steth.jpg",
    "weth": "weth.jgp",
    "tron": "tron.jpg"
}

window = Tk()
window.title("Курсы обмена криптовалюты")
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w2 = w//2 - 230
h2 = h//2 - 175
window.geometry(f"460x350+{w2}+{h2}")

canvas = Canvas(window, width=70, height=70)
canvas.pack()

Label(text="Выберите криптовалюту:").pack(padx=5, pady=5)

base_combobox = ttk.Combobox(values=list(coins.values()))
base_combobox.pack(padx=5, pady=5)
base_combobox.bind("<<ComboboxSelected>>", clear_label_base)

Label(text="Выберите код целевой валюты:").pack(padx=5, pady=5)

target_combobox = ttk.Combobox(values=list(currencis.values()))
target_combobox.pack(padx=5, pady=5)
target_combobox.bind("<<ComboboxSelected>>", clear_label)

Label(text="Выберите код второй целевой валюты:").pack(padx=5, pady=5)

target_combobox2 = ttk.Combobox(values=list(currencis.values()))
target_combobox2.pack(padx=5, pady=5)
target_combobox2.bind("<<ComboboxSelected>>", clear_label)

Button(text="Получить курс обмена", command=exchange).pack(padx=5, pady=5)

label = Label(text="", font="Courier 10")
label.pack(padx=5, pady=5)

window.mainloop()