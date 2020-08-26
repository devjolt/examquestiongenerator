//Used on subject home pages and question pages
function setCookie (cName, cValue){//sets a cookie
    document.cookie = `${cName}=${cValue};path=/`;
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
      var c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "nope";
}

//Used with multi_choice_dynamic.html question pages
function resetCookies(){
    setCookie('sql_attempts', '0')
    setCookie('sql_correct', '0')
}

function calculatePercentage(){
    if (getCookie('sql_attempts') == 0){
      return 0;
    }else{
      var percent = Math.ceil( getCookie('sql_correct') / getCookie('sql_attempts') * 100);
      return percent;
    }
}
  
function incrementCookie(cName){
    var value = parseInt(getCookie(cName)) + 1;
    setCookie(cName, value)
    console.log('Incremented')
    console.log(cName)
}
    
function ifRespondedCorrect(correct){
  if (responded == 0){
    responded = 1
    incrementCookie('sql_attempts');
    console.log('first response');
    if (correct == 'yes'){
      incrementCookie('sql_correct');
      console.log('Plus 1 to correct');
    }else{
      console.log('Wrong');
    }
   }else{
      console.log('SOOOO many clicks');
    }
}

// when question is incorrect, add question type to list stored in cookie
// get list stored in cookie and put on screen somewhere
function createWorkOnCookie(){//Creates cookie to record subjects to work on, if not existing
    if (getCookie("work_on") == 'nope'){
        document.cookie = "work_on='';path=/;"
        console.log('set workon cookie')
    }
    else{
      console.log('no need to set')
    }
}



