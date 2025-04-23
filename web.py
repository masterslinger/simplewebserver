from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<html>
<head>
<title>TCP/IP PROTOCOLS</title>
</head>
<body><center>
    <h1>TCP/IP Protocol Suite</h1>
    <table border="5" cell panding="1" align="center">
        <tr>
            <th>TCP/IP Layer</th>
            <th>Key Protocols</th>
       </tr>
       <tr>
            <td>Application Layer</td>
            <td>HTTP, HTTPS, FTP, SMTP, POP3, IMAP, DNS, DHCP, TELNET, SNMP</td>
       </tr>
       <tr>
            <td>Transport Layer</td>
            <td>TCP, UDP, SCTP</td>
       </tr>
       <tr>
            <td>Internet Layer</td>
            <td>IP (IPv4, IPv6), ICMP, ARP, IGMP</td>
       </tr>
       <tr>
            <td>Network Access Layer</td>
            <td>Ethernet, Wi-Fi (IEEE 802.11), PPP, Frame Relay, DSL</td>
       </tr>
    </table>
</center>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()