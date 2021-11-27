// https://codedamn.com/challenge/IrwD7q6WkiIold03su0XS

const time = '12:0AM';

function convertTo24HrsFormat(time) {
    // write your solution here
    let ans="";
    let l = time.length;
    let check = time[l-2]+time[l-1];

    time  = time.replace(check,"");
    console.log(time);
    time = time.split(":");
    h = time[0];
    m = time[1];
    if(check == 'AM'){
        h = h % 12;
        
    }
    else if(check=="PM" && (h>0 && h<12)) {
        h = parseInt(h) + parseInt(12);
    }
    if(h<10 && String (h.length<2)){
        h = "0"+h;
    }
    if(m<10 && m.length<2){
        m = "0"+m;
    }
    ans = h +":"+m;
    return ans;
}

console.log(`Converted time: ${convertTo24HrsFormat(time)}`)
