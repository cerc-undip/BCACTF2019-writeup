# open-docs
**Category:** forensic <br>
**Point:** 150

> Yay! I really enjoy using these free and open file standards. I love them so much, that I made a file expressing how much I like using them. Let's enjoy open standards together!
> 
> made by: @edwfeng

file : [open.docx](https://www.bcactf.com/files/547366015d9c2ca402542999f1e5097e/open.docx?token=eyJ0ZWFtX2lkIjoxMTE4LCJ1c2VyX2lkIjoxODY2LCJmaWxlX2lkIjo1fQ.XRi91w.-vbSZlBNzlp2laHkNRknKJqshCU)

---

Pada challenge kali ini kita diberikan sebuah file yang walaupun file ini berekstensi `.docx` namun file ini merupakan `Zip archive data, at least v2.0 to extract` yang artinya kita bisa langsung extract menggunakan `unzip`.

```bash
unzip open.docx
```

Setelah di-extract terdapat beberapa file dan folder yang tidak memberikan clue apapun. Selanjutnya kita coba list folder dengan menggunakan `tree` agar mempermudah melihatnya.

```
.
├── [Content_Types].xml
├── docProps
│   ├── app.xml
│   └── core.xml
├── open.docx
├── _rels
└── word
    ├── document2.xml
    ├── fontTable.xml
    ├── _rels
    │   └── document2.xml.rels
    ├── secrets.xml
    ├── settings.xml
    ├── styles.xml
    ├── theme
    │   └── theme1.xml
    └── webSettings.xml

5 directories, 12 files
```

Dari sini kita mengetahui terdapat sebuah file bernama `secrets.xml` yang berisi :

```
<?xml version="1.0" encoding="utf-8"?>
PHNlY3JldCBmbGFnPSJiY2FjdGZ7ME94TWxfMXNfNG00ejFOZ30iIC8+
```

Baris kedua terlihat seperti format text pada encoding menggunakan **base64**. Mari kita decode pesan tersebut menggunakan `base64`.

```
echo PHNlY3JldCBmbGFnPSJiY2FjdGZ7ME94TWxfMXNfNG00ejFOZ30iIC8+ | base64 -d
```

Taadddaaaaaa kita dapatkan flag-nya!!

exploit : [script.sh](./script.sh)

flag : `bcactf{0OxMl_1s_4m4z1Ng}`