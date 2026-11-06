# Hálózati függvények

Az MQL5-programok adatokat cserélhetnek távoli szerverekkel, továbbá push értesítéseket, e-maileket és FTP-adatokat küldhetnek.

- A [Socket\*](SocketCreate/SocketCreate.md) függvénycsoport rendszerfoglalatokon keresztül TCP-kapcsolatot — akár biztonságos TLS-kapcsolatot is — hoz létre távoli gépekkel. A használat menete: [foglalat létrehozása](SocketCreate/SocketCreate.md), [csatlakozás a szerverhez](SocketConnect/SocketConnect.md), majd adatok [olvasása](SocketRead/SocketRead.md) és [írása](SocketSend/SocketSend.md).
- A [WebRequest](WebRequest/WebRequest.md) függvénnyel webes erőforrások érhetők el, és egyszerűen küldhetők HTTP-kérések, például GET és POST kérések.
- A [SendFTP](SendFTP/SendFTP.md), [SendMail](SendMail/SendMail.md) és [SendNotification](SendNotification/SendNotification.md) függvényekkel fájlokat, e-maileket és mobilértesítéseket lehet küldeni.

A végfelhasználók biztonsága érdekében az ügyfélterminál tartja nyilván az engedélyezett IP-címeket. Az MQL5-program csak olyan címekhez csatlakozhat a Socket\* és WebRequest függvényekkel, amelyek szerepelnek ezen a listán. Ha például a programnak a `https://www.someserver.com` címhez kell csatlakoznia, a felhasználónak ezt a címet meg kell adnia a terminálban. A címlista programból nem módosítható.

![Cím felvétele az engedélyezési listára](../assets/allow_net_request.png "Cím felvétele az engedélyezési listára")

Az MQL5-programban külön jelezd a felhasználónak, ha további beállításra van szükség. Erre használható a [#property description](../Language-Basics/Preprocessor/Program-Properties-(#property)/Program-Properties-(#property).md), az [Alert](../Common-Functions/Alert/Alert.md) vagy a [Print](../Common-Functions/Print/Print.md) függvény.

| Függvény | Működés |
| --- | --- |
| [SocketCreate](SocketCreate/SocketCreate.md) | Foglalatot hoz létre a megadott jelzőkkel, és visszaadja a leíróját. |
| [SocketClose](SocketClose/SocketClose.md) | Bezár egy foglalatot. |
| [SocketConnect](SocketConnect/SocketConnect.md) | Időtúllépés-kezeléssel csatlakozik a szerverhez. |
| [SocketIsConnected](SocketIsConnected/SocketIsConnected.md) | Ellenőrzi, hogy a foglalat csatlakozik-e. |
| [SocketIsReadable](SocketIsReadable/SocketIsReadable.md) | Visszaadja a foglalatból olvasható bájtok számát. |
| [SocketIsWritable](SocketIsWritable/SocketIsWritable.md) | Ellenőrzi, hogy az adott pillanatban írhatók-e adatok a foglalatba. |
| [SocketTimeouts](SocketTimeouts/SocketTimeouts.md) | Beállítja a foglalat adatfogadási és -küldési időkorlátait. |
| [SocketRead](SocketRead/SocketRead.md) | Adatokat olvas a foglalatból. |
| [SocketSend](SocketSend/SocketSend.md) | Adatokat ír a foglalatba. |
| [SocketTlsHandshake](SocketTlsHandshake/SocketTlsHandshake.md) | TLS Handshake protokollal biztonságos TLS-kapcsolatot kezdeményez a megadott géppel. |
| [SocketTlsCertificate](SocketTlsCertificate/SocketTlsCertificate.md) | Lekéri a hálózati kapcsolat biztonságát szolgáló tanúsítvány adatait. |
| [SocketTlsRead](SocketTlsRead/SocketTlsRead.md) | Adatokat olvas a biztonságos TLS-kapcsolatból. |
| [SocketTlsReadAvailable](SocketTlsReadAvailable/SocketTlsReadAvailable.md) | Beolvassa a biztonságos TLS-kapcsolaton elérhető összes adatot. |
| [SocketTlsSend](SocketTlsSend/SocketTlsSend.md) | Adatokat küld a biztonságos TLS-kapcsolaton. |
| [WebRequest](WebRequest/WebRequest.md) | HTTP-kérést küld a megadott szervernek. |
| [SendFTP](SendFTP/SendFTP.md) | Fájlt küld a beállítások FTP lapján megadott címre. |
| [SendMail](SendMail/SendMail.md) | E-mailt küld a beállítások E-mail lapján megadott címre. |
| [SendNotification](SendNotification/SendNotification.md) | Push értesítést küld az Értesítések lapon megadott MetaQuotes ID-khez tartozó mobilterminálokra. |
