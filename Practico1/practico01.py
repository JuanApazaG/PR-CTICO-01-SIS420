import numpy as np
import pandas as pd

# Establecer una semilla para reproducibilidad
np.random.seed(0)

# Generar estaturas entre 1.50 y 2.05 metros
alturas = np.random.uniform(1.50, 2.05, 100)

# Generar pesos correlacionados con la estatura, entre 50 y 100 kilos
pesos = alturas * np.random.uniform(20, 30) + np.random.uniform(10, 15)

# Crear un DataFrame con los datos
data = pd.DataFrame({
    'Altura': alturas,
    'Peso': pesos
})

# Guardar el DataFrame en un archivo CSV (opcional)
data.to_csv('peso_estatura.csv', index=False)
