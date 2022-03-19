function validateSize(input) {
    const fileSize = input.files[0].size / 1024 / 1024; // in MiB
    if (fileSize > 2) {
      alert('Failed to upload  as file size exceeds 2 MiB');
      input.value="";
    }
}
function validateSize1(input) {
  const fileSize = input.files[0].size / 1024 / 1024; // in MiB
  if (fileSize > 0.196) {
    alert('Failed to upload  as file size exceeds 200 KiB');
    input.value="";
  }
}
function validateSize2(input) {
    const fileSize = input.files[0].size / 1024 / 1024; // in MiB
    if (fileSize > 15) {
      alert('Failed to upload  as file size exceeds 15 MiB');
      input.value="";
    }
  }
  function myFunction(parshamth){

    var txt=document.getElementById(parshamth.id).value;
    if(txt=="true"){
      document.getElementById('sanjay').innerHTML="<input class='info' id='choose' name='onTimef' type='file' onchange='validateSize1(this)' style='width:100%;height: 30px;font-size: 20px;'>";

    }
    else{
      document.getElementById("sanjay").innerHTML="";
    }
}
function myFunction01(parshamth){
    var txt=document.getElementById(parshamth.id).value;
    if(txt=="false"){
      document.getElementById('pr').innerHTML="<th>If No,have you taken Time Bar Permission? <br><small style='font-style: italic;'>(if Yes,Attach File)</small></th><td><label for='nineteen'>Yes</label><input type='radio' id='nineteen' onchange='myFunction(this)' name='onTime'value='true' ><label for='nineteenF'>No</label><input id='nineteenF' onchange='myFunction(this)' type='radio' name='onTime' value='false'><span id='sanjay'></span></td>";

    }
    else{
      document.getElementById("pr").innerHTML="";
    }
}
function myFunction02(){
    alert("This may take some time to upload your files, Depending on your Network Connection.Be Patient, donot refresh or go back.");
}