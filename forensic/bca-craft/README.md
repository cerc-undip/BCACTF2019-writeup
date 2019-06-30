# bca-craft
**Category:** forensic <br>
**Point:** 125

> Yo I made a sic Minecraft adventure MAP! Try it out it's kewler than ur Fortnite gamez!
> 
> (This map runs in Minecraft 1.13.2 and above)
> 
> made by: @anli5005

file : [BCACraft.zip](https://www.bcactf.com/files/2749663bd54cf3bb71295879858b4fb0/BCACraft.zip?token=eyJ0ZWFtX2lkIjoxMTE4LCJ1c2VyX2lkIjoxODY2LCJmaWxlX2lkIjoyfQ.XRixVQ.jva4BSzRUedtlGtV17OjeRDR024)

---

Pada challenge ini kita diberikan sebuah file dengan format `BCACraft.zip: Zip archive data, at least v1.0 to extract` yang artinya dapat kita _exract_ menggunakan `unzip`.

```bash
unzip BCACraft.zip
```

Dikarenakan foldernya "terlalu dalam" maka dari itu kita coba lakukan list menggunakan `tree` agar mempercepat dalam melihat file yang ada di dalamnya. Dari hasil tersebut, kita mendapatkan sebuah file yang mencurigakan yaitu `flag.mcfunction`.

```
.
├── datapacks
│   └── bcacraft
│       ├── data
│       │   └── bca
│       │       └── functions
│       │           └── flag.mcfunction
│       └── pack.mcmeta
├── icon.png
├── level.dat
├── README.md
└── region
    └── r.0.0.mca
```

Setelah kita buka, disitu terdapat flag yang kita cari. Kita hanya tinggal mengekstrak secara manual kedalam format flag yang diinginkan.

> Cara lain yang lebih mudah bisa dilihat pada script exploit [script.sh](./script.sh)

flag : `bcactf{m1n3cr4f7_b347s_f0rtn1t3}`