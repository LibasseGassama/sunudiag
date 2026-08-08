"""
SunuDiag - API REST servant le modele paludisme
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
import joblib
import pandas as pd

app = FastAPI(
    title="SunuDiag API",
    description="Pre-diagnostic du paludisme (modele DataSANTE-221).",
    version="2.0",
)

# CORS (optionnel mais utile)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Charger le modèle
modele = joblib.load("models/model.pkl")
FEATURES = ["age", "glycemie", "hemoglobine", "fievre", "saison"]

class Patient(BaseModel):
    age: int = Field(ge=0, le=120)
    glycemie: float = Field(ge=2.0, le=25.0)
    hemoglobine: float = Field(ge=4.0, le=20.0)
    fievre: float = Field(ge=34.0, le=43.0)
    saison: int = Field(ge=0, le=1)

@app.get("/health")
def health():
    return {"statut": "ok", "modele": "RandomForest DataSANTE-221"}

@app.post("/predict")
def predict(patient: Patient):
    donnees = pd.DataFrame([patient.model_dump()])[FEATURES]
    proba = float(modele.predict_proba(donnees)[0, 1])
    return {
        "probabilite_paludisme": round(proba, 3),
        "pre_diagnostic": "A ORIENTER" if proba >= 0.5 else "risque faible",
        "avertissement": "Ne remplace pas un avis medical.",
    }

# Servir le frontend - TOUJOURS EN DERNIER !
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")