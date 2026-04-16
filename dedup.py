from difflib import SequenceMatcher

def deduplicar(casos):
    unique = []
    for c in casos:
        is_dup = False
        for u in unique:
            ratio = SequenceMatcher(None, c["titular"].lower(), u["titular"].lower()).ratio()
            # Criterio de deduplicación profesional: >75% similitud textual
            if ratio > 0.75:
                is_dup = True
                if c["fuente"] not in u.get("fuentes_cruzadas", []):
                    u.setdefault("fuentes_cruzadas", [u["fuente"]]).append(c["fuente"])
                break
        if not is_dup:
            c["fuentes_cruzadas"] = [c["fuente"]]
            unique.append(c)
    return unique
