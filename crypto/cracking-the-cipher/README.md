# cracking-the-cipher
**Category:** crypto <br>
**Point:** 50

> Hackers work in the most unlikely of places. We have recently discovered one working in a grocery store (weird), and he was able to print out receipts to pass on information to certain customers. We have obtained one of the receipts, but we cannot tell what it says.
> 
> Grocery Store Receipt<br>
> Item	Unit Price	Quant.	Overall Price<br>
> Caesar Salad Dressing	5.99	4	23.96<br>
> Vinegar	6.99	1	6.99<br>
> Apples (Honey Crisp)	2.79	5	13.95<br>
> Roast Chicken	7.59	1	7.59<br>
> Tomatoes	1.59	4	6.36<br>
> Subtotal	58.85<br>
> Paper Bag Fee	0.10<br>
> Taxes (9.00%)	0.00<br>
> Total	58.95<br>
> vjg rcuuyqtf ku ngctpkpi_ecguct_ekrjgtu_ku_hwp!
> 
> Can you crack the code and tell us the information within? The answer should be in the format `bcactf{answer}`.<br>
> made by: @camelliaguan

---

Deskripsi soal challenge ini memang cukup banyak, tapi cukup perhatikan bagian yang kelihatannya sulit dibaca

```
vjg rcuuyqtf ku ngctpkpi_ecguct_ekrjgtu_ku_hwp!
```

Dari bentuk dan rangkaiannya, tebakan pertama saya adalah pesan tersebut di-enkripsi menggunakan enkripsi [Caesar](https://en.wikipedia.org/wiki/Caesar_cipher).

Langsung saja kita lakukan dekripsi menggunakan [tools online](https://cryptii.com/pipes/caesar-cipher) dengan jumlah shift-nya adalah 24.

```
the password is learning_caesar_ciphers_is_fun!
```

flag : `bcactf{learning_caesar_ciphers_is_fun!}`