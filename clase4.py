def procesador():
    conceptos="""*El procesaodr o micro es la unidad mas importante.
*Conectado mediante un zocalo especifico.
*Sistema de refrigeracion que consta de un disipador de calor (Cobre o aluminio).
*Uno o mas ventiladores que eliminan el calor absorvido por el disipador.
*Entre el disipador y el microprocesador usualmente se coloca pasta terminca.
*Existen otros metodos, como la refrigeracion liquida o celulas de peltier.
*Una metrica del rendimiento es la frecuencia de reloj que permite comarar procesadores con nucleos de la misma familia.
*Un microprocesador puede estar constituido por varios nucles fisicos o logicos.
*Un nucleo fisico se refiere a una porcion interna casi independiente.
*Un nucleo logico es una simulacion de un nucleo fisico.
*Existe una tendencia de integrar un mayor numero de elementos dentro del propio procesador, aumentando asi la eficiencia energetica y la miniaturizacion. """
    khz="1hz es un ciclo. 1khz es 1000 ciclos"
    pc="""1ra: PC XT 8086 --> PC AT 80286-80386-XX4XX -> CompaQ PC IBM compatibles"""
    tiposArcPrincipal="CISC: AMD e Intel"
    cisc="""Complex instruction set computer -> Ventajas:
    *ejecuta instrucciones complejas,
    *menos codigo menos ram, 
    *instrucciones a mas de un ciclo de reloj, 
    *se requiere menos instrucciones para escribir software, 
    *mas sencillo en ensamblador, 
    *soporta estructuras complejas, 
    *menos registros.
    Desventajas:
    *Se puede requerir varios ciclos de reloj para completar instrucciones,
    *se usa el 20% del total de instrucciones,
    *genera mas temperatura, mas consumo y mas espacio fisico  """
    risc="""reduced instrution set computer processor --> Ventajas:
    *cada instruccion se ejecuta en un ciclo de reloj.
    *menor cantidad de transistores, reduce costos y tiempos.
    *basado en instrucciones simples."""
    frecuencia="""Indica a que velocidad trabaja el procesador.
    Es medida en Hz
    es una implementacion practica de conmutacion entre dos estados, o logica binaria.
    """
    setInstrucciones="""los procesadores incluyen instrucciones que facilitan la ejecucion de determinados codigos, x86,x64,MMX,3d Now, SSE, etc...
    """

def chipset():
    definicion="""Conjunto de chips o un cicuito integrado, con funciones relacionadas con la gestion de distintos dispositivos.
    el chipset siempre se diseño en base a la arquitectura del procesador central.
    es el control de comunicaciones y el o los chips que se encargan de controlar el trafico de datos en la placa base.
    Encontramos dos chipsets en la plaza, el puente norte y el puente sur.
    la placa base como el bus principal del sistema, es el eje que es capaz de interconectar elementos de diferentes fabricantes.
    desde su aparicion, su funcion fue clara, dismuniur la carga de trabajo del procesador principal, derivandolo en otros circuitos que a su vez se conectaban con el."""
    northBridge="""Sus funciones se encuentran actualmentee en la CPU."""
    caché="""es una memoria ultrarrapida que emplea el procesador para tener alcance directo a ciertos datos imprescindibles que sera utilizadas en las siguientes operaciones:
    Cache L1: es la memoria mas pequeña y mas rapida, tiene 256kb, alcaza """