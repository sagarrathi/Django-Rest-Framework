
e1=document.querySelector("#event1");
e2=document.querySelector("#event2");
e3=document.querySelector("#event3");

var boxes=document.querySelectorAll("#gamecell");


flag="X"
function xomarker(box){
  box.addEventListener("click", function(){
  box.textContent=flag;
  if(flag=="X"){flag="O";} else{flag="X";}
  })
                      }
boxes.forEach(xomarker)



reset_button=document.querySelector("#gamereset")

function xoreseter(box){
  box.textContent="";
}


reset_button.addEventListener("click", function(){
  boxes.forEach(xoreseter);
})



e1.addEventListener("mouseover", function(){
    e1.style.color="red"; 
    e1.textContent="hover hua hai"
    })

e1.addEventListener("mouseout", function(){
    e1.style.color="black"; 
    e1.textContent="Hover"
  })

e2.addEventListener("click", function(){
    e2.style.color="green"; 
    e2.textContent="click hua hai"
    })

e3.addEventListener("dbclick", function(){
    e3.style.color="blue"; 
    e3.textContent="double click hua hai"
  })





function getRandomColor(){
  r=Math.floor(Math.random()*255)
  g=Math.floor(Math.random()*255)
  b=Math.floor(Math.random()*255)
  color="rgb("+r+","+g+","+b+")"
  return color
}

setInterval(function() {
  color=getRandomColor();
  x=document.querySelector("h1");
  x.style.color=color;
  // method to be executed;
}, 500);


var employee = {
    name: "John Smith",
    job: "Programmer",
    age: 31
  }


var car = {
            type:"Fiat", 
            model:"500", 
            color:"white", 
            fun:function(){
                console.log("kya bolta tu")
                } 
            };

rooster=[]

// answer=""

// while (answer!="quit"){
//     answer=prompt("Enter command");
//     if (answer=="add"){
//         x=prompt("Enter name");
//         rooster.splice(rooster.length,0,x);
//     }
    
//     if (answer=="remove"){
//         x=prompt("Enter name");
//         i=rooster.indexOf(x);
//         rooster.splice(i,1);
//     }
    
//     if (answer=="display"){
//       console.log(rooster);
//     }
    
    
// }

// function tagger(name){
//     console.log(name+" is awsome");
// }

// var topics=["this", "is", "black"];

// topics.forEach(tagger);


// for (t of topics){
//     alert(t);}


// y=100;
// function x(y=20){
//     return(y);
// }
// // for(var i=0; i < 5;i++) {
// //     alert(i);
// // }

// answer="n"
// while(answer!="y"){
//     answer=prompt("Are you above 18 (y/n)")
//     }

// lbs=prompt("Enter weight in \"lbs\"");
// kg=lbs*.45
// if(lbs>50){alert("So heavy weight")}
// else {alert("Low weight")}
// alert(lbs+" lbs is equal to:\n"+kg+" kg");
// console.log("Calcualtion completed successfully")
