# Zoran-Audit-Register — Journal immuable basé Merkle

## 🌍 Contexte
L’intégrité des journaux est essentielle pour l’IA réglementée (RGPD, AI Act).  
Beaucoup d’IA conservent des logs textuels : facilement modifiables, difficilement auditables.  

**Zoran aSiM** propose un **registre immuable**, basé sur un **arbre de Merkle**, permettant à quiconque de vérifier l’intégrité des décisions.  

## ⚙️ Fonctionnement
- Chaque entrée (`action`, `status`, `timestamp`) est hashée.  
- Les hashs sont regroupés en paires → construisent un arbre de Merkle.  
- La racine de Merkle (`merkle_root`) devient la preuve globale d’intégrité.  
- Toute modification d’une entrée change la racine → fraude détectable.  
- ΔM11.3 peut annuler une session entière si la racine change de manière anormale.  

## 📜 Exemple
```json
{
  "entries": [
    {"id": "entry_1", "action": "read_data", "status": "allowed", "hash": "a12b..."},
    {"id": "entry_2", "action": "delete_data", "status": "denied", "hash": "c45f..."}
  ],
  "merkle_root": "9f3e..."
}
```

## 🧪 Démonstration
`demo.py` simule :  
- actions conformes (lecture avec consentement),  
- actions rejetées (suppression interdite).  

À la fin, l’arbre de Merkle est généré et validé.  

## 📊 Objectifs
- Fournir une **preuve technique d’intégrité** vérifiable publiquement.  
- Rendre impossible la falsification silencieuse.  
- Assurer un lien fort entre **éthique**, **auditabilité** et **conformité légale**.  
