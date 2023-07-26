module.exports = function(RED) {
    function KepwareWrite(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            if(msg.topic && msg.payload) {
                var v = [{"id": msg.topic,"v": msg.payload}];
                msg.payload = v;
                node.send(msg);
            }
        });
    }
    RED.nodes.registerType("kepware-write",KepwareWrite);
}