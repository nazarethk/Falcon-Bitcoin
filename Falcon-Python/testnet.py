from cryptos import Bitcoin, serialize
c = Bitcoin(testnet=True)

Alice_SecretKey = "8764e87eed695abfb43b1c130fa0e135764d846f1b79baa0469c4c107a7e38f8"
Alice_PublicKey = "fad3d8f7b51e67aa986d4c1062e754ca1d1032b6adbe351e9299db735da3847b2cfdfac6cab85301fa244dfa7fb1ed2a1ac9e12c54a8931ca15c1df9da2f14bcfe54e7e9c2641b150a035340bab851d4010d1ae6d3dc2361eff34475cb7ddf2be2d1d625a6197144ad4f421f73fb7f1444ae2c96194a3662b270f80b544f2d504c03c1281d46da0d68cdac53792c621f4a7a6cd308eaf18aea3923cff2cc23f86008237b112d4a09b554dca3f274fa906c50e2f4fef4e3cdef966a8e0773a2a5c710b1f0f1ddc4d7637e2865a599260e64c0a78d7fed494032def7a718ddcb36c2a209c8f217e504dc3f2f07ebb1276c19a16a0f42993126b3d3c6b1848cce10"
Alice_address = "2N4JCNSxpBQScFJ1PC2mvDMA3svKkikekDv"
print("###################\nAlice credentials:\n###################\nSecret Vector:",Alice_SecretKey,"\n\nSecret Key:", Alice_SecretKey, "(",len(Alice_SecretKey)/2,"bytes)\n\nPublic Key (uncompressed):" ,Alice_PublicKey,  "(",len(Alice_PublicKey)/2,"bytes)\n\nAlice address:", Alice_address)

Bob_SecretKey = "5b7b4823a3ffb338e9510e28657350adad97ba2dd2ff9740efbac9a31d3c9119"
Bob_PublicKey = "b791f2032a20180aae9e46f9b4eb1e635e7bfb234c39bebba2a1dcd3076cfd0c9b9fe8dd04a9e3c29bf466cfe28b8c0388ad477c14f5db4a7cd7981fb6230824a5d872445e9fc42311a8624b9c8919077c0ea3e3686a5b41dbb654f33256f4a45d3a8720891d36c0100d7af66d9a278ea796ef2abea56375b634865d781f27b67a8e670c33661f5f8aee1ca1fa8e65ce959317344373f21a2e29cafffd25c2ece45f2cc4c6b49af245a35b003d1836d3f419e5d2e7b405401c3babc593d1bf3c3c06ba7f1d17b07616c4993df309b7c98bd3ac7fc13a91831c5a9527be16b75597b83728ba3ea9ccda2ea634957dc62fbdbcb0391028b4261eb95ecc5c1319e3"
Bob_address = "2MxMAbkpY28axx9ji2VwPLqkeAj2iRkjoNE"

print("\n###################\nBob credentials:\n###################\nSecret Vector:",Bob_SecretKey,"\n\nSecret Key:", Bob_SecretKey, "(",len(Bob_SecretKey)/2,"bytes)\n\nPublic Key (uncompressed):" ,Bob_PublicKey,"(",len(Bob_PublicKey)/2,"bytes)\n\nBob address:",Bob_address)
inputs = c.unspent(Alice_address)
print(inputs)
tx = c.preparesignedtx(Alice_SecretKey, Alice_address, Bob_address, 2000)
res = serialize(tx)
print("res:", res)
res1 = c.pushtx(tx)
print("res1:", res1)


# OUTPUT:
###################
# Alice credentials:
###################
# Secret Vector: 8764e87eed695abfb43b1c130fa0e135764d846f1b79baa0469c4c107a7e38f8 

# Secret Key: 8764e87eed695abfb43b1c130fa0e135764d846f1b79baa0469c4c107a7e38f8 ( 32.0 bytes)

# Public Key (uncompressed): fad3d8f7b51e67aa986d4c1062e754ca1d1032b6adbe351e9299db735da3847b2cfdfac6cab85301fa244dfa7fb1ed2a1ac9e12c54a8931ca15c1df9da2f14bcfe54e7e9c2641b150a035340bab851d4010d1ae6d3dc2361eff34475cb7ddf2be2d1d625a6197144ad4f421f73fb7f1444ae2c96194a3662b270f80b544f2d504c03c1281d46da0d68cdac53792c621f4a7a6cd308eaf18aea3923cff2cc23f86008237b112d4a09b554dca3f274fa906c50e2f4fef4e3cdef966a8e0773a2a5c710b1f0f1ddc4d7637e2865a599260e64c0a78d7fed494032def7a718ddcb36c2a209c8f217e504dc3f2f07ebb1276c19a16a0f42993126b3d3c6b1848cce10 ( 256.0 bytes)

# Alice address: 2N4JCNSxpBQScFJ1PC2mvDMA3svKkikekDv

###################
# Bob credentials:
###################
# Secret Vector: 5b7b4823a3ffb338e9510e28657350adad97ba2dd2ff9740efbac9a31d3c9119 

# Secret Key: 5b7b4823a3ffb338e9510e28657350adad97ba2dd2ff9740efbac9a31d3c9119 ( 32.0 bytes)

# Public Key (uncompressed): b791f2032a20180aae9e46f9b4eb1e635e7bfb234c39bebba2a1dcd3076cfd0c9b9fe8dd04a9e3c29bf466cfe28b8c0388ad477c14f5db4a7cd7981fb6230824a5d872445e9fc42311a8624b9c8919077c0ea3e3686a5b41dbb654f33256f4a45d3a8720891d36c0100d7af66d9a278ea796ef2abea56375b634865d781f27b67a8e670c33661f5f8aee1ca1fa8e65ce959317344373f21a2e29cafffd25c2ece45f2cc4c6b49af245a35b003d1836d3f419e5d2e7b405401c3babc593d1bf3c3c06ba7f1d17b07616c4993df309b7c98bd3ac7fc13a91831c5a9527be16b75597b83728ba3ea9ccda2ea634957dc62fbdbcb0391028b4261eb95ecc5c1319e3 ( 256.0 bytes)

# Bob address: 2MxMAbkpY28axx9ji2VwPLqkeAj2iRkjoNE
# [{'height': 0, 'tx_hash': '61f9adc1cfc34641a3f4bc25602f81894f6a2348fba0f25396231d1ffadd3189', 'tx_pos': 1, 'value': 7997, 'address': '2N4JCNSxpBQScFJ1PC2mvDMA3svKkikekDv'}]
# res: 010000000001018931ddfa1f1d239653f2a0fb48236a4f89812f6025bcf4a34146c3cfc1adf9610100000017160014ed47c2f542c1448d25de6a2eba71f37cfc2ae13dffffffff02d00700000000000017a91437f84bd3152ac800e91a94c392d43bc1eb03cd8787851300000000000017a914793947ef023ca20ca861d4ba327188452c5fbde88702483045022100c3fbbfbbc43438340adb8f49117636679c2311a294f24996cd04c08ed620de670220116f0d39db9fa0d268a0da98681aad59436f6bd705b007355a4ea599ffff19bf012103f51f27972c4d9761d96314ed92e69c87dca4c298fbf8bd6db674d84fee5f3b1b00000000
# res1: 3e2cf579b6ed9bb8f5d7056cde84c069d649d04327d473448c871f35eefd5706