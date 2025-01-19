# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

import os
import zipfile
import pandas as pd

def pregunta_01():
    
    ruta = "files/input.zip"
    with zipfile.ZipFile(ruta, 'r') as zip_ref:
        zip_ref.extractall("input")

    ## Crear el output en files: 
    output_dir = os.path.join("files","output")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
        
    phrases_test = []
    targets_test = []
    phrases_train = []
    targets_train = []    
    
    test_dir = os.path.join("input","input","test")
    train_dir = os.path.join("input","input","train")
    sentimientos_nombres = ["negative","neutral","positive"]
    
    
    for sentimiento in sentimientos_nombres:
        for file in os.listdir(os.path.join(test_dir,sentimiento)):
            with open(os.path.join(test_dir,sentimiento,file), 'r') as f:
                phrases_test.append(f.read())
                targets_test.append(sentimiento)
        for file in os.listdir(os.path.join(train_dir,sentimiento)):
            with open(os.path.join(train_dir,sentimiento,file), 'r') as f:
                phrases_train.append(f.read())
                targets_train.append(sentimiento)
            
    
    test_data = pd.DataFrame({'phrase': phrases_test, 'target': targets_test})
    train_data = pd.DataFrame({'phrase': phrases_train, 'target': targets_train})
    
    test_data.to_csv(os.path.join(output_dir,"test_dataset.csv"), index=False)
    train_data.to_csv(os.path.join(output_dir,"train_dataset.csv"), index=False)

    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """

if __name__ == '__main__':
    pregunta_01()

