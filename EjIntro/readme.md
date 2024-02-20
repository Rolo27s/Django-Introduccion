# API para cálculos matemáticos y operaciones con cadenas

Esta API proporciona varios métodos para realizar cálculos matemáticos y operaciones con cadenas a través de consultas GET en Django.

## Métodos disponibles

### Cálculo de área de figuras geométricas

- **Triángulo:** `/areatriangulo/?base=4&altura=7`
- **Rectángulo:** `/arearectangulo/?lado1=3&lado2=5`
- **Círculo:** `/areacirculo/?radio=2.24`

### Cálculo de longitud de figuras geométricas

- **Triángulo:** `/longitudtriangulo/?lado1=2&lado2=3&lado3=4`
- **Rectángulo:** `/longitudrectangulo/?lado1=3&lado2=5`
- **Círculo:** `/longitudcirculo/?radio=31.24`

### Operaciones con cadenas

- **Contar vocales:** `/cantidadvocales?palabra=Hola mundo`
- **Encontrar el mínimo:** `/minimo/?numeros=1,2,3,4,5,6,7,8`
- **Determinar signo de un número:** `/posnegcero/?numero=4`

## Ejemplo de uso

Para calcular el área de un rectángulo con lados de longitud 3 y 5, se realiza una solicitud GET a `/arearectangulo/?lado1=3&lado2=5`.

El resultado será devuelto como una respuesta HTTP con el valor del área.

## Notas

- Para cada método, se deben proporcionar los parámetros necesarios en la consulta GET.
- Si no se proporcionan los parámetros adecuados, se devolverá un mensaje de error correspondiente.
- Los parámetros deben estar en el formato correcto (por ejemplo, números para cálculos matemáticos).
