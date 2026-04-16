import re

GEOGRAFIA_CR = {
    "San José": ["desamparados", "alajuelita", "pavas", "goicoechea", "tibas", "moravia", "escazu", "santa ana"],
    "Alajuela": ["alajuela", "san carlos", "upala", "los chiles", "palmares", "grecia", "ramon"],
    "Cartago": ["cartago", "paraiso", "la union", "turrialba", "alvarado"],
    "Heredia": ["heredia", "barva", "santo domingo", "santa barbara", "san rafael", "belen", "flores", "pablo"],
    "Guanacaste": ["liberia", "nicoya", "santa cruz", "bagaces", "cañas", "tilaran", "nandayure"],
    "Puntarenas": ["puntarenas", "esparza", "buenos aires", "montes de oro", "osa", "quepos", "golfito", "corredores"],
    "Limón": ["limón", "limon", "pococí", "pococi", "siquirres", "talamanca", "matina", "guácimo", "guacimo"]
}

MODALIDADES = {
    "sicariato": ["sicariato", "ajuste", "ajusticiamiento", "moto", "acribillado"],
    "balacera": ["balacera", "tiroteo", "racha de disparos", "fuego cruzado"],
    "arma_blanca": ["puñalada", "arma blanca", "cuchillo", "machete"],
    "hallazgo": ["cuerpo", "cadáver", "cadáver hallado", "bolsas", "fosa"]
}

def analizar_caso(titular):
    titular_low = titular.lower()
    provincia_hallada = "Desconocida"
    canton_hallado = "No especificado"
    modalidad_hallada = "Desconocida"

    # Buscar Provincia y Cantón
    for prov, cantones in GEOGRAFIA_CR.items():
        if prov.lower() in titular_low:
            provincia_hallada = prov
        for canton in cantones:
            if canton in titular_low:
                provincia_hallada = prov
                canton_hallado = canton.capitalize()
                break
    
    # Buscar Modalidad
    for mod, kws in MODALIDADES.items():
        if any(kw in titular_low for kw in kws):
            modalidad_hallada = mod
            break

    return {
        "provincia": provincia_hallada,
        "canton": canton_hallado,
        "modalidad": modalidad_hallada
    }
