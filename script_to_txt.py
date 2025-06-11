import os
import re
import unicodedata
from pathlib import Path
from pdfminer.high_level import extract_text

def clean_text(text: str) -> str:
    """
    - Normalise les caractères Unicode (NFKD)
    - Supprime les caractères non-ASCII
    - Remplace les espaces multiples par un seul espace
    - Trim des espaces en début/fin de ligne
    """
    # Décompose les caractères accentués
    text = unicodedata.normalize('NFKD', text)
    # Supprime les diacritiques
    text = ''.join(ch for ch in text if not unicodedata.combining(ch))
    # Supprime tout caractère non-ASCII
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    # Remplace les retours à la ligne par un espace
    text = text.replace('\r', ' ').replace('\n', ' ')
    # Collapse multiples espaces en un seul
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def pdfs_to_txt(input_root: Path, output_root: Path):
    for dirpath, dirnames, filenames in os.walk(input_root):
        # Pour chaque PDF trouvé
        for fname in filenames:
            if not fname.lower().endswith('.pdf'):
                continue

            src_pdf = Path(dirpath) / fname
            # Calcul du chemin relatif (ex. "Droit Civil/Naissance/…")
            rel_dir = Path(dirpath).relative_to(input_root)

            # Création du dossier correspondant sous output_root
            dest_dir = output_root / rel_dir
            dest_dir.mkdir(parents=True, exist_ok=True)

            # Nom du fichier de sortie
            dest_txt = dest_dir / (src_pdf.stem + '.txt')

            try:
                # Extraction du texte
                raw_text = extract_text(str(src_pdf))
            except Exception as e:
                print(f"⚠️ Échec extraction {src_pdf}: {e}")
                continue

            # Nettoyage
            cleaned = clean_text(raw_text)

            # Écriture
            with open(dest_txt, 'w', encoding='utf-8') as f:
                f.write(cleaned)

            print(f"✅ Converti : {src_pdf} → {dest_txt}")

if __name__ == "__main__":
    # Chemins à adapter si besoin
    INPUT_DIR  = Path("Collecte Pdf")
    OUTPUT_DIR = Path("Collecte Txt")

    pdfs_to_txt(INPUT_DIR, OUTPUT_DIR)
    print("🔔 Conversion terminée.")
