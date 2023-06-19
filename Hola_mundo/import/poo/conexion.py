import mysql.connector as sql

class Conexion():
    
    __conn=None
    __msgErr=None
    
    def getMsgError(this):
        return this.__msgErr
    
        
    def __conectar(this,host,user,pwd,db):
        
        try:
           
            this.__conn=sql.connect(
               host=host,
               user=user,
               passwd=pwd,
               db=db
            )
           
        except Exception as e:
            this.__msgErr=e
        
            
    def __init__(this,usuario,pwd,db):
    
            host="127.0.0.1"    
            this.__msgErr=None
            this.__conn=None
            this.__conectar(host,usuario,pwd,db)
    
    def consulta(this,id):
    
        try:
            if this.__conn !=None:
                
                cur=this.__conn.cursor()
                #cur.execute("select * from vista") # Llamada a vista
                cur.callproc("proc_alumno",(int(id),))
        
                for fila in cur.fetchall():
                    print(fila)
            else:
                raise Exception("Error de conexión")
            
        except  Exception as e:
            this.__msgErr=e
            
    def __cerrarCon(this):
        
        try:
            if this.__conn!=None and this.__conn.is_connected:
                this.__conn.close()
        except Exception as e:
            this.__msgErr=e

    def __del__(this):
        
        this.__cerrarCon()
        this.__conn=None
            