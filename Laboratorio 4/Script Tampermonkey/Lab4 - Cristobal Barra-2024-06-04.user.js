// ==UserScript==
// @name         Lab4 | Cristobal Barra
// @namespace    http://tampermonkey.net/
// @version      2024-06-04
// @description  try to take over the world!
// @author       You
// @match        https://cripto.tiiny.site/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=tiiny.site
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js#sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==
// ==/UserScript==

(function() {
    'use strict';

    // Función para obtener llave
    function getKey() {
        // Extraer todas las letras mayúsculas del contenido de la página
        let uppercaseLetters = document.body.innerText.match(/[A-Z]/g) || [];
        let key = uppercaseLetters.join('');
        console.log(`La llave es: ${key}`);
        return key;
    }

    // Ejecutar función de obtención de llave
    const key = getKey();

    // Función para contar mensajes cifrados
    function countEncryptedMessages() {
        let encryptedElements = document.querySelectorAll('[class^="M"]');
        let count = encryptedElements.length;
        console.log(`Los mensajes cifrados son: ${count}`);
        return count;
    }

    // Ejecutar funcińón de conteo de mensajes
    const encryptedCount = countEncryptedMessages();

    // Función para descifrar usando CryptoJS
    function decryptMessages(key) {
        let encryptedElements = document.querySelectorAll('[class^="M"]');

        encryptedElements.forEach(function(element) {
            let encryptedTextBase64 = element.getAttribute('id');

            try {
                // Decodificar el texto cifrado desde Base64
                let encryptedText = CryptoJS.enc.Base64.parse(encryptedTextBase64);

                // Convertir la clave a bytes
                let keyBytes = CryptoJS.enc.Utf8.parse(key);

                // Configurar las opciones de descifrado
                const options = { mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.Pkcs7 };

                // Descifrar el texto cifrado
                const decrypted = CryptoJS.TripleDES.decrypt(
                    { ciphertext: encryptedText },
                    keyBytes,
                    options
                );

                let decryptedText = decrypted.toString(CryptoJS.enc.Utf8);

                if (decryptedText) {
                    console.log(`${encryptedTextBase64} ${decryptedText}`);
                    // Actualizar el contenido del elemento con el texto descifrado
                    element.textContent = decryptedText;
                } else {
                    console.log(`No se pudo descifrar el texto de ${element.className}.`);
                }
            } catch (e) {
                console.error("Error al descifrar el mensaje:", e);
            }
        });
    }

    // Ejecutar función de descifrado de mensajes
    decryptMessages(key);


})();

