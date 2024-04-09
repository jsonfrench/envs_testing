//French 2.2.23

function buttonLogic() {
    if(document.getElementById("button1").innerHTML == "nothing to see here...") {
        document.getElementById("button1").innerHTML = "you shouldn\'t have done that.";
        document.getElementById("birthday-message").innerHTML = "listen to the voices.";
    }
    else {
        document.getElementById("button1").innerHTML = "nothing to see here...";
        document.getElementById("birthday-message").innerHTML = "Happy Birthday!";
    }
}
