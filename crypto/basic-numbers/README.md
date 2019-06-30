# 1+1=window
**Category:** programming <br>
**Point:** 75

> We have a raw flag here, but what do we do with it?
> 
> 01100010 00110001 01101110 01100001 01110010 01111001 01011111 01110011 00110000 01101100 01110110 00110011 01100100 01011111 01100111 00110000 00110000 01100100 01011111 01110111 00110000 01110010 01101011
>
> made by: @camelliaguan
> 
> The answer should be in the format bcactf{answer}.

---

Untuk menyelesaikan challenge ini kita hanya perlu mengkonversikan bilangan biner pada soal menjadi ASCII. Bisa diselesaikan menggunakan [tools online](https://www.binaryhexconverter.com/binary-to-ascii-text-converter) ataupun pemrograman. Challenge ini saya selesaikan dengan menggunakan bahasa Python.

```python
raw = open("quest.txt", "r").read()

binary = raw.split(" ")
binary = [chr(int(x, 2)) for x in binary]

print(''.join(map(str, binary)))
```

Hasilnya adalah
```
b1nary_s0lv3d_g00d_w0rk
```

Terakhir cukup tambahkan sesuai dengan format flag

solution : [script.py](./script.py)

flag : `bcactf{b1nary_s0lv3d_g00d_w0rk}`