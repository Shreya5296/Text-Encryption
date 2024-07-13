# Text and Image Encryption

**Block** can be defined as a square box. Which has three sides,
1. Data - Some part of the block contains information which is known as data. This data is nothing but information about sender, receiver and how many coins(money) have been transferred.
2. Hash code - Hash code is nothing but the fingerprint of the block. It is the mainsecurity feature available in blockchain which makes blockchain unbreakable.
3. Previous Hash - Hash of previous block is nothing but information of previous block. Since each block is tied up to the next block in the chain. Having information about the previous block is mandatory to make the block chain more secure.

If any hacker tries to break into the blockchain then the hacker needs to chain the entire blockchain hash code as well as the previous block. And this process is very difficult.
Chain is nothing but a sequence of multiple blocks connected together in chain format. Blockchain technology widely used in cryptocurrency transactions

**Cryptocurrency** :
It is a form of payment that can be exchanged online for goods and services. Cryptocurrencies work using a technology called blockchain.
● For example, if you sell your phone then you will receive money into your bank account but if you use cryptocurrency to sell your phone you can receive coins which are nothing but money which hold some good value in the market.
● Blockchain is a decentralized technology spread across many computers that manages and records transactions. Decentralized technology means the technology which does not come under
any goverstand authority.
● Cryptocurrency is a great example of blockchain. We have multiple cryptocurrency such as Bitcoin, Ethereum and so on

**Hashing** is the method which makes blockchain technology secure
Hashing is the process of transforming any given key or a string of characters into another value. This value is non-readable by humans but it can be read by machines or systems.
Hash function is nothing but a mathematical function which encrypts data from original text to secure format.

A good hash function uses a one-way hashing algorithm, or in other words, the hash cannot be converted back into the original key.
Imagine a hashing algorithm as a one way road.

Why we are using hashing in blockchain ??
Hashing makes blockchain secure that converting hash code back to original text is impossible. And hash also works as a fingerprint of the data. Fingerprint of the data means just like our fingerprint is unique and it is used to provide security just like that we can use the same method to secure our blockchain transaction. Which is unique and untraceable.
Thus hashing is widely used in blockchain.
There are multiple hashing algorithms which can be used to transform plain text to hash code such as **RSA, SHA**, and many more.
We will use SHA and we will code for the same

SHA-1 or Secure Hash Algorithm 1 is a cryptographic hash function which takes an input and produces a hash value.
SHA algorithm uses an encoding method for hashing.

Today we will be doing hashing on a plain text and we will do this by 2 ways
1. Using sandbox online
2. Using python code offline
   
**Sandbox Implementation** -
**Link -**  https://sandbox.eth.build/build#1f266bbf4596af1c2b101094ed4baa6f49179fced00ba087b5ccdf20cbfcb7d6 
We are implementing hashing into Sandbox to see how hashing looks like in block coding.
1. Implement hashing into sandbox
● To implement hashing into a sandbox.
● Once you open the site you can see a blank black screen
● Now to create hash function press SPACEBAR
● Then choose Crypto/Hash
● Once you select Crypto/Hash, it contain two parameters.
  1. Input - Input is something which the sandbox accepts as plain text.
  2. Hash - Hash is output which will return a hashing string.
● Now, double click on Input Which will create one more block name TEXT.
● Here you can provide a string which will be set as input.
● You can type any text in the TEXT block.
● Now double click on Hash. It will create one more block named string.
● In this block we have hashed a string of text plain text which is game

**Using Python Code Implementation** - 
1. First we need to import the hashlib library. Which can be used to hash any text 
This library is used to convert string or any input such as number, text, image into secure text. Which is non-readable by humans.
2. Initialize string
3. Hash string using SHA3_256 algorithm
4. Print converted secure hash string

**Testing the code For Mac:**
1. Go to “BLOCKCHAIN” folder in Documents directory
2. Open BLOCKCHAIN folder
3. Run text_encryption.py file in terminal using python text_encryption.py
To run file in terminal first open terminal by pressing command + SPACEBAR key and type ‘terminal’
4. Then locate Documents folder using cd command as cd Documents
5. Now create one new environment using conda command as conda create -n blockchain python==3.8
6. Now activate blockchain environment as conda activate blockchain
7. If you see confirmation window please click on OK
8. Then locate BLOCKCHAIN folder using cd command as cd BLOCKCHAIN
9. Now, run python file as python text_encryption.py
10. Now you can see the output.

**Testing the code For Windows :**
1. Go to “BLOCKCHAIN” folder in Documents directory
2. Open BLOCKCHAIN folder
3. Open terminal in this folder
4. Now create one new environment using conda command as conda create -n blockchain python==3.8
5. Now activate blockchain environment as conda activate blockchain
6. Now, run python file as python text_encryption.py
7. Now you can see the output


