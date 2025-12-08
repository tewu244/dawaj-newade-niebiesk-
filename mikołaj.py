# Zapisz ten kod do pliku app.py w Colab
# W Colab musimy użyć magicznej komendy, aby zapisać kod do pliku
%%writefile app.py

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

    # --- Rysowanie: Głowa ---
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
    
    # Kolorowa część czapki (Polygon) - używa zmiennego koloru
    punkty_czapki = np.array([(1.5, 6.5), (1.5, 5), (-1.5, 5)])
    czapka_czerwona = patches.Polygon(punkty_czapki, closed=True, 
                                      facecolor=kolor_stroju, edgecolor=KOLOR_CZARNY, linewidth=1.5)
    ax.add_patch(czapka_czerwona)
    
    # Pompon (koło)
    pompon = patches.Circle((1.5, 6.5), radius=0.5, facecolor=KOLOR_BIALY_FUTRO, 
                            edgecolor=KOLOR_CZARNY, linewidth=1)
    ax.add_patch(pompon)
    
    # Broda (Elipsa)
    broda = patches.Ellipse((0, 1.5), width=4, height=3, facecolor=KOLOR_BIALY_FUTRO, 
                            edgecolor=KOLOR_CZARNY, linewidth=1.5, zorder=1)
    ax.add_patch(broda)
    
    # --- Rysowanie: Ciało i Pas ---
    # Ciało - używa zmiennego koloru
    cialo = patches.Rectangle((-3, -6), 6, 8, facecolor=kolor_stroju, 
                              edgecolor=KOLOR_CZARNY, linewidth=1.5, zorder=0)
    ax.add_patch(cialo)

    # Futro na dole
    futro_dol = patches.Rectangle((-3.5, -6.5), 7, 0.5, facecolor=KOLOR_BIALY_FUTRO, 
                                 edgecolor=KOLOR_CZARNY, linewidth=1.5, zorder=2)
    ax.add_patch(futro_dol)

    # Pas
    pas_czarny = patches.Rectangle((-3.5, -0.5), 7, 1, facecolor=KOLOR_CZARNY, zorder=2)
    ax.add_patch(pas_czarny)
    
    # Klamra
    klamra = patches.Rectangle((-1, -0.25), 2, 0.5, facecolor=KOLOR_KLAMRA, 
                              edgecolor=KOLOR_CZARNY, linewidth=1, zorder=3)
    ax.add_patch(klamra)
    
    # --- Finalizacja ---
    plt.title("Wesoły Mikołaj", fontsize=16)
    
    return fig

# --- Główna sekcja Streamlit ---

st.title("🎅 Interaktywny Generator Mikołaja")

st.sidebar.header("Opcje personalizacji")

# Widget do wyboru koloru w panelu bocznym
kolor_wybrany = st.sidebar.color_picker(
    'Wybierz kolor stroju Mikołaja:', 
    value='#D93025' # Domyślny kolor czerwony
)

# Generowanie i wyświetlanie figury
figura_mikolaja = narysuj_mikolaja(kolor_wybrany)

# Użycie funkcji Streamlit do wyświetlenia figury
st.pyplot(figura_mikolaja)
