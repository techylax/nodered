// UDP Message with BAckslash

var hexString = "5C6170706C65"; // Hexadecimal string to send
var buffer = Buffer.from(hexString, 'hex');
msg.payload = buffer;
return msg;