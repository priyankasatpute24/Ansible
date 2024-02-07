#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: changes_xlsx_reader.py
short_description: Read an Excel xlsx file containg SNOW changes and register its content into an ansible list of dict
description:
    - Read a specified Excel file and register the Excel file content into an Ansible list of dictionaries. 
    
author: Tommy STYCZEN
options:
    src:
        description:
            - The name of the Excel spreadsheet
        required: true
        type: str
requirements:
    - openpyxl Python library must be installed on the Ansible host.
'''


RETURN = r'''
list:
    description: The modules returns a list of dictionaries containing the cell values.
    returned: on success
    type: list
    sample:
    
    "change_index_0": [
        {
            "assignement_group": "DSIT_ITO-ISIM2_TRANSVERSE",
            "business_service": "SIMM",
            "category": "Exploitation applicative",
            "category_element": "Paramétrage de produits",
            "change_reason": "Sécurité",
            "check_box": "CHG transverse",
            "chg_parent": "CHG0032137",
            "description": "La faille CVE-2021-20305 a été identifiée dans la bibliothèque de cryptographie Nettle, où des fonctions de vérification de signature Nettle (GOST DSA, EDDSA et ECDSA) peuvent donner des résultats incorrects.\nLa faille concerne également la bibliothèque GNU Transport Layer Security (GnuTLS), qui implémente des algorithmes et des protocoles cryptographiques tels que SSL, TLS et DTLS.\nVersions vulnérables : nettle, gnutls                                                                                                                                                                                                                                                                                                             \nVersions corrigées : nettle-2.7.1-9.el7_9.x86_64.rpm, nettle-3.4.1-4.el8_3.x86_64.rpm, gnutls-3.6.14-8.el8_3.x86_64.rpm\nCette RFC prend la relève de la RFC POGS C00073273\n\n\n\nla PTI : https://deposit.edf.fr/artifactory/transverse-gen/fr/edf/oi_serveurs_win_unix_netware_calibre/sysref_linux/7.x.x_patch_kernel_cve_2021_20305",
            "end_date": "20/05/2023 12:00:00",
            "impact": "1 - Interrompu",
            "requested_by": "Agnieszka JASTRZEBSKA (AJ0337AL)",
            "short_description": "[ISIM2] - [PRJ_TRANSVERSE] - Remédiation de la faille Nettle/Gnutls (CVE-2021-20305)",
            "start_date": "20/05/2023 08:00:00",
            "type": "Standard",
            "unavailability_expected_end": "20/05/2023 12:00:00",
            "unavailability_expected_start": "20/05/2023 08:00:00"
        }
    ],
    "change_index_1": [
        {
            "assignement_group": "DSIT_ITO-ISIM2_TRANSVERSE",
            "business_service": "SIAM",
            "category": "Exploitation applicative",
            "category_element": "Paramétrage de produits",
            "change_reason": "Sécurité",
            "check_box": "CHG transverse",
            "chg_parent": "CHG0032137",
            "description": "Description et objectifs du chantier : CVE-2022-22719, CVE-2022-22720, CVE-2022-22721, CVE-2022-23943 - Apache HTTP serveur est vulnérable à l'exécution de code à distance et au déni de service.\nLa souche Apache https 2.4.53 permet de corriger cette vulnérabilité. \n\nOS éligibles : RHEL7, CentOS7, RHEL8\n\nImpact annoncé : G3\n\nIndisponibilité annoncée : Coupure applicative de 3 heures durant l'installation manuel. Si plusieurs versions d'Apache présentes sur un serveur coupure applicative de 4 heures.\n\nChamps de critère PERS : C09\n\nDate de démarrage : 16/05/2022\n\nDate de fin estimée : N/A\n\nType action : Manuelle\n\nLa souche Apache httpd 2.4.53 permet de corriger cette vulnérabilité Deux procédures différentes sont disponibles  pour les os supportés EL7 et EL8:\nProcédure simplifiée qui ne demande plus le téléchargement de l'image ISO de la souche Apache 2.4.53:\nEL7 https://www.myelectricnetwork.fr/surl/4ff7a\nEL8 https://www.myelectricnetwork.fr/surl/4ff7g\nProcédure avec image ISO:\nEL7 https://www.myelectricnetwork.fr/surl/4ff78\nEL8 https://www.myelectricnetwork.fr/surl/4ff7j\nNon pas de reboot d'os  (reboot de l'instance Apache uniquement\n\nATTENTION:\nMERCI de garder le paramètre \"is-enabled\" pour que le service APACHE démarre automatiquement après le reboot.\n\n",
            "end_date": "30/10/2022 10:00:00",
            "impact": "3 - Aucun impact",
            "requested_by": "Izabela WOSZCZAK-MAJTYKA (IW05758L)",
            "short_description": "[ISIM2] - [PRJ_TRANSVERSE] - [Campagne Projets - Transverses : [Vulnérabilité Apache Mars 2022]",
            "start_date": "30/10/2022 08:00:00",
            "type": "Standard",
            "unavailability_expected_end": "30/10/2022 10:00:00",
            "unavailability_expected_start": "30/10/2022 08:00:00"
        }
    ]

    
    elements:
        - change_index_<n>: Reference to the index of the change found in the Excel workbook, where <n> refers to the row index number (starting from 0)
            - key: value    
'''


EXAMPLES = r'''
tasks:
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
'''

import openpyxl
from ansible.module_utils.basic import *



def read_xl_content(excel_file):
    
    retval = {}
    retval['data'] = {}
    changes_from_file = {}

    try:
        wb = openpyxl.load_workbook(excel_file, data_only=True)
        change_index = 0
        
        for row in wb.active.iter_rows(min_row=2, values_only=True):
            if(row[0] is None):
                break
                
            ansible_change_index_name = 'change_index_' + str(change_index).zfill(3)
            changes_from_file[ansible_change_index_name] = []
            
            temp_dict = {}
            # Change Info
            temp_dict['type']=row[0]
            temp_dict['category']=row[1]
            temp_dict['insertion_en_exploitation']=row[2]
            temp_dict['category_element']=row[3]
            temp_dict['element']=row[4]
            temp_dict['requested_by']=row[5]
            temp_dict['check_box']=row[6]
            temp_dict['business_service']=row[7]
            temp_dict['impact']=row[8]
            temp_dict['change_reason']=row[9]
            temp_dict['assignement_group']=row[10]
            temp_dict['chg_parent']=row[11]
            temp_dict['short_description']=row[12]
            temp_dict['description']=row[13]
            temp_dict['start_date']=row[14]
            temp_dict['end_date']=row[15]
            temp_dict['unavailability_expected_start']=row[16]
            temp_dict['unavailability_expected_end']=row[17]

            changes_from_file[ansible_change_index_name].append(temp_dict)
            change_index += 1
                        
    except Exception as err:
        return (1, err)

    retval['data'] = changes_from_file
    
    return (0, retval)



def main():
    module = AnsibleModule(argument_spec = dict(
             src = dict(type='str', required=True)
             ),
             add_file_common_args=True)
    
    ret_code = 0
    
    ret_code, response = read_xl_content(module.params["src"])
    
    if ret_code:
        module.fail_json(msg=response)
    else:
        module.exit_json(changed=False, **response)

    return ret_code


if __name__ == '__main__':
    main()