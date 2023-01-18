const URL_PREFIX="http://192.168.0.104:10240/";
const APIS={
    test:"api/test",
    download1:"api/vd1",
    download2:"api/ud2",
    first:"api/first",
    second:"api/second",
    dele:"api/dele",
    email:"api/email",
    kill:"api/kill",
    getusername:"api/getusername",
    getperiod:"api/period"
}


for(const i in APIS){
    APIS[i]=URL_PREFIX+APIS[i];
}
export default APIS;
