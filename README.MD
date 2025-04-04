
# Ejercicio: Modelado de Ejércitos

## Descripción
Este proyecto modela ejércitos, civilizaciones y batallas utilizando Python, implementando reglas y dinámicas entre distintos tipos de unidades y civilizaciones.

## Estructura del Proyecto
El proyecto se organiza en las siguientes clases:
- **Army**: Representa un ejército.
- **Battle**: Simula una batalla entre ejércitos.
- **Civilization**: Define las civilizaciones disponibles.
- **Unit**: Clase base para las unidades:
  - **Pikeman** (Piquero)
  - **Archer** (Arquero)
  - **Knight** (Caballero)

### Archivos
- **`tst_army.py`**: Contiene pruebas unitarias para verificar el correcto funcionamiento.

## Funcionalidades


### Batallas
- Los ejércitos se enfrentan comparando su **fuerza total**.
- **Ganador**:
  - Obtiene 100 monedas de oro.
- **Perdedor**:
  - Pierde sus dos unidades más fuertes.
- **Empate**:
  - Ambos ejércitos pierden unidades.

## Casos Especiales
1. **Nueva unidad: Mago**
   A partir del siguiente modelado, si quisieramos obtener una nueva unidad, como en este caso un Mago, simplemente tenemos que agregarla con sus metodos. Esto se debe a la herencia y el polimorfismo, principios básicos del OOP.

2. **Entrenamiento + Transformación**:
   En base a como estuve modelando, en caso de que exista un entrenamiento + transformacion, la nueva unidad obtendría la fuerza que tenía la misma antes de transformarse.

3. **Restricciones**:
   - Con el uso de manejos de errores, por ejemplo en caso de que un ejercito ya no tenga unidades, no podría atacar a nadie, por lo tanto se arroja un exception.



