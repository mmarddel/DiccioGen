import os

if __name__ == '__main__':
    print "______  _              _         _____              "
    print "|  _  \(_)            (_)       |  __ \             "
    print "| | | | _   ___   ___  _   ___  | |  \/  ___  _ __  "
    print "| | | || | / __| / __|| | / _ \ | | __  / _ \| '_ \ "
    print "| |/ / | || (__ | (__ | || (_) || |_\ \|  __/| | | |"
    print "|___/  |_| \___| \___||_| \___/  \____/ \___||_| |_|"
    print "Creado por: Franco Casas"
    print "\n"

    
    while True:
        op = int(raw_input("Seleccione la cantidad de datos que posee (entre 3 - 8). presione 9 para salir: "))

        if op==3:
            a = raw_input("Dato N 1: ")
            b = raw_input("Dato N 2: ")
            c = raw_input("Dato N 3: ")
            
            print "\n"
            print "Combinaciones posibles"
            print "\n"
            print a
            print a+b
            print a+c
            print a+b+c
            print a+c+b
            print b
            print b+a
            print b+c
            print b+a+c
            print b+c+a
            print c
            print c+a
            print c+b
            print c+a+b
            print c+b+a
            print "\n"

        if op==4:
            a = raw_input("Dato N 1: ")
            b = raw_input("Dato N 2: ")
            c = raw_input("Dato N 3: ")
            d = raw_input("Dato N 4: ")

            print "\n"
            print "Combinaciones posibles"
            print "\n"
            print a
            print a+b
            print a+c
            print a+d
            print a+b+c
            print a+c+b
            print a+b+d
            print a+d+b
            print a+c+d
            print a+d+c
            print a+b+c+d
            print a+b+d+c
            print a+c+b+d
            print a+c+d+b
            print a+d+c+b
            print a+d+b+c
            print b
            print b+a
            print b+c
            print b+d
            print b+a+c
            print b+c+a
            print b+d+a
            print b+a+d
            print b+c+d
            print b+d+c
            print b+a+c+d
            print b+a+d+c
            print b+c+d+a
            print b+c+a+d
            print b+d+a+c
            print b+d+c+a
            print c
            print c+a
            print c+b
            print c+d
            print c+a+b
            print c+b+a
            print c+a+d
            print c+d+a
            print c+b+d
            print c+d+b
            print c+a+b+d
            print c+a+d+b
            print c+b+a+d
            print c+b+d+a
            print c+d+b+a
            print c+d+a+b
            print d
            print d+a
            print d+b
            print d+c
            print d+a+b
            print d+b+a
            print d+a+c
            print d+c+a
            print d+b+c
            print d+c+b
            print d+a+b+c
            print d+a+c+b
            print d+b+a+c
            print d+b+c+a
            print d+c+a+b
            print d+c+b+a
            print "\n"
            
        if op==5:
            a = raw_input("Dato N 1: ")
            b = raw_input("Dato N 2: ")
            c = raw_input("Dato N 3: ")
            d = raw_input("Dato N 4: ")
            e = raw_input("Dato N 5: ")

            print "Estamos trabajando para generar mas combinaciones."

        if op==6:
            a = raw_input("Dato N 1: ")
            b = raw_input("Dato N 2: ")
            c = raw_input("Dato N 3: ")
            d = raw_input("Dato N 4: ")
            e = raw_input("Dato N 5: ")
            f = raw_input("Dato N 6: ")

            print "Estamos trabajando para generar mas combinaciones."

        if op==7:
            a = raw_input("Dato N 1: ")
            b = raw_input("Dato N 2: ")
            c = raw_input("Dato N 3: ")
            d = raw_input("Dato N 4: ")
            e = raw_input("Dato N 5: ")
            f = raw_input("Dato N 6: ")
            g = raw_input("Dato N 7: ")

            print "Estamos trabajando para generar mas combinaciones."

        if op==8:
            a = raw_input("Dato N 1: ")
            b = raw_input("Dato N 2: ")
            c = raw_input("Dato N 3: ")
            d = raw_input("Dato N 4: ")
            e = raw_input("Dato N 5: ")
            f = raw_input("Dato N 6: ")
            g = raw_input("Dato N 7: ")
            h = raw_input("Dato N 8: ")

            print "Estamos trabajando para generar mas combinaciones."

        
        
        
        print "Presione <Enter> para continuar"
        raw_input()
        os.system('clear')
        
        
        if op==9:
            print "Gracias por utilizar:"
            print "\n"
            print "______  _              _         _____              "
            print "|  _  \(_)            (_)       |  __ \             "
            print "| | | | _   ___   ___  _   ___  | |  \/  ___  _ __  "
            print "| | | || | / __| / __|| | / _ \ | | __  / _ \| '_ \ "
            print "| |/ / | || (__ | (__ | || (_) || |_\ \|  __/| | | |"
            print "|___/  |_| \___| \___||_| \___/  \____/ \___||_| |_|"
            print "Creado por: Franco Casas"
            
            break
           





