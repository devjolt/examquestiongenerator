//setting cookies if they don't exist: comptia_a_plus_attempts, comptia_a_plus_possible, comptia_a_plus_correct
if (getCookie('comptia_a_plus_attempts') == 'nope')
  {
  setCookie("comptia_a_plus_attempts",'0');
  console.log("No comptia_a_plus_attempts cookie so we made one");
  }
if (getCookie('comptia_a_plus_possible') == 'nope')
  {
  setCookie("comptia_a_plus_possible",'0');
  console.log("No comptia_a_plus_possible cookie so we made one");
  }
if (getCookie('comptia_a_plus_correct') == 'nope')
  {
  setCookie("comptia_a_plus_correct",'0');
  console.log("No comptia_a_plus_cookie so we made one");
  }

document.onload = createWorkOnCookie()



//Allows stats to be reset onclick of button
function resetCookies(){
    console.log("Resetting cookies!")
    setCookie('comptia_a_plus_attempts', '0')
    setCookie('comptia_a_plus_possible', '0')
    setCookie('comptia_a_plus_correct', '0')
}

//Allows reset of visual elements
function resetElements(){
  console.log("Visual elements reset");
  document.getElementById("attempted").innerHTML = '0';
  //document.getElementById("correct").innerHTML = '0';
  //document.getElementById("possible").innerHTML = '0';
  //document.getElementById("percent").innerHTML = '0';
  document.getElementById("grade").innerHTML = 'Complete 80 marks to get a grade!';
  document.getElementById("score").innerHTML = '0';
}

//Displaying to the console to make sure it is working
console.log(getCookie('comptia_a_plus_attempts') + ' attempts');
console.log(getCookie('comptia_a_plus_correct') + ' correct');
console.log(calculatePercentage());



//following variable and function enable workon cookie list to be populated
var workOn = "{{workOn}}"
var weblink = "{{weblink}}"
var helplink = "<a href='"+weblink+"' target='_blank'>" + workOn + "</a>"



function addToCookieList(cName){
    if (clicks == 0){
        console.log('trying to add');
        console.log(helplink);
        console.log(getCookie("work_on").split(',').includes(helplink));
        console.log(getCookie("work_on").split(','));
        if (getCookie("work_on").split(',').includes(helplink)){
            console.log('No need to add');
            return
        }
        else {
            console.log('adding');
            var value = getCookie(cName) + "," + helplink;
            document.cookie = cName + "=" + value + ";path=/";
        }
    }
}
//
function calculatePercentage(){
    if (getCookie('comptia_a_plus_attempted') == 0){
      return 0;
    }else{
      var percent = Math.ceil( getCookie('comptia_a_plus_correct') / getCookie('comptia_a_plus_possible') * 100);
      return percent;
    }
}

//All vars reset when each question refreshes
var correct_required = {{correctRequired}};
var clicks = 0;
var clicks_correct = 0;
var possible_marks = {{marks}};
var possible = getCookie('comptia_a_plus_possible');
var correct_marks = getCookie('comptia_a_plus_correct');
var out_of = correct_marks.toString() + '/' + possible.toString();//create string to show score


function scoreEighty(){
  if (possible < 80){
    var grade = (80 - possible).toString() + ' to go';
  }
  else {
    if (calculatePercentage() > 86){
      grade = (9).toString();
    }
    if (calculatePercentage() > 71){
      grade = (8).toString();
    }
    if (calculatePercentage() > 56){
      grade = (7).toString();
    }
    if (calculatePercentage() > 43){
      grade = (6).toString();
    }
    if (calculatePercentage() > 31){
      grade = (5).toString();
    }
    if (calculatePercentage() > 18){
      grade = (4).toString();
    }
    if (calculatePercentage() > 11){
      grade = (3).toString();
    }
  }
  return grade;
}


//populating attempts, possible score, correct score
function populateAttemptedScoreGrade(){
  console.log("Trying to update these on screen...");
  document.getElementById("grade").innerHTML = scoreEighty();//work out whether grades can be displaye
  document.getElementById("attempted").innerHTML = parseInt(getCookie('comptia_a_plus_attempts'));
  document.getElementById("score").innerHTML = out_of;//update score element 
}

document.onload= populateAttemptedScoreGrade();

//
function ifRespondedCorrect(correct){
  if (clicks < correct_required){
    if (correct == 'yes'){
      clicks_correct = clicks_correct + 1
    }
    if (clicks_correct == correct_required){
      incrementCookie('comptia_a_plus_correct', possible_marks);//increase correct cookie
    }
    clicks = clicks + 1
  }else{
    return
  }
  if (clicks == 1){
    incrementCookie('comptia_a_plus_attempts');//record attempt on cookie
    document.getElementById("attempted").innerHTML = parseInt(getCookie('comptia_a_plus_attempts'));//update attempted element with cookie value
    incrementCookie('comptia_a_plus_possible', possible_marks);//increase possible cookie
    console.log('first response');
  }else{
      console.log('SOOOO many clicks');//happens if you click twice
  }
  var possible = getCookie('comptia_a_plus_possible');
  var correct_marks = getCookie('comptia_a_plus_correct');
  var out_of = correct_marks.toString() + '/' + possible.toString();//create string to show score 
  document.getElementById("score").innerHTML = out_of//update score element
  document.getElementById("grade").innerHTML = scoreEighty()//work out whether grades can be displayed
}


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


