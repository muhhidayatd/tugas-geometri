import muhhidayatd

def main():

    t = 10
    n = 6

    T = muhhidayatd.periodeGetaran (t,n)
    f = muhhidayatd.frekuensiGetaran(n, t)
  
    print("Getaran")
    print("Periode getaran\t\t: ", T)
    print("Frekuensi\t\t: ",f)

    frekuensi=10

    periode = muhhidayatd.periodeGetaran2(frekuensi)
    print("Periode getaran\t\t: ",periode)

if __name__ == "__main__":
    main()
