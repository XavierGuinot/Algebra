from typing import *

d10 = {"id": (1, 2, 3, 4, 5), "r1": (5, 1, 2, 3, 4), "r2": (4, 5, 1, 2, 3), "r3": (3, 4, 5, 1, 2),
       "r4": (2, 3, 4, 5, 1), "s1": (1, 5, 4, 3, 2),
       "s2": (3, 2, 1, 5, 4), "s3": (5, 4, 3, 2, 1), "s4": (2, 1, 5, 4, 3), "s5": (4, 3, 2, 1, 5)}

d10nombres = {(1, 2, 3, 4, 5): "id", (5, 1, 2, 3, 4): "r1", (4, 5, 1, 2, 3): "r2", (3, 4, 5, 1, 2): "r3",
              (2, 3, 4, 5, 1): "r4", (1, 5, 4, 3, 2): "s1",
              (3, 2, 1, 5, 4): "s2", (5, 4, 3, 2, 1): "s3", (2, 1, 5, 4, 3): "s4", (4, 3, 2, 1, 5): "s5"}

d10expl = {"id": "id: aplicación identidad", "r1": "r1: rotación en sentido antihorario de (2/5)*pi",
           "r2": "r2: rotación en sentido antihorario de (4/5)*pi",
           "r3": "r3: rotación en sentido antihorario de (6/5)*pi",
           "r4": "r4: rotación en sentido antihorario de (8/5)*pi",
           "s1": "s1: reflexión respecto al eje que pasa por vértice 1",
           "s2": "s2: reflexión respecto al eje que pasa por vértice 2",
           "s3": "s3: reflexión respecto al eje que pasa por vértice 3",
           "s4": "s4: reflexión respecto al eje que pasa por vértice 4",
           "s5": "s5: reflexión respecto al eje que pasa por vértice 5"}

ID = 1, 2, 3, 4, 5

"Función que calcula la rotación o reflexión sobre cualquier pentagono, el primer parámetro f es la tupla que define la" \
"función que queremos aplicar y el segundo parámentro p es el pentágono sobre el cual hacer la función"
"ADVERTENCIA: aunque para nosotros la primera posición del pentágono viene representada por el 1, para el ordenador" \
"la primera posición de la tupla pentágono es t[0]"


def funcion(f: Tuple[int, int, int, int, int], p: Tuple[int, int, int, int, int]) -> Tuple[int, int, int, int, int]:
    return (p[f[0] - 1], p[f[1] - 1], p[f[2] - 1], p[f[3] - 1], p[f[4] - 1])


cayley = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

i = 0  # indice de la fila
j = 0  # indice de la columna
"v1*v2=v2ºv1"
for v1 in d10.values():  #
    j = 0
    for v2 in d10.values():
        prueba = funcion(v1, v2)
        cayley[i][j] = d10nombres[funcion(v2, v1)]
        j += 1
    i += 1


def dibujar():
    print("         REPRESENTACIÓN DE TODAS LAS ROTACIONES Y SIMETRÍAS")
    for key, value in d10.items():
        print("_____________________________________________________________________________________")
        print("             ", d10expl[key])
        print("_____________________________________________________________________________________")
        print("")
        print(f"        1                                                      {value[0]}")
        print("")
        print(f"2               5                                     {value[1]}                {value[4]}")
        print(f"                             === {key} ===> ")
        print("")
        print(f"    3        4                                            {value[2]}        {value[3]}")
        print("")


def imprimir():
    print("Nota: r1(1ªcolumna) * r2(1ªfila) = r2 º r1 , siendo 'º' la composición de aplicaciones")
    print("")
    print("       TABLA DE CAYLEY DE D10 (PENTÁGONO)")
    print("")
    print("      id  r1  r2  r3  r4  s1  s2  s3  s4  s5")
    print("    __________________________________________")
    for fila in cayley:
        print(f"{fila[0]}  ", end="")
        for e in fila:
            print(f"  {e}", end="")
        print("")
    print("    __________________________________________")


def sub1():
    print("")
    print("LOS SUBGRUPOS DE D1O DE 1 ELEMENTOS SON: ")
    for key, value in d10.items():
        if funcion(value, value) == d10["id"]:
            print("     -{", end="")
            print(f"{key}", end="")
            print("}")


