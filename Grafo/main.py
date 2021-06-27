from parser_writer import guardar_grafo
from parser_writer import mostrar_grafo
from grafo import Grafo
"""""
# Generamos grafo de mallas con 30 nodos
grafo_malla_30 = Grafo(dirigido=False)
grafo_malla_30.grafo_malla(5, 6)
guardar_grafo(grafo_malla_30, "grafo_malla_30_nodos")
guardar_grafo(grafo_malla_30.KruskalD(),"grafo_malla_30_nodos_KruskalD")
guardar_grafo(grafo_malla_30.KruskalI(),"grafo_malla_30_nodos_KruskalI")
guardar_grafo(grafo_malla_30.Prim(),"grafo_malla_30_nodos_Prim")

"""""
"""""
# Generamos grafo de mallas con 500 nodos
grafo_malla_500 = Grafo(dirigido=False)
grafo_malla_500.grafo_malla(50, 10)
guardar_grafo(grafo_malla_500, "grafo_malla_500_nodos")
guardar_grafo(grafo_malla_500.KruskalD(), "grafo_malla_500_nodos_KruskalD")
guardar_grafo(grafo_malla_500.KruskalI(), "grafo_malla_500_nodos_KruskalI")
guardar_grafo(grafo_malla_500.Prim(), "grafo_malla_500_nodos_Prim")
"""""
"""""
# Generamos grafo Erdös y Rényi con 30 nodos y 200 aristas
grafo_erdos_30_200 = Grafo(dirigido=False)
grafo_erdos_30_200.grafo_erdos_renyi(30, 200)
guardar_grafo(grafo_erdos_30_200, "grafo_erdos_30_200")
guardar_grafo(grafo_erdos_30_200.KruskalD(), "grafo_erdos_30_200_KruskalD")
guardar_grafo(grafo_erdos_30_200.KruskalI(), "grafo_erdos_30_200_KruskalI")
guardar_grafo(grafo_erdos_30_200.Prim(), "grafo_erdos_30_200_Prim")


# Generamos grafo Erdös y Rényi con 500 nodos y 2500 aristas
grafo_erdos_500_2500 = Grafo(dirigido=False)
grafo_erdos_500_2500.grafo_erdos_renyi(500, 2500)
guardar_grafo(grafo_erdos_500_2500, "grafo_erdos_500_2500")
guardar_grafo(grafo_erdos_500_2500.KruskalD(),"grafo_erdos_500_2500_KruskalD")
guardar_grafo(grafo_erdos_500_2500.KruskalI(),"grafo_erdos_500_2500_KruskalI")
guardar_grafo(grafo_erdos_500_2500.Prim(),"grafo_erdos_500_2500_Prim")

# generamos grafo con modelo de Gilbert 30 nodos y probabilidad 0.5
grafo_gilbert_30_05 = Grafo(dirigido=False)
grafo_gilbert_30_05.grafo_gilbert(30, 0.5)
guardar_grafo(grafo_gilbert_30_05, "grafo_gilbert_30_05")
guardar_grafo(grafo_gilbert_30_05.KruskalD(),"grafo_gilbert_30_05_KruskalD")
guardar_grafo(grafo_gilbert_30_05.KruskalI(),"grafo_gilbert_30_05_KruskalI")
guardar_grafo(grafo_gilbert_30_05.Prim(),"grafo_gilbert_30_05_Prim")
# generamos grafo con modelo de Gilbert 500 nodos y probabilidad 0.02
grafo_gilbert_500_002 = Grafo(dirigido=False)
grafo_gilbert_500_002.grafo_gilbert(500, 0.02)
guardar_grafo(grafo_gilbert_500_002, "grafo_gilbert_500_002")
guardar_grafo(grafo_gilbert_500_002.KruskalD(),"grafo_gilbert_500_002_KruskalD()")
guardar_grafo(grafo_gilbert_500_002.KruskalI(),"grafo_gilbert_500_002_KruskalI()")
guardar_grafo(grafo_gilbert_500_002.Prim(),"grafo_gilbert_500_002_Prim")
"""""
"""""
# generamos grafo con modelo geográfico simple con 30 nodos y r=0.5
grafo_geografico_30_05 = Grafo(dirigido=False)
grafo_geografico_30_05.grafo_geografico(30, 0.5)
guardar_grafo(grafo_geografico_30_05, "grafo_geografico_30_05")
guardar_grafo(grafo_geografico_30_05.KruskalD(), "grafo_geografico_30_05_KruskalD")
guardar_grafo(grafo_geografico_30_05.KruskalI(), "grafo_geografico_30_05_KruskalI")
guardar_grafo(grafo_geografico_30_05.Prim(), "grafo_geografico_30_05_Prim")
# generamos grafo con modelo geográfico simple con 500 nodos y r=0.1
grafo_geografico_500_01 = Grafo(dirigido=False)
grafo_geografico_500_01.grafo_geografico(500, 0.15)
guardar_grafo(grafo_geografico_500_01, "grafo_geografico_500_01")
guardar_grafo(grafo_geografico_500_01.KruskalD(), "grafo_geografico_500_01_KruskalD")
guardar_grafo(grafo_geografico_500_01.KruskalI(), "grafo_geografico_500_01_KruskalI")
guardar_grafo(grafo_geografico_500_01.Prim(), "grafo_geografico_500_01_Prim")
"""""
"""""
# generamos grafo con modelo Barabási-Albert con 30 nodos y grado 10
grafo_babarasi_30_10 = Grafo(dirigido=False)
grafo_babarasi_30_10.grafo_barabasi_albert(30, 10, False, False)
guardar_grafo(grafo_babarasi_30_10, "grafo_babarasi_30_10")
guardar_grafo(grafo_babarasi_30_10.KruskalD(), "grafo_babarasi_30_10_Kruskal_D")
guardar_grafo(grafo_babarasi_30_10.KruskalI(), "grafo_babarasi_30_10_Kruskal_I")
guardar_grafo(grafo_babarasi_30_10.Prim(), "grafo_babarasi_30_10_Prim")

# generamos grafo con modelo Barabási-Albert con 500 nodos y grado 12
grafo_babarasi_500_12 = Grafo(dirigido=False)
grafo_babarasi_500_12.grafo_barabasi_albert(500, 15)
guardar_grafo(grafo_babarasi_500_12, "grafo_babarasi_500_12")
guardar_grafo(grafo_babarasi_500_12.KruskalD(), "grafo_babarasi_500_12_KruskalD")
guardar_grafo(grafo_babarasi_500_12.KruskalI(), "grafo_babarasi_500_12_KruskalI")
guardar_grafo(grafo_babarasi_500_12.Prim(), "grafo_babarasi_500_12_Prim")
"""""
# generamos grafo con modelo Dorogovtsev-Mendes con 30 nodos
grafo_dorogovtsev_mendes_30 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_30.dorogovtsev_mendes(30)
guardar_grafo(grafo_dorogovtsev_mendes_30, "grafo_dorogovtsev_mendes_30")
guardar_grafo(grafo_dorogovtsev_mendes_30.KruskalD(), "grafo_dorogovtsev_mendes_30_KruskalD")
guardar_grafo(grafo_dorogovtsev_mendes_30.KruskalI(), "grafo_dorogovtsev_mendes_30_KruskalI")
guardar_grafo(grafo_dorogovtsev_mendes_30.Prim(), "grafo_dorogovtsev_mendes_30_Prim")
# generamos grafo con modelo Dorogovtsev-Mendes con 500 nodos
grafo_dorogovtsev_mendes_500 = Grafo(dirigido=False)
grafo_dorogovtsev_mendes_500.dorogovtsev_mendes(500)
guardar_grafo(grafo_dorogovtsev_mendes_500, "grafo_dorogovtsev_mendes_500")
guardar_grafo(grafo_dorogovtsev_mendes_500.KruskalD(), "grafo_dorogovtsev_mendes_500_KruskalD")
guardar_grafo(grafo_dorogovtsev_mendes_500.KruskalI(), "grafo_dorogovtsev_mendes_500_KruskalI")
guardar_grafo(grafo_dorogovtsev_mendes_500.Prim(), "grafo_dorogovtsev_mendes_500_Prim")




