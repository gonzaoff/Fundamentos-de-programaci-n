class clase2():
    def Arc(self):
        arquitecturaHardvard = """Resuelve el cuello de botella de Von Neumann con ciclos de reloj,
        lo que conlleva un mayor costo"""
    def logicaProposicional():
        Definicion="""Definicion: Establece proposiciones logicas que poseen un valor Verdadero o Falso (true or false). Nos devuelve un razonamiento logico a un razonamiento binario"""
        conectoresLogicos = """Conectores Logicos
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

    def BIOS():
        concepto="""Concepto: Rutinas de software en un chip o circuito integrado.
primer programa al encender una PC"""
        comoFunciona= """Como funciona: Inicializa, configura y testea todo el hardware del sistema y carga el gestor de arranque
Ante problemas, no permite el arranque del SO
chip del tipo CMOS ubicado en la Mother, se utiliza una bateria para alimentarlo
si pierde energia, todos los datos en el CMOS se perderán"""
        actualizar="""Se actualiza la bios? Si, hacer funcionar nuestra placa con un procesador nuevo, o solucionar compatibilidad con ciertos tipos de hardware. Cualquier paso erroneo podria llevar al final de su vida activa. Tecnologia que esta siendo reemplazada por UEFI, (Unified Extensible Firmware Interface)"""
        tipos="Tipos de BIOS: Se diferencian por el metodo utilizado para grabar informacion en el chip. Tres de ellas suelen ser las mas comunes: ROM, EPROM, Flash BIOS."
        
        print(concepto,comoFunciona)
    def ROM():
        Nombre="Read Only Memory."
        Funcion="Funcion: Memoria no volatil, la informacion es susceptible de alteracion y cambios, esto garantiza la disponibilidad."
    def PROM():
            nombre="Nombre: Programmable read only memory."
            Desarrollo="""Desarrollo: Desarrollo militar de mediados de los 50. para grabar datos con sobrecarga de tencion, diodos intactos '1'"""
    def EPROM():
        nombre="Erasable Programmable Read-Only Memory."
        desarrollo="Son regrabables, asi que la informacion es modificable y remobible. Luz ultravioleta para grabar. Se encuentran e 286 y 386"
    
clase=clase2
clase.logicaProposicional()