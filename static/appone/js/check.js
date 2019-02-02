
var i=0;
function hide(){

      if(i==0){
            document.getElementById("box").style.display= "none";
            i=1;
      }
      else if(i==1){
            document.getElementById("box").style.display= "block";
            i=0;
      }

}