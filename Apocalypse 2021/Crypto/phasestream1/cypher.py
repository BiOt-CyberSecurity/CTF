#!/usr/bin/env python

cypher = bytes.fromhex('2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904')
print (cypher)

plaintext = b'CHTB{'

key = ''.join(chr(c ^ m) for c, m in zip(cypher, plaintext))

print(key)
