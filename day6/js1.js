let x=0;
let y=0;
let z=1;
if(++x && ++y && z++ && y-- && --y && --y && y-- || ++z){
    console.log(x,y,z)
}