def sub1detallado():
    print("")
    print(
        "Nota 1: r1 * r2 = r2 º r1 , siendo 'º' la composición de aplicaciones. (r1)^-1 es la inversa de r1")
    print("Nota 2: las combinaciones que no incluyen a la identidad no son analizados, ya que es trivial que no pueden "
          "ser subgrupo")
    print("Nota 3: en el caso particular de los subgrupos de 1 elementos, solo aquellos que sus inversos son ellos"
          " mismos serán subgrupo")
    print("")
    "misma funcion que sub5() pero que explica porque cada conbinación no es subgrupo"
    print("ANÁLISIS DE TODOS LOS SUBCONJUNTOS DE 1 ELEMENTOS DE D10:")
    for key, value in d10.items():
        if funcion(value, value) == d10["id"]:
            print("     > Este subconjunto SÍ es subgrupo, { ", end="")
            print(f"{key}", end="")
            print(" }")
        else:
            print("     > Este subconjunto NO es subgrupo, { ", end="")
            print(f"{key}", end="")
            print(" }, ya que", f"{key} * {key} = {d10nombres[funcion(value, value)]} =/=", "{id}")


def sub2():
    print("")
    print("Nota 1: las combinaciones que no incluyen a la identidad no son analizados, ya que es trivial que no pueden "
          "ser subgrupo")
    print("LOS SUBGRUPOS DE D1O DE 2 ELEMENTOS SON: ")
    combinaciones = 0  # número de combinaciones sin repetición analizados
    d10inversas = {"id": "id", "r1": "r4", "r2": "r3", "r3": "r2", "r4": "r1", "s1": "s1", "s2": "s2", "s3": "s3",
                   "s4": "s4", "s5": "s5"}
    setpresentes = set()
    """dado a que {id,s1,s2,s3,s4} es el mismo suscnjunto que {s1,id,s2,s3,s4}, 
    pondremos todos los subconjuntos analizados en un set para comprobar que no se repiten"""
    for k1, v1 in d10.items():
        for k2, v2 in d10.items():
            flag = 0  # suponemos que es un subgrupo, si no flag=1
            setactual = set()
            setactual.add(k2)
            setactual.add(k1)
            if "id" in setactual and len(setactual) == 2 and setactual not in setpresentes:
                setpresentes.add(frozenset(setactual))
                combinaciones += 1
                for f1 in setactual:
                    for f2 in setactual:
                        if d10nombres[funcion(d10[f1], d10[d10inversas[f2]])] not in setactual:
                            flag = 1
                            break
                    if flag == 1:
                        break
                if flag == 0:
                    print("     >{", end="")
                    print(f"{k1},{k2}", end="")
                    print("}")

    print(f"El número de combinaciones analizadas es de: {combinaciones}")

def sub2detallado():
    print("")
    print(
        "Nota 1: r1 * r2 = r2 º r1 , siendo 'º' la composición de aplicaciones. (r1)^-1 es la inversa de r1")
    print("Nota 2: las combinaciones que no incluyen a la identidad no son analizados, ya que es trivial que no pueden "
          "ser subgrupo")
    print("")
    print("ANÁLISIS DE TODOS LOS SUBCONJUNTOS DE 2 ELEMENTOS DE D10:")
    combinaciones = 0  # número de combinaciones sin repetición analizados
    d10inversas = {"id": "id", "r1": "r4", "r2": "r3", "r3": "r2", "r4": "r1", "s1": "s1", "s2": "s2", "s3": "s3",
                   "s4": "s4", "s5": "s5"}
    setpresentes = set()
    """dado a que {id,s1,s2,s3,s4} es el mismo suscnjunto que {s1,id,s2,s3,s4}, 
    pondremos todos los subconjuntos analizados en un set para comprobar que no se repiten"""
    for k1, v1 in d10.items():
        for k2, v2 in d10.items():

                        flag = 0  # suponemos que es un subgrupo, si no flag=1
                        setactual = set()
                        setactual.add(k1)
                        setactual.add(k2)

                        if "id" in setactual and len(setactual) == 2 and setactual not in setpresentes:
                            setpresentes.add(frozenset(setactual))
                            combinaciones += 1
                            for f1 in setactual:
                                for f2 in setactual:
                                    if d10nombres[funcion(d10[f1], d10[d10inversas[f2]])] not in setactual:
                                        flag = 1
                                        noes = "ya que: " \
                                               f"{f1} * ({f2})^-1 = {f1} * {d10inversas[f2]} = {d10inversas[f2]} º {f1} " \
                                               f"= {d10nombres[funcion(d10[f1], d10[d10inversas[f2]])]} (que no está " \
                                               f"en el subconjunto analizado)"
                                        break
                                if flag == 1:
                                    break
                            if flag == 0:
                                print("     > Este subconjunto SÍ es subgrupo, { ", end="")
                                print(f"{k2},{k1}", end="")
                                print(" }")
                            if flag == 1:
                                print("     > Este subconjunto NO es subgrupo, {", f"{k2},{k1}", "},",
                                      noes)
    print("")
    print(f"El número de combinaciones analizadas es de: {combinaciones}")


