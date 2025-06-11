import os
from pathlib import Path

def chunk_large_file(txt_path: Path,
                     dest_dir: Path,
                     max_words: int = 30,
                     overlap: int = 200):
    """
    Traite un fichier .txt volumineux sans tout charger en mémoire.
    Écrit les chunks dans dest_dir.
    """
    dest_dir.mkdir(parents=True, exist_ok=True)
    base = txt_path.stem
    buffer = []
    chunk_id = 1

    with txt_path.open(encoding="utf-8") as f:
        for line in f:
            words = line.strip().split()
            buffer.extend(words)

            while len(buffer) >= max_words:
                chunk_words = buffer[:max_words]
                chunk_text = " ".join(chunk_words)
                chunk_name = f"{base}_chunk{chunk_id:02d}.txt"
                (dest_dir / chunk_name).write_text(chunk_text, encoding="utf-8")
                print(f"→ {chunk_name}")

                # prépare le buffer suivant avec chevauchement
                buffer = buffer[max_words - overlap:]
                chunk_id += 1

        # écrit le dernier chunk s’il reste des mots
        if buffer:
            chunk_name = f"{base}_chunk{chunk_id:02d}.txt"
            (dest_dir / chunk_name).write_text(" ".join(buffer), encoding="utf-8")
            print(f"→ {chunk_name}")

def chunk_all_files_light(input_root: Path,
                          output_root: Path,
                          max_words: int = 300,
                          overlap: int = 200):
    for txt_path in input_root.rglob("*.txt"):
        rel = txt_path.relative_to(input_root)
        dest_dir = output_root / rel.parent
        chunk_large_file(txt_path, dest_dir, max_words, overlap)

if __name__ == "__main__":
    INPUT_DIR = Path("Collecte Txt")
    OUTPUT_DIR = Path("Collecte Chunks")
    chunk_all_files_light(INPUT_DIR, OUTPUT_DIR,
                          max_words=30,
                          overlap=200)
    print("✅ Découpage terminé avec gestion mémoire légère.")
