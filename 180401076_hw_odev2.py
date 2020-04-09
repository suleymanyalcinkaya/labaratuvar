ithalat  sys
def  hist ( dosya ):
    histogram  = []
    içinde  = []
    için  i  de  dosya :
        check  =  Yanlış
        altında . append ( int ( i . bölünmüş ( ";" ) [ 3 ]. bölünmüş ( "-" ) [ 1 ]))
        için  k  olarak  aralık ( len ( Histogram )):
            Eğer  int ( i . bölünmüş ( ";" ) [ 3 ]. bölünmüş ( "-" ) [ 1 ]) ==  histogramı [ k ] [ 0 ]:
                histogram [ k ] [ 1 ] + =  1
                check  =  Doğru
        eğer  onay  ==  false :
            histogram . append ([ int ( i . bölünmüş ( ";" ) [ 3 ]. bölünmüş ( "-" ) [ 1 ]), 1 ])
    dönüş  histogramı , Veriler

def  ort ( dizi ):
    toplam = 0
    için  i  içinde  Dizi :
        toplam + = i
    dönüş  toplam / len ( dizi )

def  bubbleSort ( dizi ):
    için  I  içinde  aralığı ( len ( dizi ) - 1 , - 1 , - 1 ):
        için  j  olarak  aralık ( 0 , i )
            Eğer  değil  dizi [ j ] < dizi [ j + 1 ]:
                temp = dizi [ j ]
                dizi [ j ], dizi [ j + 1 ] = dizi [ j + 1 ], sıcaklık
    dönüş  dizisi

def  medyan ( dizi ):
    dizi = bubbleSort ( dizi )
    Eğer  Len ( dizi ) % 2 == 1 :
        orta  =  int ( len ( dizi ) / 2 ) + 1
        dönüş  dizisi [ orta - 1 ]
    başka :
        orta1 , orta2 = dizi [ int ( len ( dizi ) / 2 )], dizi [ int ( len ( dizi ) / 2 ) - 1 ]
        dönüş ( orta1 + orta2 ) / 2

ile  açık ( sys . argv [ 1 ] + "input_hw_2.csv" ) olarak  dosya :
    histogram  =  hist ( dosya )
    aylar  =  histogram [ 1 ]
    histogram  =  histogram [ 0 ]
    dosyaYaz ( sys . argv [ 2 ])
    yazdır ( "Histogram:" , histogram )

def  dosyaYaz ( adres ):
    yaz  =  open ( adres + "180401104_hw_2_output.txt" , "w +" , kodlama = "UTF-8" )
    yaz . yazma ( f "Medyan: { medyan ( aylar ) } " )
    yaz . yazma ( f "Ortalama: { ort ( aylar ) } " )
    yaz . kapat ()