def sub5():
    print("")
    print("LOS SUBGRUPOS DE D1O DE 5 ELEMENTOS SON: ")
    combinaciones = 0  # número de combinaciones sin repetición analizados
    d10inversas = {"id": "id", "r1": "r4", "r2": "r3", "r3": "r2", "r4": "r1", "s1": "s1", "s2": "s2", "s3": "s3",
                   "s4": "s4", "s5": "s5"}
    setpresentes = set()
    """dado a que {id,s1,s2,s3,s4} es el mismo suscnjunto que {s1,id,s2,s3,s4}, 
    pondremos todos los subconjuntos analizados en un set para comprobar que no se repiten"""
    for k1, v1 in d10.items():
        for k2, v2 in d10.items():
            for k3, v3 in d10.items():
                for k4, v4 in d10.items():
                    for k5, v5 in d10.items():
                        flag = 0  # suponemos que es un subgrupo, si no flag=1
                        setactual = set()
                        setactual.add(k5)
                        setactual.add(k4)
                        setactual.add(k3)
                        setactual.add(k2)
                        setactual.add(k1)
                        if "id" in setactual and len(setactual) == 5 and setactual not in setpresentes:
                            setpresentes.add(frozenset(setactual))
                            combinaciones += 1
                            for f1 in setactual:
                                for f2 in setactual:
                                    if d10nombres[funcion(d10[f1], d10[d10inversas[f2]])] not in setactual:
                                        flag = 1
                                        break
                                if flag == 1:
                                    break
                            if flag == 0:
                                print("     >{", end="")
                                print(f"{k5},{k4},{k3},{k2},{k1}", end="")
                                print("}")

    print(f"El número de combinaciones analizadas es de: {combinaciones}")


def sub5detallado():
    print("")
    print(
        "Nota 1: r1 * r2 = r2 º r1 , siendo 'º' la composición de aplicaciones. (r1)^-1 es la inversa de r1")
    print("Nota 2: las combinaciones que no incluyen a la identidad no son analizados, ya que es trivial que no pueden "
          "ser subgrupo")
    print("")
    "misma funcion que sub5() pero que explica porque cada conbinación no es subgrupo"
    print("ANÁLISIS DE TODOS LOS SUBCONJUNTOS DE 5 ELEMENTOS DE D10:")
    combinaciones = 0  # número de combinaciones sin repetición analizados
    d10inversas = {"id": "id", "r1": "r4", "r2": "r3", "r3": "r2", "r4": "r1", "s1": "s1", "s2": "s2", "s3": "s3",
                   "s4": "s4", "s5": "s5"}
    setpresentes = set()
    """dado a que {id,s1,s2,s3,s4} es el mismo suscnjunto que {s1,id,s2,s3,s4}, 
    pondremos todos los subconjuntos analizados en un set para comprobar que no se repiten"""
    for k1, v1 in d10.items():
        for k2, v2 in d10.items():
            for k3, v3 in d10.items():
                for k4, v4 in d10.items():
                    for k5, v5 in d10.items():
                        flag = 0  # suponemos que es un subgrupo, si no flag=1
                        setactual = set()
                        setactual.add(k1)
                        setactual.add(k2)
                        setactual.add(k3)
                        setactual.add(k4)
                        setactual.add(k5)
                        if "id" in setactual and len(setactual) == 5 and setactual not in setpresentes:
                            setpresentes.add(frozenset(setactual))
                            combinaciones += 1
                            for f1 in setactual:
                                for f2 in setactual:
                                    if d10nombres[funcion(d10[f1], d10[d10inversas[f2]])] not in setactual:
                                        flag = 1
                                        noes = "ya que: " \
                                               f"{f1} * ({f2})^-1 = {f1} * {d10inversas[f2]} = {d10inversas[f2]} º {f1}" \
                                               f" = {d10nombres[funcion(d10[f1], d10[d10inversas[f2]])]} (que no está " \
                                               f"en el subconjunto analizado)"
                                        break
                                if flag == 1:
                                    break
                            if flag == 0:
                                print("     > Este subconjunto SÍ es subgrupo, { ", end="")
                                print(f"{k5},{k4},{k3},{k2},{k1}", end="")
                                print(" }")
                            if flag == 1:
                                print("     > Este subconjunto NO es subgrupo, {", f"{k5},{k4},{k3},{k2},{k1}", "},",
                                      noes)
    print("")
    print(f"El número de combinaciones analizadas es de: {combinaciones}")

