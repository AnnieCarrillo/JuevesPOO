from cosas imporrt Libro

def main():
        l1 = libro_planeta("El perfume",Autor("Patrik", "PS"), 1980)
        print(l1)
        #Codigo para cambiar el pseudonimo
        l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
        print(l1)
        print("-------------Herencia-----------")
        al2 = Alumno("Jose, 19, "23232", "ICO", 9")
        Al2.nombre = "Pepe"
        print(vars(al2))

main()

