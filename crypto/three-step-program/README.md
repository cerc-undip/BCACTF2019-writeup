# three-step-program
**Category:** crypto <br>
**Point:** 125

> We found this strange file with a bunch of stuff in it... Can you help us decode it?

file : [RmlsZW5hbWU.txt](https://www.bcactf.com/files/02d2510ea1f357dc632b786e6597b332/RmlsZW5hbWU.txt?token=eyJ0ZWFtX2lkIjoxMTE4LCJ1c2VyX2lkIjoxODY2LCJmaWxlX2lkIjo0NX0.XRjSPA.HFQWJ0g29nMwG5GQHmdtIPPjPiE)

---

Pada challenge kali ini kita diberikan sebuah file instruksi/urutan untuk mendapatkan flag. Pada baris pertama, dari karakteristiknya merupakan pesan yang di-encode menggunakan **Base64** karena terdapat karakter "*=*" di akhir. Kita lakukan decode menggunakan command `base64`.

```bash
echo MzIgLSAgfDMgVGltZXMgQSBDaGFybXwgLSAzMg== | base64 -d
```

Pesan yang didapat adalah : `32 -  |3 Times A Charm| - 32`

Sempat berfikiri beberapa saat tentang maksud ini untuk menyelesaikan perintah berikutnya. Ternyata, maksud dari pesan ini adalah kita harus melakukan decoding pesan kedua sebanyak 3 kali menggunakan algoritma encoding [Base32](https://en.wikipedia.org/wiki/Base32). Hal ini dapat diselesaikan dengan perintah linux `base32`.

```
echo JJGTEVSLKNBVISSGINCU2VCTGJFVETCWKNGVGTKLKJEEKQ2VJNEUSNC2KZKVCS2OJFNE4RKPKNFUUSKSJNKTITSDKJFEERKUI5GTETKJLJGVMQ2RJNLEWUSLIZAVES2DJRFE2RKDK5JU2SKKJBCTEVKLJBDUSWSUI5KTETSLKZEVKS2TLJKEWUSFIU2FKU2WJRBEIVCFKFJVASKWIFKU2USLIRDUUR2FGJJEWQ2LKJGFMR2TJNCUYSSIIRFU2U2UJFCTEVKJKZJUMSKKJNKU6VK2KRFVES2VGZKEWUSKIJCVIR2XKNBEUNKGIZDVMMSEJRFEERKDKRJVOR2SJJKUGV2TJVFDKR2VGRLVGSKLJUZEKSKWJNHEWWSKKVDVCSSUJFJEERJUK5JVKTCCIZKEKVCDIVFFUQKWKFITEQSJJZEVKV2SGJDEYQSCKVBVMSSTJFFEMRSFKMZEISKFLJCVSTKTIZEUUTCGJ5JVUV2KJJAVKNSVKNMUWTSBKZKU2MSUJJLEYRCFKEZEETCKJNDECVCSKZFU4QSVI5ITEU2LJZCEMU2VJNDEYRSOIVKVCS2OJRFE4RKPKFNFIS2SINCTEUSTKZGEERCVKNJEGRKKGVDEISKXINBEOVSDIVGVES2DJM2UIVKXKNFUKSS2I5LE2VSLLBGEKWSVJFJFGUCLLJHEKQ2QJI2UQVJWKE6T2PJ5 | base32 -d | base32 -d | base32 -d
```

Hasil yang didapat adalah
```
Why english so ard to tok. 
No speak more English. 
Ail gi you tu hints to read my encrypted languich. 

1. SALT iz key to gret food!
2. Le francais crypte le meilleur
```

Dari clue kedua kita tahu bahwa mereka berusaha menyebutkan algoritma enkripsi [Vigenere](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) karena berasal dari Perancis. Untuk melakukan dekripsi pesan terakhir kita bisa gunakan tools online [Vigenere Solver](https://www.guballa.de/vigenere-solver) dan kita akan mendapatkan flag yang dicari.

flag : `bcactf{ju57_y0u_w4i7_znjhbmnhaxm}`
