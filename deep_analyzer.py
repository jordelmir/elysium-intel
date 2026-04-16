import re

# Diccionario Maestro de Inteligencia Criminal CR
ESTRUCTURA_GEO = {
    "San José": {
        "San José": ["Pavas", "Hatillo", "San Sebastián", "Zapote", "Uruca"],
        "Desamparados": ["San Miguel", "San Rafael", "Frailes", "Patarrá"],
        "Alajuelita": ["Concepción", "San Josecito", "San Felipe"],
        "Goicoechea": ["Guadalupe", "Ipís", "Purral", "Calle Blancos"],
    },
    "Limón": {
        "Limón": ["Cieneguita", "Limón 2000", "Envaco", "Pueblo Nuevo"],
        "Pococí": ["Guápiles", "Cariari", "Jiménez", "Rita"],
        "Matina": ["Batán", "Carrandi"],
        "Siquirres": ["Siquirres", "Pacuarito", "Germania"],
    },
    "Puntarenas": {
        "Puntarenas": ["Chacarita", "El Roble", "Barranca", "Fray Casiano"],
        "Corredores": ["Paso Canoas", "La Cuesta", "Ciudad Neily"],
        "Quepos": ["Savegre", "Naranjito"],
    }
}

MOVILES = {
    "Narcotráfico/Sicariato": ["droga", "estupefacientes", "búnker", "ajuste de cuentas", "venganza", "moto", "acribillado", "banda"],
    "Robo/Asalto": ["asalto", "robar", "pertenencias", "vivienda", "sustraer"],
    "Riña/Discusión": ["discusión", "pelea", "riña", "alcohol", "bar"],
    "Violencia Doméstica": ["pareja", "ex-pareja", "femicidio", "celos", "casa"],
    "Desconocido/En Investigación": ["investigación", "oij", "móvil", "desconocido"]
}

def dissect_content(text):
    text = text.lower()
    result = {
        "provincia": "No detectada",
        "canton": "No detectado",
        "distrito": "No detectado",
        "motivo": "No determinado",
        "armas": "Desconocida"
    }

    # Extracción Geo-Forense
    for prov, cantones in ESTRUCTURA_GEO.items():
        if prov.lower() in text:
            result["provincia"] = prov
        for canton, distritos in cantones.items():
            if canton.lower() in text:
                result["provincia"] = prov
                result["canton"] = canton
                for distrito in distritos:
                    if distrito.lower() in text:
                        result["distrito"] = distrito
                        break
    
    # Extracción de Móvil (El "Por qué")
    for mov, kws in MOVILES.items():
        if any(kw in text for kw in kws):
            result["motivo"] = mov
            break
            
    # Detección de Armas
    if "fuego" in text or "disparos" in text or "bala" in text:
        result["armas"] = "Arma de Fuego"
    elif "blanca" in text or "puñal" in text or "cuchillo" in text:
        result["armas"] = "Arma Blanca"
        
    return result
