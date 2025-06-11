import os
import re
from pathlib import Path

def split_into_chunks(text: str,
                      max_words: int = 1000,
                      overlap: int = 200) -> list[str]:
    """
    Découpe `text` en chunks d'environ `max_words` mots,
    avec un chevauchement de `overlap` mots.
    """
    # On découpe en "phrases" basiques via le point suivi d'espace
    sentences = re.split(r'(?<=\.)\s+', text)
    words = []
    for sent in sentences:
        words.extend(sent.split())

    chunks = []
    start = 0
    total = len(words)
    while start < total:
        end = min(start + max_words, total)
        chunk_words = words[start:end]
        chunks.append(" ".join(chunk_words))
        # on recule de `overlap` mots pour le prochain chunk
        start = end - overlap
        if start < 0:
            start = 0
    return chunks

def chunk_txt_files(input_root: Path,
                    output_root: Path,
                    max_words: int = 1000,
                    overlap: int = 200):
    """
    Parcourt récursivement `input_root`, lit chaque .txt,
    le découpe en chunks, et écrit les chunks dans la même
    structure sous `output_root`.
    """
    for txt_path in input_root.rglob("*.txt"):
        rel = txt_path.relative_to(input_root)
        dest_dir = output_root / rel.parent
        dest_dir.mkdir(parents=True, exist_ok=True)

        text = txt_path.read_text(encoding="utf-8")
        chunks = split_into_chunks(text, max_words, overlap)

        base = txt_path.stem
        for i, chunk in enumerate(chunks, start=1):
            chunk_name = f"{base}_chunk{i:02d}.txt"
            (dest_dir / chunk_name).write_text(chunk, encoding="utf-8")
            print(f"→ {rel.parent / chunk_name}")

if __name__ == "__main__":
    INPUT_DIR  = Path("Collecte Txt")    # vos .txt nettoyés
    OUTPUT_DIR = Path("Collecte Chunks") # là où seront les chunks
    chunk_txt_files(INPUT_DIR, OUTPUT_DIR,
                    max_words=1000,
                    overlap=200)
    print("✅ Découpage terminé.")