def sub10():
    print("Es trivial que el único subgrupo de 10 posible es el propio D10 = { id,r1,r2,r3,r4,s1,s2,s3,s4,s5 }")

def subnormales():
    subg = (("id"),("s1"),("s2"),("s3"),("s4"),("s5"),("id","s1"),("id","s2"),("id","s3"),("id","s4"),
            ("id","s5"),("r4","r3","r2","r1","id"),("id","r1","r2","r3","r4","s1","s2","s3","s4","s5"))
    print("ANÁLISIS DE LOS SUBGRUPOS NORMALES")
    print("")
    print("Vamos a analizar si se cumple la definición de subgrupo normal en todos los subgrupos de D10, para ello ")
    print("calcularemos todas las clases de equivalencia, izquierdas y derechas, de los subgrupos con todos los elementos de D10")
    print("")
    print("Nota: Hs4 es la clase derecha de s4 en H (siendo H el subgrupo analizado y s4 el elemento de D10")
    print("")
    for sub in subg:
        flag = 0  # suponemos que es normal
        if sub in ("id", "s1", "s2", "s3", "s4", "s5"):
            print("Vamos a analizar el subgrupo : H = {", f"{sub}", "}")
        else:
            print("Vamos a analizar el subgrupo :  H = {",end="")
            for e in sub:
                if e == sub[0]:
                    print(f"{e}", end="")
                else:
                    print(f",{e}", end="")
            print("}")
        for v in d10.values():
            claiz = set()
            cladr = set()
            if sub in ("id","s1","s2","s3","s4","s5"):
                cladr.add(d10nombres[funcion(v, d10[sub])])
                claiz.add(d10nombres[funcion(d10[sub], v)])
                if claiz == cladr:
                    print(f"     {d10nombres[v]}H = {cladr} = {claiz} = H{d10nombres[v]}")
                else:
                    print(f"     {d10nombres[v]}H = {cladr} =/= {claiz} = H{d10nombres[v]}")
                    flag = 1
                    break
            else:
                for e in sub:  #v hace de x y d10[v] de h en xH (clases)
                    cladr.add(d10nombres[funcion(v,d10[e])])
                    claiz.add(d10nombres[funcion(d10[e],v)])
                if claiz == cladr:
                    print(f"     {d10nombres[v]}H = {cladr} = {claiz} = H{d10nombres[v]}")
                else:
                    print(f"     {d10nombres[v]}H = {cladr} =/= {claiz} = H{d10nombres[v]}")
                    flag = 1
                    break
            if flag == 1:
                break
        print("")
        if flag == 0:
            print("El subgrupo SÍ es normal")
        else:
            print("El subgrupo NO es normal")
        print("")
        print("")

def centro():
    setcentro = set()
    print("")
    print("ANALISIS DEL CENTRO DE D10")
    print("")
    for kanal,vanal in d10.items():
        print("")
        print("Vamos a ver si",{kanal},"forma parte del centro:")
        flag = 0 # suponemos que es parte del centro
        for vcom in d10.values():
            xy=funcion(vanal,vcom)
            yx=funcion(vcom,vanal)
            if xy == yx:
                print(f"    {d10nombres[vanal]} * {d10nombres[vcom]} = {d10nombres[xy]} = {d10nombres[vcom]} * {d10nombres[vanal]}")
            else:
                print(f"    {d10nombres[vanal]} * {d10nombres[vcom]} = {d10nombres[xy]} =/= {d10nombres[yx]} = {d10nombres[vcom]} * {d10nombres[vanal]}")
                flag = 1
                break
        if flag == 0:
            print("{",f"{kanal}","} forma parte del nucleo")
            setcentro.add(kanal)
        else:
            print("{",f"{kanal}","} no forma parte del nucleo")
    print("")
    print("Así, el centro de D10 es: { ",end="")
    for e in setcentro:
        print(f"{e}",end="")
    print(" }")


