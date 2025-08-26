import json, hashlib, time, os

LOG_FILE = "logs/audit_log.json"

def hash_entry(entry):
    entry_str = json.dumps(entry, sort_keys=True).encode("utf-8")
    return hashlib.sha256(entry_str).hexdigest()

def build_merkle_root(entries):
    hashes = [e["hash"] for e in entries]
    if not hashes:
        return "0"*64
    while len(hashes) > 1:
        temp = []
        for i in range(0, len(hashes), 2):
            h1 = hashes[i]
            h2 = hashes[i+1] if i+1 < len(hashes) else h1
            temp.append(hashlib.sha256((h1+h2).encode("utf-8")).hexdigest())
        hashes = temp
    return hashes[0]

def log_action(action, status):
    entry = {
        "id": f"entry_{int(time.time()*1000)}",
        "action": action,
        "status": status,
        "timestamp": time.time()
    }
    entry["hash"] = hash_entry(entry)

    entries = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            entries = json.load(f).get("entries", [])
    entries.append(entry)

    merkle_root = build_merkle_root(entries)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump({"entries": entries, "merkle_root": merkle_root}, f, indent=2)

    print(f"📝 Action logged: {entry['action']} (status={status})")
    print(f"🌐 Merkle root: {merkle_root}")
    return entry, merkle_root
