function displayName(myName){
    console.log(myName)
}


displayName("sss");


function sum(a,b){
    return a+b;
}

console.log(sum(1,2));


// anonymous function 

var funExp = function(a,b){
    return a*b;
}

console.log(funExp(10,2));// function with no name

console.log((33).toString);


/*
Value	String Conversion	Number Conversion	Boolean Conversion
1	        "1"	                    1	            true
0	        "0"	                    0	            false
"1"	        "1"                    	1           	true
"0"	        "0"	                    0                true
"ten"	    "ten"	                NaN               true
true	    "true"	                1	            true
false	    "false"                	0	            false
null	    "null"	                0	             false
undefined	"undefined"	            NaN	            false
''	            ""	               0	            false
' '	            " "	                0	            true

*/