import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Konfiguracja strony
st.set_page_config(
    page_title="Interaktywny Mikołaj",
    layout="centered"
)

# --- Stałe kolory ---
KOLOR_CIALO = '#FDD9C2'
KOLOR_BIALY_FUTRO = '#F0F0F0'
KOLOR_CZARNY = '#1A1A1A'
KOLOR_KLAMRA = '#FFD700' # Złoty

# Funkcja rysująca Mikołaja
def narysuj_mikolaja(kolor_stroju):
    """Generuje figurę Matplotlib Mikołaja z możliwością zmiany koloru stroju."""
    
    # Inicjalizacja figury
    fig, ax = plt.subplots(figsize=(6, 8))

    # Ustawienia osi
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal', adjustable='box') 
    ax.axis('off') 

    # --- Rysowanie: Głowa (koło) ---
    glowa = patches.Circle((0, 3), radius=2, facecolor=KOLOR_CIALO, 
                           edgecolor=KOLOR_CZARNY, linewidth=1.5)
    ax.add_patch(glowa)

    # Oczy i Nos
    oko_lewe = patches.Circle((-0.7, 3.5), radius=0.2, facecolor=KOLOR_CZARNY)
    oko_prawe = patches.Circle((0.7, 3.5), radius=0.2, facecolor=KOLOR_CZARNY)
    nos = patches.Circle((0, 3), radius=0.3, facecolor=KOLOR_CIALO, 
                         edgecolor=KOLOR_CZARNY, linewidth=0.5)
    ax.add_patch(oko_lewe)
    ax.add_patch(oko_prawe)
    ax.add_patch(nos)

    # --- Rysowanie: Czapka i Broda ---
    # Opaska futrzana (prostokąt)
    opaska_futrzana = patches.Rectangle((-2.5, 4.5), 5, 0.5, facecolor=KOLOR_BIALY_FUTRO, 
                                        edgecolor=KOLOR_CZARNY, linewidth=1.5)
    ax.add_patch(opaska_futrzana)
    
    # Czerwona/Kolorowa część (Polygon) - używa zmiennego koloru
    punkty_czapki = np.array([(1.5, 6.5), (1.5, 5), (-1.5, 5)])
    czapka_czerwona = patches.Polygon(punkty_czapki, closed=True, 
                                      facecolor=kolor_stroju, edgecolor=KOLOR_CZARNY, linewidth=1.5)
    ax.add_patch(czapka_czerwona)
    
    # Pompon (koło)
    pompon = patches.Circle((1.5, 6.5), radius=0.5, facecolor=KOLOR_BI
