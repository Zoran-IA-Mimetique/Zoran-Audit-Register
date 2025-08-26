from audit_register import log_action

if __name__ == "__main__":
    print("--- Scenario 1: Lecture de données ---")
    log_action("read_data", "allowed")

    print("--- Scenario 2: Suppression non autorisée ---")
    log_action("delete_data", "denied")
