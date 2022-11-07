async function loop(){
  let a;
  await  setTimeout(()=>{a=10},2000)
    console.log(a)
}

console.log("Start")
loop()
console.log("End")