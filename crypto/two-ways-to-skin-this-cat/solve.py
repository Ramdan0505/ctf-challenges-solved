import crypt

SHADOW_PATH = "shadow"
WORDLIST_PATH = "password-clean.lst"

def parse_shadow(path: str):
    users = []
    hashes = {}
    with open(path, "r", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            user, rest = line.split(":", 1)
            shadow_hash = rest.split(":")[0]
            users.append(user)
            hashes[user] = shadow_hash
    return users, hashes

def crack_sha512_crypt(shadow_hash: str, candidates: list[str]) -> str | None:
    # $6$salt$hash  -> salt token must be "$6$salt$"
    parts = shadow_hash.split("$")
    salt = f"${parts[1]}${parts[2]}$"
    for pw in candidates:
        if crypt.crypt(pw, salt) == shadow_hash:
            return pw
    return None

def main():
    users, hashes = parse_shadow(SHADOW_PATH)

    with open(WORDLIST_PATH, "r", errors="ignore") as f:
        candidates = [line.strip() for line in f if line.strip()]

    cracked = {}
    for user in users:
        pw = crack_sha512_crypt(hashes[user], candidates)
        if pw is None:
            raise SystemExit(f"[-] Failed to crack: {user}")
        cracked[user] = pw
        print(f"[+] {user}: {pw}")

    key = "".join(cracked[u] for u in users)
    print("\n[+] Concatenated key:")
    print(key)

if __name__ == "__main__":
    main()
