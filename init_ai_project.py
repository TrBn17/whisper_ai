import os

def create_ai_project(base_dir: str):
    structure = [
        "docs",
        "data/raw",
        "data/processed",
        "models",
        "notebooks",
        "scripts",
        "tests",
        "env",
        "docker",
        "src/config",
        "src/data",
        "src/datasets",
        "src/models",
        "src/training",
        "src/inference",
        "src/evaluation",
        "src/utils",
    ]
    
    for path in structure:
        os.makedirs(os.path.join(base_dir, path), exist_ok=True)
    
    with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"# AI Project\n\nProject structure initialized.\n")
    
    with open(os.path.join(base_dir, "requirements.txt"), "w", encoding="utf-8") as f:
        f.write("# Python dependencies here\n")
    
    print(f"✅ Project structure created under {base_dir}")

if __name__ == "__main__":
    base_dir = r"G:\test_whisper\whisper_ai"
    create_ai_project(base_dir)
