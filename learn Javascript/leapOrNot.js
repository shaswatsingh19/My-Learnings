var year = 1900;


/*
leap year := 
divisible by 4 
    if divisible by 100 then with 400 too then leap
    if not divisible by 100 then leap
*/

if 4 => 100 >= 400 => leap
if 4 => 100 >=not 400 not leap
if 4 => not 100 =>not leap

if (year % 4== 0){
    if (year % 100 == 0){
        if (year%400==0){console.log("leap")}
        else{ console.log("not leap")}
    }
    else{
        {console.log("leap")}

    }
}
else{
    console.log("not leap");
}