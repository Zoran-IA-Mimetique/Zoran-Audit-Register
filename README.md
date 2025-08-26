# Zoran-Audit-Register

**Audit Register** est la brique de Zoran aSiM qui assure l’**intégrité totale** des journaux par **arbre de Merkle**.  
Chaque action critique génère une entrée dans `audit_log.json`, liée à un hash parent.  
Résultat : tout audit peut **rejouer** la chaîne et vérifier son intégrité.  

## 🚀 Fonctionnalités
- Journal d’audit immuable (JSON).  
- Arbre de Merkle pour vérification d’intégrité.  
- Rollback ΔM11.3 si falsification détectée.  
- Démonstration reproductible (`demo.py`).  
- Tests unitaires.  

## 📖 Démonstration
```bash
python demo.py
```

## 📜 Exemple de log
```json
{
  "id": "entry_001",
  "action": "process_user_data",
  "status": "allowed",
  "timestamp": 1693059999.789,
  "hash": "7ac2f...c19e"
}
```

## 🔗 Liens associés
- White Paper : *“Zoran Auditability Framework: Merkle Journals and ΔM11.3 Resilience”*.  
- Contact : tabary01@gmail.com  

## 📄 Licence
MIT — usage libre.  
© 2025, Frédéric Tabary — Projet Zoran aSiM
