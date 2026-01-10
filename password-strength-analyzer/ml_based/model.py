import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

datos = pd.read_csv("passwords_dataset.csv")
datos.head()

datos["Strength"] = datos["Strength"].map({
"weak": 0,
"strong": 1
})

datos = datos.dropna(subset=["Strength"])

for col in datos.select_dtypes(include='bool').columns:
    datos[col] = datos[col].astype(int)

datos.isna().sum()



x_ent, y_ent, x_test, y_test = train_test_split(datos.drop(["Password"], axis=1), datos["Strength"])


modelo = LogisticRegression()
modelo.fit(x_ent, x_test)

password = input("Ingrese su contraseña: ")

features = [
    len(password),
    any(c.isupper() for c in password),
    any(c.islower() for c in password),
    any(c.isdigit() for c in password),
    any(not c.isalnum() for c in password)
]

X_usuario = np.array(features).reshape(1, -1)

prediccion = modelo.predict(X_usuario)

if prediccion[0] == 0:
    print("Su contraseña es poco segura")
else:
    print("Su contraseña es segura")