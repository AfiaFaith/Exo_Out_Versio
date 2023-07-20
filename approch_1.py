import os
import shutil
import subprocess

def create_project_structure():
    # Créer les dossiers de l'arborescence
    os.makedirs("data/cleaned")
    os.makedirs("data/raw")
    os.makedirs("docs")
    os.makedirs("models")
    os.makedirs("notebooks")
    os.makedirs("reports")
    os.makedirs("src")

    # Créer les fichiers README.md, LICENSE, Makefile, requirements.txt
    open("README.md", "w").close()
    open("LICENSE", "w").close()
    open("Makefile", "w").close()
    open("requirements.txt", "w").close()

def edit_notebook_and_utils():
    # Éditer le fichier main_notebook.ipynb
    with open("notebooks/main_notebook.ipynb", "w") as notebook_file:
        notebook_file.write("Jupyter notebook content...")

    # Éditer le fichier src/utils.py
    with open("src/utils.py", "w") as utils_file:
        utils_file.write("# Your utility functions...")

def initialize_git_repo():
    # Initialiser le dépôt Git
    subprocess.run(["git", "init"])

    # Ajouter tous les fichiers de l'arborescence au dépôt
    subprocess.run(["git", "add", "."])

    # Effectuer un commit avec un message
    subprocess.run(["git", "commit", "-m", "Initial commit"])

    # Créer et changer à la branche "approch_1"
    subprocess.run(["git", "checkout", "-b", "approch_1"])

    # Remplacer "REMOTE_URL" par l'URL de votre dépôt Git distant
    remote_url = "https://github.com/AfiaFaith/Exo_Out_Versio.git"
    subprocess.run(["git", "remote", "add", "origin", remote_url])

    # Pousser les changements vers le dépôt distant (branche "approch_1")
    subprocess.run(["git", "push", "-u", "origin", "approch_1"])

def main():
    create_project_structure()
    edit_notebook_and_utils()
    initialize_git_repo()

if __name__ == "__main__":
    main()
