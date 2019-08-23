/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
    
    var period = ".";
    var replace = "[.]";
    //var length = address.length;
    var defangedAddress = "";
    //console.log(length);
    
    //console.log(address.replace(address, replace));

    for(var i = 0; i < address.length; i++){
        if(period == address.charAt(i)){
            defangedAddress += replace;
        } else {
            defangedAddress += address.charAt(i);
        }
    }
    return defangedAddress;
}
