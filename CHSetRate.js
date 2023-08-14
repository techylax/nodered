msg.payload.down = 0;
if (msg.payload.value == "2") {
    flow.set("RunSet",2);
    msg.enabled = false;
    msg.payload.value = flow.get("RunSet");
    return msg
} else if (msg.payload.value == "1") {
    flow.set("RunSet",1);
    msg.enabled = false;
    msg.payload.value = flow.get("RunSet");
    return msg
} else if (msg.payload.value == "3"){

// This next piece will make sure that downtime only required if machine was in run
// If machine was in set up and stopped, no downtime code needed, assuming down for set up still

    if(flow.get("RunSet") == 1){
        msg.payload.down = 3;
        msg.enabled = true;
        msg.topic = "show";
        msg.payload.value = flow.get("RunSet");
        return msg
    } 
}