def menu():
    print("")
    print("Programa escrito por Xavier Guinot Canlles")
    print("")
    print("Bienvenido al maravilloso mundo de las rotaciones y simentrías de un pentágono regular, llamémosle D10")
    print("¿Qué quieres hacer? Selecciona una opción (teclea el número asociado), si quieres salir del menú teclea -1:")
    print("     1.- Ver como se han definido las rotaciones y simetrías")
    print("     2.- Ver la tabla de Cayley de D10 ")
    print("     3.- Ver subgrupos de 1 elemento")
    print("     4.- Ver subgrupos de 2 elementos")
    print("     5.- Ver subgrupos de 2 elementos de manera detallada (todas las combinaciones y explicación de si son o no)")
    print("     6.- Ver subgrupos de 5 elementos")
    print("     7.- Ver subgrupos de 5 elementos de manera detallada (todas las combinaciones y explicación de si son o no)")
    print("     8.- Ver subgrupos de 10 elementos")
    print("     9.- Ver todos los subgrupos")
    print("    10.- Ver todos los subgrupos de manera detallada")
    print("    11.- Ver los subgrupos normales")
    print("    12.- Ver el centro")
    print("    13.- Verlo todo")
    print("")
    opcion = int(input("Selecciona opción: "))
    while opcion != -1:
        if opcion == 1:
            print("***************************************************************************************************************************************************")
            dibujar()
        elif opcion == 2:
            print("***************************************************************************************************************************************************")
            imprimir()
        elif opcion == 3:
            print("***************************************************************************************************************************************************")
            sub1()
        elif opcion == 4:
            print("***************************************************************************************************************************************************")
            sub2()
        elif opcion == 5:
            print("***************************************************************************************************************************************************")
            sub2detallado()
        elif opcion == 6:
            print("***************************************************************************************************************************************************")
            sub5()
        elif opcion == 7:
            print("***************************************************************************************************************************************************")
            sub5detallado()
        elif opcion == 8:
            print("***************************************************************************************************************************************************")
            sub10()
        elif opcion == 9:
            print("***************************************************************************************************************************************************")
            sub1()
            print(
                "***************************************************************************************************************************************************")
            sub2()
            print(
                "***************************************************************************************************************************************************")
            sub5()
            print(
                "***************************************************************************************************************************************************")
            sub10()
        elif opcion == 10:
            print(
                "***************************************************************************************************************************************************")
            sub1()
            print(
                "***************************************************************************************************************************************************")
            sub2detallado()
            print(
                "***************************************************************************************************************************************************")
            sub5detallado()
            print(
                "***************************************************************************************************************************************************")
            sub10()
        elif opcion == 11:
            print("***************************************************************************************************************************************************")
            subnormales()
            print(
                "***************************************************************************************************************************************************")
        elif opcion == 12:
            print(
                "***************************************************************************************************************************************************")
            centro()
            print(
                "***************************************************************************************************************************************************")
        elif opcion == 13:
            print(
                "***************************************************************************************************************************************************")
            dibujar()
            print(
                "***************************************************************************************************************************************************")
            imprimir()
            print(
                "***************************************************************************************************************************************************")
            sub1()
            print(
                "***************************************************************************************************************************************************")
            sub2detallado()
            print(
                "***************************************************************************************************************************************************")
            sub5detallado()
            print(
                "***************************************************************************************************************************************************")
            sub10()
            print(
                "***************************************************************************************************************************************************")
            subnormales()
            print(
                "***************************************************************************************************************************************************")
            centro()
            print(
                "***************************************************************************************************************************************************")
        else:
            print("***************************************************************************************************************************************************")
            print("Introduce una opción correcta")
        print("")
        print("____________________________________________________________________________________________________________")
        print(
            "¿Qué quieres hacer? Selecciona una opción (teclea el número asociado), si quieres salir del menú teclea -1:")
        print("     1.- Ver como se han definido las rotaciones y simetrías")
        print("     2.- Ver la tabla de Cayley de D10 ")
        print("     3.- Ver subgrupos de 1 elemento")
        print("     4.- Ver subgrupos de 2 elementos")
        print(
            "     5.- Ver subgrupos de 2 elementos de manera detallada (todas las combinaciones y explicación de si son o no)")
        print("     6.- Ver subgrupos de 5 elementos")
        print(
            "     7.- Ver subgrupos de 5 elementos de manera detallada (todas las combinaciones y explicación de si son o no)")
        print("     8.- Ver subgrupos de 10 elementos")
        print("     9.- Ver todos los subgrupos")
        print("    10.- Ver todos los subgrupos de manera detallada")
        print("    11.- Ver los subgrupos normales")
        print("    12.- Ver el centro")
        print("    13.- Verlo todo")
        print("")
        opcion = int(input("Selecciona opción: "))

menu()