//allow changes between multiple choice and reveal answer perpectives
var q_type = '{{qtype}}'

function displayQuestion(q_type) {
  var x = document.getElementById("reveal");
  var y = document.getElementById(q_type);
  y.style.display = "block";
  x.style.display = "none";
}

function displayReveal(q_type) {
  var x = document.getElementById("reveal");
  var y = document.getElementById(q_type);
  x.style.display = "block";
  y.style.display = "none";
}

function revealedAnswer(){
  clicks = 10;
  submitted = true;
}
//Checkbox logic... on submit button:
var final_mark = 0
var submitted = false

function checkboxSubmit(){
  if (submitted == false){//if form hasn't been submitted before
    console.log("First form submit")

    function incrementFinalMarkIfCorrect(ci, check_box_str, row_str, correct_incorrect_str){
      if ( ci !== null){//if an option exists
        console.log(ci)
        var option =$(check_box_str).is(":checked");//get true or false value representing whether box checked
        if (option == false){//if unchecked...
          if ( ci == "correct"){//if option correct, subtract one from final_mark
            final_mark -= 1;
            document.getElementsByName(row_str)[0].style.background='red';
            document.getElementsByName(row_str)[1].style.background='lightgreen';
            document.getElementsByName(row_str)[2].style.background='lightgreen';
            document.getElementsByName(row_str)[3].style.background='lightgreen';
            document.getElementById(correct_incorrect_str).innerHTML = 'Incorrect'
          }
        } else {//elif box checked
          if (ci == "correct"){//if option correct, add one to final mark score
            final_mark += 1;
            document.getElementsByName(row_str)[0].style.background='green';
            document.getElementsByName(row_str)[1].style.background='lightgreen';
            document.getElementsByName(row_str)[2].style.background='lightgreen';
            document.getElementsByName(row_str)[3].style.background='lightgreen';
            document.getElementById(correct_incorrect_str).innerHTML = 'Correct';
          } else {//else subtract one from final mark score
            final_mark -= 1;
            document.getElementsByName(row_str)[0].style.background='red';
            document.getElementsByName(row_str)[1].style.background='pink';
            document.getElementsByName(row_str)[2].style.background='pink';
            document.getElementsByName(row_str)[3].style.background='pink';
            document.getElementById(correct_incorrect_str).innerHTML = 'Incorrect';
          }
        }
      }
    }
    incrementFinalMarkIfCorrect('{{a1ci}}', "#option1", 'option1row', 'option1ci')
    incrementFinalMarkIfCorrect('{{a2ci}}', "#option2", 'option2row', 'option2ci')
    incrementFinalMarkIfCorrect('{{a3ci}}', "#option3", 'option3row', 'option3ci')
    incrementFinalMarkIfCorrect('{{a4ci}}', "#option4", 'option4row', 'option4ci')
    incrementFinalMarkIfCorrect('{{a5ci}}', "#option5", 'option5row', 'option5ci')
    incrementFinalMarkIfCorrect('{{a6ci}}', "#option6", 'option6row', 'option6ci')
    incrementFinalMarkIfCorrect('{{a7ci}}', "#option7", 'option7row', 'option7ci')
    incrementFinalMarkIfCorrect('{{a8ci}}', "#option8", 'option8row', 'option8ci')
    incrementFinalMarkIfCorrect('{{a9ci}}', "#option9", 'option9row', 'option9ci')
    incrementFinalMarkIfCorrect('{{a10ci}}', "#option10", 'option10row', 'option10ci')

    console.log(final_mark)
    if (final_mark == correct_required){
      incrementCookie('comptia_a_plus_correct', possible_marks);//increase correct cookie
    }else{
      addToCookieList('work_on')
    }
    incrementCookie('comptia_a_plus_attempts');//record attempt on cookie
    document.getElementById("attempted").innerHTML = parseInt(getCookie('comptia_a_plus_attempts'));//update attempted element with cookie value
    incrementCookie('comptia_a_plus_possible', possible_marks);//increase possible cookie
    
    submitted = true
    console.log(submitted)
    var possible = getCookie('comptia_a_plus_possible');
    var correct_marks = getCookie('comptia_a_plus_correct');
    var out_of = correct_marks.toString() + '/' + possible.toString();//create string to show score 
    document.getElementById("score").innerHTML = out_of//update score element
    document.getElementById("grade").innerHTML = scoreEighty()//work out whether grades can be displayed
  }  
}
  





// utility functions

//sets a cookie with a given name and value
function setCookie (cName, cValue){//sets a cookie
    document.cookie = `${cName}=${cValue};path=/`;
}

//either returns the value of a cookie or "nope" if cookies doesn't exist
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

// increases value of any given cookie, default of 1
function incrementCookie(cName, to_add = 1){
    var value = parseInt(getCookie(cName)) + to_add;
    setCookie(cName, value)
    console.log('Incremented')
    console.log(cName)
}


