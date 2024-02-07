# mod-isim2-changes_xlsx_reader

Ansible module designed to read specific formatted xlsx files containing changes to create in SNOW.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install mod-isim2-changes_xlsx_reader dependencies.

```bash
/var/lib/awx/venv/ansible/bin/pip install --user --no-index jdcal-1.4.1.tar.gz
/var/lib/awx/venv/ansible/bin/pip install --user --no-index et_xmlfile-1.0.1.tar.gz
/var/lib/awx/venv/ansible/bin/pip install --user --no-index openpyxl-2.6.4.tar.gz
```

Then copy module file to yout library project subfolder or in general Ansible module library.
```bash
cp /tmp/changes_xlsx_reader.py /usr/share/ansible/plugins/modules/
```

## Usage

```yaml
  - name: Read changes to create file
    hosts: localhost
    connection: local
    gather_facts: no
    tasks:
      - name: Read file
        register: result
        changes_xlsx_reader:
          src: "changes.xlsx"
          
      - debug: var=result
```
