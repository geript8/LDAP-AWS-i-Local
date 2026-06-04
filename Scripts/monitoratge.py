import subprocess

serveis = ["slapd", "smbd"]

for servei in serveis:
    resultat = subprocess.run(
        ["systemctl", "is-active", servei],
        capture_output=True,
        text=True
    )

    print(f"{servei}: {resultat.stdout.strip()}")
