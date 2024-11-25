from locale import currency
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
from requests.packages import target

target_code = None
target_code2 = None
base_code = None


def tc_tc2():
    global (target_code, target_code2, base_code)
    try:
        response = requests.get(
            f'https://api.coingecko.com/api/v3/simple/price?ids={base_code}&vs_currencies=usd,eur,rub')
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

def exchange():
    t = target_combobox.get()
    target_code = next(key for key, value in currencis.items() if value == t)
    v = base_combobox.get()
    base_code = next(key for key, value in coins.items() if value == v)
    t2 = target_combobox2.get()
    target_code2 = next(key for key, value in currencis.items() if value == t2)

    if target_code and target_code2 and base_code:
        tc_tc2()

    else:
        mb.showwarning("Внимание", "Выберите код валюты")

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

window = Tk()
window.title("Курсы обмена криптовалюты")
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w2 = w//2 - 230
h2 = h//2 - 175
window.geometry(f"460x350+{w2}+{h2}")

Label(text="Выберите криптовалюту:").pack(padx=5, pady=5)

base_combobox = ttk.Combobox(values=list(coins.values()))
base_combobox.pack(padx=5, pady=5)
Label(text="Выберите код целевой валюты:").pack(padx=5, pady=5)

target_combobox = ttk.Combobox(values=list(currencis.values()))
target_combobox.pack(padx=5, pady=5)

Label(text="Выберите код второй целевой валюты:").pack(padx=5, pady=5)

target_combobox2 = ttk.Combobox(values=list(currencis.values()))
target_combobox2.pack(padx=5, pady=5)

Button(text="Получить курс обмена", command=exchange).pack(padx=5, pady=5)

label = Label(text="", font="Courier 10")
label.pack(padx=5, pady=5)

window.mainloop()