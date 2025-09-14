#!/usr/bin/env python3

import hashlib
import base58
import os
import time

DIVI_P2PKH_VERSION = 0x1e  # 'D'

def generate_random_divi_burn_address():
    # 20 random bytes — not from a real pubkey, totally unlinked
    random_hash = os.urandom(20)
    payload = bytes([DIVI_P2PKH_VERSION]) + random_hash
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    address = base58.b58encode(payload + checksum).decode()
    return address

def mine_divi_burn_addresses(prefixes):
    found = {}
    attempts = 0
    start = time.time()

    try:
        while True:
            addr = generate_random_divi_burn_address()
            attempts += 1

            for prefix in prefixes:
                if prefix not in found and addr.startswith(prefix):
                    elapsed = time.time() - start
                    print(f"\n🔥 MATCH: {addr} (prefix '{prefix}')")
                    print(f"⏱️  Found after {attempts:,} attempts in {elapsed:.2f} sec")
                    found[prefix] = addr

            if attempts % 1_000_000 == 0:
                print(f"⛏️  Checked {attempts // 1_000_000:,} million so far...")

            if len(found) == len(prefixes):
                print("\n✅ All vanity burn addresses found:")
                for p, a in found.items():
                    print(f"  {p}: {a}")
                break

    except KeyboardInterrupt:
        print("\n🛑 Stopped by Interrupt. Results so far:")
        for p, a in found.items():
            print(f"  {p}: {a}")

if __name__ == "__main__":
    prefixes = ["D1337", "D1E", "DBURN"]
    print(f"🚀 Mining Divi meme burn addresses for: {', '.join(prefixes)}")
    mine_divi_burn_addresses(prefixes)
