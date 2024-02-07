# [AE380] Création de change en masse

Le cas d'usage permet de créer de multiples changes enfant sur SNOW.

## Prérequis et dépendances

Le module custom changes_xlsx_reader (dans le repo mod-isim2-changes_xlsx_reader) doit être présent dans le venv/EE.
Le fichier d'entrée doit être présent dans le Nexus.

## Usage

Variables d'entrées:
- snow_change_creation_xlsx_file_name: nom du fichier xls source
- use_case_environment: (DEV|PRD) environnement d'execution du cas d'usage.
- use_case_report_email: liste de mails (comma separated) qui recevront le rapport d'execution.
