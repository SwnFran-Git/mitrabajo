from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from Exceptions.Exepciones import FormatoError


def texto_obligatorio(texto, campo: str) -> str:
    if texto is None or not str(texto).strip():
        raise FormatoError(f"{campo} es obligatorio.")
    return str(texto).strip()


def a_entero(texto, campo: str) -> int:
    try:
        return int(str(texto).strip())
    except (ValueError, TypeError):
        raise FormatoError(f"{campo} debe ser un número entero.") from None


def a_decimal(texto, campo: str) -> float:
    try:
        valor = Decimal(str(texto).strip().replace(",", "."))
        if not valor.is_finite():
            raise InvalidOperation
        return float(valor.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
    except (InvalidOperation, ValueError, TypeError, OverflowError):
        raise FormatoError(f"{campo} debe ser un número válido.") from None