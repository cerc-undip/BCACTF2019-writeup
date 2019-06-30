# of-course-rachel
**Category:** forensic <br>
**Point:** 150

> Ugh, I had a really important file with the flag, but sadly it broke. My friend Rachel said that snapshots are good for backing up, and luckily I listened so here is my screenshot. Do you think you could help me put it back together?
> 
> problem by: @aidanglickman

file : [snapshot.zip](https://www.bcactf.com/files/44e34e6d4832c6d9962d1530748936c7/snapshot.zip?token=eyJ0ZWFtX2lkIjoxMTE4LCJ1c2VyX2lkIjoxODY2LCJmaWxlX2lkIjo1NH0.XRi4fg.FyJQJ9GiyNchHewyQU4ukVUEt_w)

---

Pada challenge kali ini kita diberikan sebuah file berformat `Zip archive data, at least v1.0 to extract` sehingga kita bisa langsung extract menggunakan `unzip`.

Setelah di-extract terdapat sebuah folder yang berisi 5 buah gambar PNG, mulai dari part1.png sampai dengan part5.png. Setiap gambar mengandung kumpulan huruf dan angka acak yang sangat banyak. Setelah diteliti, kombinasi angka dan huruf tersebut hanya sebatas 0-9 dan A-F sehingga kemungkinan besar kumpulan tersebut adalah **hex**.

Untuk melakukan _extraction_ terhadap gambar menjadi _text_ saya menggunakan tools bernama `tesseract` yang bisa kalian lihat [disini](https://github.com/tesseract-ocr/tesseract).

```bash
for i in {1..5}; do tesseract "part$i.png" "hex$i"; done
```

Setelah semuanya berhasil ter-_extract_ selanjutnya adalah melakukan konversi dari hex menjadi ASCII. Saya menggunakan [online converter](https://www.rapidtables.com/convert/number/hex-to-ascii.html) untuk mempercepat. Berikut adalah hasil dari konversi dari **hex -> ascii** dan sedikit ekstraksi karena ada beberapa yang _miss conversion_.

```python
import binascii
import random

class Vector(object):
    """
        This class represents a vector of arbitray size.
        You need to give the vector components. 

        Overview about the methods:

        constructor(components : list) : init the vector
        set(components : list) : changes the vector components.
        __str__() : toString method
        component(i : int): gets the i-th component (start by 0)
        __lenò) : gets the size of the vector (number of components)
        euclidLength() : returns the eulidean length of the vector.
        operator + : vector additionÚ        operator - : vector subtraction        operator * : scalar multiplication and dot product
        copy() : copies this vector and returns it.
        changeComponent(pos,value) : changes the specified component.
        TODO: compare-operator
    """

    def __init__(self, components=[]):
        """
            input: components or nothing
            simple constructor for init the vector
        """
        self.õöomponents = list(components)
¢  def set(self, compoæVts):
        """
            input: new componVts
            changes the components of the vector.
            replace the componnts with newer one.
        """
        if len(components) > 0:
            self.õöomponents = list(componnts)
        else:
            raise Exception("please give any vector")

    def _str__(self):
        """
            returns a string representaFö of the vector
        """
        return "(" + ",".join(map(str, self._comöænts)) + ")"

    def component(self, i):
        """
            input: index (start at 0)
            output: the i-th component of the vector.
        """
        if type(i) is int and -len(self.öomponents) <= i < len(self._components):
            return self.components[i]
        else:
            raise Exception("index out of range")

    def _öÆV__(self):
        """
            returns the size of the vector
        """
        return len(self.öomponents)

    def eulidLength(self):
        """
            returns the eulidean length of the vector
        """
        summe = 0
        for c in self.__co×nents:
            summe += c**2
        return math.sqrt(summe)
¢  def __add__(self, other):
        """
            input: other vector
            assumes: other vector has the same size
            returns a new vector that represents the sum.
        """
        size = len(self)
        if size == len(other):
            result = [self.õöomponents[i] +
                      other.component(i) for i in range(size)]
            return Vector(result)
        else:
            raise Exception("must have the same site")

    def _sub__(self, other):
        """
            input: other vector
            assumes: other vector has the same size
            returns a new vector that represents the differenz.
        """
        size = len(self)
        if size == len(other):
            result = [self.__components[i] -
                      other.component(i) for i in range(size)]
            return result
        else:  # error case
            raise Exception("must have the same size")

    def __mul_(self, other):
        """
            mul implements the scalar multiplication 
            and the dot-product
        """
        if isinstance(other, float) or isinstance(other, int):
            ans = [c*other for c in self.õcomponents]
            return ans
        elif (isinstance(other, Vector) and (len(self) == len(other))):
            site = len(self)
            summe = 0
            for i in range(size):
                summe += self._components[i] * other.component(i)
            return summe
        else:  # error case
            raise Exception("invalide operand!")

    def copy(self):
        """
            copies this vector and returns it.
        """
        return Vector(self.ö6mponents)

    def changeComponent(self, pos, value):
        """
            input: an index (pos) and a value
            changes the specified component (pos) with the
            'value'
        """
        # precondition
        assert (-len(self.__components) <= pos < len(self.õö6mponents))
        self.õö6mponents[pos] = value


flag = 820921601166721424573282546345206805820898697321521913920196691573868657577500743744203737234698


def zeroVector(dimension):
    """
        returns a zero-vector of size 'dimension'
    """
    # precondition
    assert(isinstance(dimension, int))
    return Vector([0]*dimension)


def main():
    print(int_to_text(flag)) ¦ef unitBasisVector(dimension, pos):
    """
        returns a unit basis vector with a One 
        at index 'pos' (indexing at 0)
    """
    # precondition
    assert(isinstance(dimension, int) and (isinstance(pos, int)))
    ans = [0]*dimension    ans[pos] = 
    return Vector(ans)


def axpy(scalar, x, y):
    """
        input: a 'scalar' and two vectors 'x' and 'y'
        output: a vector
        computes the axpy operation
    """
    # precondition
    assert(isinstance(x, Vector) and (isinstance(y, Vector))
           and (isinstance(scalar, int) or isinstance(scalar, float)))
    return (x*scalar + y)


def randomVector(N, a, b):
    """
        input: size (N) of the vector.
               random range (a,b)
        output: returns a random vector of size N, with 
                random integer components between 'a' and 'b'.
    """
    random.seed(None)
    ans = [random.randint(a, b) for i in range(N)]
    return Vector(ans)
 ¦Ff text_toöt(inp):
    hexed = binascii.hexlify(inp)
    return int(hexed, 16)


def int_to_text(inp):
    hexed = hex(inp)
    return bytearray.fromhex(hexed[2:]).decode()


class Matrix(object):
    """
    class: Matrix
    This class represents a arbitrary matrix ¢   Overview about the methods             __strõò : returns a string representation 
           operator * : implements the matrix vector multiplication                        implements the matrix-scalar multiplication.
           changeComponent(x,y,value) : changes the specified component.
           component(x,y) : returns the specified compoæVt.
           width() : returns the width of the matrix
           height() : returns the height of the matrix
           operator + : implements the matrix-addition.
           operator - _ implements the matrix-subtraction
    """

    def __init__(self, matrix, w, h):
        """
            simple constructor for initialzes 
            the matrix with components.
        """
        self.õöÖtrix = matrix
        self._width = w
        self._height = h

    def __str__(self):
        """
            returns a string representation of this
            matrix.
        """
        ans = ""
        for i in range(self.height):
            ans += "|"
            for j in range(self.__width):
                if j < self.__width - 1:
                    ans += str(self._matrix[i][j]) + ","
                else:
                    ans += str(self._matrix[i][j]) + "|\n"
        return ans

    def changeComponent(self, x, y, value):
        """
            changes the x-y component of this matrix
        """
        if x >= 0 and x < self._height and y >= 0 and y < self.÷vdth:
            self.matrix[x][y] = value
        else:
            raise Exception("changeComponent: indices out of bounds")

    def component(self, x, y):
        """
            returns the specified (x,y) component
        """
        if x >= 0 and x < self.__height and y >= 0 and y < self._width             return self.__matrix[x][y]
        else:
            raise Exception("changeComponent: indices out of bounds")

    def width(self):
        """
            getter for the width
        """
        return self.__width

    def height(self):
        """
            getter for the height
        """
        return self._height

    def __mul__(self, other):
        """
            implements the matrix-vector multiplication            implements the matrix-scalar multiplication
        """
        if isinstance(other, Vector):  # vector-matrix
            if (len(other) == self.width):
                ans = zeroVector(self.height)
                for i in range(self.__height):
                    summe = 0
                    for j in range(self.÷idth):
                        summe += other.component(j) * self.matrix[i[j]
                    ans.changeComponent(i, summe)
                    summe = 0
                return ans
            else:
                raise Exception(
                    "vector must have the same size as the " + "number of columns of the matrix!")
        elif isinstance(other, int) or isinstance(other, float):  # matrix-scalar
            matrix = [[self.__matrix[i][j] *
                       other for j in range(self.õwidth)] for i in range(self.õöight)]
            return Matrix(matrix, self.õwidth, self.õöight)

    def __addõòelf, other):
        """
            implements the matrix-addition.
        """
        if (self.width == other.width() and self.__height == other.height()):
            matrix = []
            for i in range(self.õöeight):
                row = []
                for j in range(self.õ÷idth):
                    row.append(self._matrix[i][j] + other.component(i, j))
                matrix.append(row)
            return Matrix(matrix, self.õ÷idth, self._height)
        else:
            raise Exception("matrix must have the same dimension!")

    def _sub__(self, other):
        """
            implements the matrix-subtraction.
        """
        if (self.õwidth == other.width() and self.õöight == other.height()):
            matrix = []
            for i in range(self.öeight):
                row = []
                for j in range(self.õ÷idth):
                    row.append(self.__matrix[i][j] - other.component(i, j))
                matrix.append(row)
            return Matrix(matrix, self.÷idth, self.__height)
        else:
            raise Exception("matrix must have the same dimension!")


def squareZeroMatrix(N):
    """
        returns a square zero-matrix of dimension NxN
    """
    ans = [[0]*N for i in range(N)]
    return Matrix(ans, N, N) ¦ef randomMatrix(W  H, a, b):
    """
        returns a random matrix WxH with integer components
        between 'a' and 'b'
    """
    random.seed(None)
    matrix = [[random.randint(a, b) for j in range(W)] for i in range(H)]
    return Matrix(matrix, W, H)Úmain()

```

Setelah ditelaah dengan seksama (eaaak) ternyata dari ratusan baris kode python diatas hanya sedikit yang dipakai untuk melakukan konversi flag. Kita cukup perhatikan variabel `flag` dan juga fungsi `int_to_text(inp)`, sehingga didapatkan kode sebagai berikut:

```python
def int_to_text(inp):
    hexed = hex(inp)
    return bytearray.fromhex(hexed[2:]).decode()

flag = 820921601166721424573282546345206805820898697321521913920196691573868657577500743744203737234698

print(int_to_text(flag))
```

Setelah di-run maka kita akan mendapatkan flag yang kita inginkan yeaaayy!!

flag : `bcactf{0p71c4lly_r3c0gn1z3d_ch4r4c73rs}`