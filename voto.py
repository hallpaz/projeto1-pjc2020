
OBRIGATORIO = 0
FACULTATIVO = 1
PROIBIDO = 2

def situacao_voto(idade):
    if idade in range(18, 70):
        return OBRIGATORIO
    elif idade >= 16:
        return FACULTATIVO
    return PROIBIDO