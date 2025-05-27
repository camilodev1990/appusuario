from django.core.exceptions import ValidationError
import re


# Validadores personalizados


def validar_password_segura(value):
    if len(value) < 8:
        raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
    if not re.search(r'[A-Z]', value):
        raise ValidationError('La contraseña debe contener al menos una letra mayúscula.')
    if not re.search(r'\d', value):
        raise ValidationError('La contraseña debe contener al menos un número.')
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};\'\\:"|<,./<>?]', value):
        raise ValidationError('La contraseña debe contener al menos un carácter especial.')
    
    consecutivos = ['123', '234', '345', '456', '567', '678', '789', '012', '111', '222', '333', '444', '555', '666', '777', '888', '999']
    for secuencia in consecutivos:
        if secuencia in value:
            raise ValidationError('La contraseña no debe contener secuencias numéricas consecutivas como 123 o 111.')

