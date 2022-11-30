class IPaddress():
    def __init__(self, ip_stringa):
        self.ip_notazione_dec=ip_stringa
        self.ip_notazione_bin=None
        self.ip_broadcast=None

    def dec2bin(self):
        lista_bin=[]
        lista=self.toList()
        c=0
        s=""
        for n in lista:
            n=int(n)
            lista_bin.append(bin(n)[2:])

            temp=bin(n)[2:]
            temp="0"*(8-len(temp))+temp
            s = s + temp + "."

            c=c+1
        self.ip_notazione_bin=s[:-1]
        return self.ip_notazione_bin

    def toListBin(self):
        lista_bin=[]
        lista=self.toList()
        c=0
        s=""
        for n in lista:
            n=int(n)
            lista_bin.append(bin(n)[2:])

            c=c+1

        return lista_bin

    def bin2dec(self):
        lista_dec=[]
        lista=self.toListBin()
        c=0
        s=""
        for n in lista:
            lista_dec.append(int(n, 2))
            print(lista_dec[c])

            temp=str(int(n, 2))
            s = s + temp + "."

            c=c+1
        self.ip_notazione_dec=s[:-1]
        return self.ip_notazione_dec


    def toList(self):
        lista_stringhe=self.ip_notazione_dec.split(".")
        return [int(gruppo) for gruppo in lista_stringhe]

    """
    def ip_broadcast(self, subnet_mask):
        cont=0
        tmp=int(subnet_mask[1:])
        ip_bin=self.ip_notazione_bin
        for elemento in range(0, 32):
            if(elemento%8==0):
                pass
            else:
                if(cont>=tmp):
                    ip_bin[cont]='1'
                cont=cont+1
        return ip_bin
        """

    def ip_broadcast(self,subnet_mask):
        num = int(subnet_mask[1:])
        sub_bin = ""
        sub_bin = '0'*num + '1'*(32-num)
        """
        for w in range(0,32):
            if(w < num):
                sub_bin = sub_bin+"0"
            else:
                sub_bin = sub_bin+"1"
        """
        temp = ""
        for a in range(0,32):
            if(a % 8 == 0):
                temp =temp + "."
            else:
                pass
            if(self.ip_notazione_bin[a] == "0" and sub_bin[a] == "0"):
                temp = temp + '0'
            else:
                temp = temp + '1'

        self.ip_Broadcast=temp[1:]    
        return self.ip_Broadcast
            


def main():
    ip=input("Inserire un indirizzo ip: ")
    indirizzoIP=IPaddress(ip)
    sub=input("Inserire la subnet mask: ")
    print(indirizzoIP.ip_notazione_dec)
    print(indirizzoIP.toList())
    print(indirizzoIP.dec2bin())
    print(indirizzoIP.toListBin())
    print(indirizzoIP.bin2dec())
    print(str(indirizzoIP.ip_broadcast(sub)))

if __name__ == "__main__":
    main()