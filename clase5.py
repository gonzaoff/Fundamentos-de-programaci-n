class cls5RedesEInternet():
    def tiposDeRedes(self):
        origen = "Origen: guerras y la necesidad de poder comunicarse a largas distancias\n"
        datosE = """58: Bell creo el primer modem \n62:ARPA comienza a estudiar ideas de red local\n67: ARPA trabaja en un sistema de intercambio de paquetes en redes de info\n71: Contaba con 23 nodos\nwww(word wide web y http): 1990 aparece y se extiende el concepto de internet\nWWW es un sistema de distribucion y compartimento de documentos de hipertexto\nGracias a el HTTP queda defnida la sintaxis y la semantica que se utilizan los elementos de la arquitectura web para comunicarse\nEl primer navegador y buscador de la historia fue Mosaic en 1993(posteriormente "netcape"), se abandono el proyecto por la aparicion de Firefox y Explorer.\nEn nuestros dias conocemos el internet de las cosas\n """
        conceptoDeRedDeDatos = "Una red de datos es aquella infraestructura que ha sido creada con el objetivo de transmitir datos desde un punto a otro\nNo solo intervienen ordenadores, sino que el elemento mas importante son los servidores.\n"
        tipoDeRedesLan = "Una red lan o de area local, es una red de comunicaciones construida mediante la interconexion de nodos mediante cables o medios inalambricos.\nEsta limitado por medios fisicos.\n"
        tipoDeRedesMAN = "Metropolitan area network\nEs el paso intermedio entre una red LAN y una red WAN, ya que la extension de este tipo de redes comprende el territorio de una gran ciudad.\nEstas salen al exterior a travez de un CPD o una centralita general."
        tipoDeRedesWAN = "Wide area network\nNo tiene limite predefinido\n\n"
        return origen + datosE + conceptoDeRedDeDatos + tipoDeRedesLan + tipoDeRedesMAN + tipoDeRedesWAN

    def topologia(self):
        definicion = "Def: Tenemos una arquitectura de conexion o topologia.\n"
        topoBus = "Bus: Se trata de un cable central en el que cuelgan distintos nodos de la red\nEste tronco debe ser un cable de alta capacidad, como coaxiall o fibra optica, y admite ramificaciones\nSu venaja es la sencillez y escalabilidad pero si falla el tronco falla la red\n"
        topoAnillo = "Anillo: Es una res que se cierra ella misma tambien denominada...\n"
        topoEstrella = "Estrella: Es la mas utilizada aunque no la mas economica. Aqui tnemos un elemento central como puerta de enlace que puede ser un router, switch o hub, en donde conecta cada nodo.\n Si la puerta de enlace se rompe, la red se cae, pero si un nodo falla los demas no se ven afectados. Una red inalambrica utiliza esta tecnologia.\n\n"
        return definicion + topoAnillo + topoBus + topoEstrella

    def modOSI(self):
        modeloOSI = "Principales protocolos que interviene en la comunicacion.\nProtocolo: conjunto de reglas que se encargan de regir el intercambio de informacion a traves de una red.\nPara clasificarestos protocolos, el estandar de comunicacion OSI creo un modelo dividido en 7 capas en donde se definen y explican los conceptos de comunicacion de una red.\nModelo Conceptual.\n"
        osiCap1 = "92:Red telefonica.\nDSL: Acceso a la red con datos digitales, cables de parez trenzados.\nEthernet: estandar de conexion, variantes segun la capacidad y velocidad del cable.\nGSM:inyerfaz de conexion mediante radiofrecuencia..\n"
        osiCap2 = "Direccionamiento Fisico\nPPP: es el protocolo punto a punto mediante el cual dos nodos de una red se conectan diretamente y sin intermediarios.\nHDLC:Otro protocolo punto a punto que se encarga de la recuperacion de errores por perdida de paquetes.\nFDDI: controla la interfaz de datos distribuida por fibra, basada en token ring y con conexiones de tipo duplex.\nVPN-T2TP:..."
        osiCap3 = "Datos desde el transmisor al recepetor. conmutaciones y encaminamientos necesarios entre las distintas redes conectadas\nIPv4,IPv6 e IPsec: Protocolo de internet mas famoso. Es un protocolo no orientado a conexion, es decir transfiere datagramas (MTU) de punto a punto por la mejor ruta que encuentre el propio paquete\nICMP:Protocolo de control de mensajes de internet que forma parte de IP y se encarga de enviar mensaje de error.\nARP: protocolo de resolucion de direcciones que sirve para encontrar la direccion MAC del hardware relacionado con su IP.\n"
        osiCap4 = "Transporte: transporte de los datos que se encuentra dentro del paquete de transmision desde el origen al destino. Independiente de la red.\nTCP: protocolo de control de transmision, los nodos pueden comunicarse de forma segura. Hace que los datos se envien en segmento encappsulados con un ACK oara que el protocolo IP envie como estime oportuni con capacidad de multiplexacion. El destino se encargara nuevamente de unir estos segmentos. Este protocolo es orientado a conexion porque verifica que la informacion se reciba.\nUDP:User datagram protocol, el funcionamiento es similar a TCP solo que en este caso es el protocolo no orientado a la conexion.\n"
        osiCap7 = "Permite a los usuarios ejecutar acciones t comandos en las propias aplicaciones. Aqui tambien tenemos protocolos\nDNS:Sistema de nombres de dominio. Traduce direcciones de nombre de dominio a IP. Va desde la zona punto (final), zona a zona de izquierda a derecha hasta que completa la IP. \n\n"
        return modeloOSI + osiCap1 + osiCap2 + osiCap3 + osiCap4 + osiCap7
    
    def redes(self):
        redesVPN="VPN:Una vpn es una red local o interna en la que los usuarios conectados a ella pueden estar separados geograficamente\nDicho de otra forma, es una red LAN que podremos extender hasta la propia red publica.\nTodas las conexiones a internet de forma segura y fiable sin necesidad de estar fisicamente donde esta nuestra red interna\nBeneficios: Mayor seguridad en conexiones publicas, evita ciertos bloqueos segun paises o zonas geograficas, evitar la censura en nuestro propio proveedor de servisios de internet"
        redesIoT="IoT=internet de las cosas\nInterconexion, a travez de una red, de todo tipo de objetos cotidianos a internet."
        return redesVPN + redesIoT
        
clase5=cls5RedesEInternet()
modOSI=clase5.modOSI()
tiposDeRedes=clase5.tiposDeRedes()
topo=clase5.topologia()
redes=clase5.redes()

print(topo)