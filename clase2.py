class clase2():
    def Arc(self):
        arquitecturaHardvard = """Resuelve el cuello de botella de Von Neumann con ciclos de reloj,
        lo que conlleva un mayor costo\n"""
        print(arquitecturaHardvard)
    def logicaProposicional(self):
        Definicion="""Definicion: Establece proposiciones logicas que poseen un valor Verdadero o Falso (true or false). Nos devuelve un razonamiento logico a un razonamiento binario\n"""
        conectoresLogicos = """Conectores Logicos ->
Negacion(Not): Cambia el valor de verdad de la proposicion. Ej: Si p es VERDADERO, NOT p es FALSO
Conjuncion(AND): Relaciona dos proposiciones, el valor de verdad de la conjuncion es VERDADERO, solo si el valor de las dos proposiciones es VERDADERO
Disyuncion(OR): Relaciona dos proposiciones, el valor de verdad de la conjuncion es FALSO, solo si el valor de las dos proposiciones es FALSO
"""
        ejercicios= """1. X > Y
2. X < Y < Z
3. X > 100 OR X+Y > Z
4. X < 0 AND Z - 325 > 0
5. X >= 18
6. Z/Y/X >= Fecha_nac."""
        print(Definicion,conectoresLogicos,ejercicios)

class Binario(clase2):
    def funcion(self):
        definicion="Sistema de numeracion, utilizando solo 2 digitos (0 y 1) == Dos niveles de voltaje.\n"
        print(definicion)

class memoria(Binario):
        def BIOS(self):
            concepto="""Concepto: Rutinas de software en un chip o circuito integrado.
    primer programa al encender una PC\n"""
            comoFunciona= """Como funciona: Inicializa, configura y testea todo el hardware del sistema y carga el gestor de arranque
    Ante problemas, no permite el arranque del SO
    chip del tipo CMOS ubicado en la Mother, se utiliza una bateria para alimentarlo
    si pierde energia, todos los datos en el CMOS se perderán\n"""
            actualizar="""Se actualiza la bios? Si, hacer funcionar nuestra placa con un procesador nuevo, o solucionar compatibilidad con ciertos tipos de hardware. Cualquier paso erroneo podria llevar al final de su vida activa. Tecnologia que esta siendo reemplazada por UEFI, (Unified Extensible Firmware Interface)\n"""
            tipos="Tipos de BIOS: Se diferencian por el metodo utilizado para grabar informacion en el chip. Tres de ellas suelen ser las mas comunes: ROM, EPROM, Flash BIOS.\n"
            
            print(concepto,comoFunciona,actualizar,tipos)
        def ROM(self):
            Nombre="Read Only Memory.\n"
            Funcion="Funcion: Memoria no volatil, la informacion es susceptible de alteracion y cambios, esto garantiza la disponibilidad.\n"
            print(Nombre,Funcion)
        def PROM(self):
                nombre="Nombre: Programmable read only memory.\n"
                Desarrollo="""Desarrollo: Desarrollo militar de mediados de los 50. para grabar datos con sobrecarga de tencion, diodos intactos '1'\n"""
                print(nombre,Desarrollo)
        def EPROM(self):
            nombre="Erasable Programmable Read-Only Memory.\n"
            desarrollo="Son regrabables, asi que la informacion es modificable y remobible. Luz ultravioleta para grabar. Se encuentran e 286 y 386\n"
            print(nombre,desarrollo)
        def FlashBIOS(self):
            Nombre="Memoria Flash\n"
            print(Nombre)
        def PNP(self):
            Nombre="Plug and Play.\n"
            Desarrollo="Reconoce automaticamente cualquier dispositivo conectado a la computadora y se le asigna los recursos necesarios\n"
            print(Nombre,Desarrollo)
        def clase(self):
            nombre="Random access memory\n"
            definicion="Memoria a coto plazo, almacena datos de acceso rapido, la capacidad es fundamental para el rendimiento del SO.\n"
            clasificacionSegunTam="DIMM (Dual inline memory module). SODIMM (Small outline dual inline memory module)\n"
            clasificacionSegunMod=" Mod SIMM, mod DIMM\n"
            ModDIMM="DDR-SDRAM (DRAM sincrona de velocidad de datos dobles). SDRAM (RAM dinamica sincronica) que esta disponible en dos config, con paridad y sin paridad\n"
            DDRSDRAM="""DDR:significa Double Data Rate. SDR (Single data rate) 
    DDR-SDRAM: la tecnologia de memoria mas avanzada disponible actualmente.
    Bus De Reloj: cada cuanto tiempo envian los datos\n"""
            BusesYconexiones="""Bus:Canal de comunicacion
    seriales: Va transmitiendo un numero atras de otr a travez de un solo bus
    paralelo: Utiliza varias pistas, que envian varios datos a la vez, tambien en serie\n"""
            BusProcesadorMemoria="Controlado por el controlador de memoria integrado en el procesador, es el mas escencial y el mas complejo dado que con cada nuevo tipo de memoria ram, se requiere rediseñar toda la estructura del controlador.\n"
            
            print(nombre,definicion,clasificacionSegunTam,clasificacionSegunMod,ModDIMM,DDRSDRAM,BusesYconexiones,BusProcesadorMemoria)



clase=memoria()
clase.logicaProposicional()