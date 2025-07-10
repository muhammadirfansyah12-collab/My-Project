from sklearn.naive_bayes import CategoricalNB
import pandas as pd

def train_model(file_path):
    df = pd.read_csv(file_path)
    X = df[['nilai_kat', 'kehadiran_kat', 'partisipasi_kat']]
    y = df['label']
    model = CategoricalNB()
    model.fit(X, y)
    return model

def predict(model, input_data):
    return model.predict([input_data])[0]
