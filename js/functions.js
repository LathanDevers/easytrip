function sendGetRequest(element,file) {
    const ip="localhost";
    const port="8080";
    const path="http://"+ip+":"+port+"/";
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            // Display the response in the page
            element.innerHTML = this.responseText;
        } else if (this.readyState == 4 && this.status != 200) {
            // Display the error in the page
            element.innerHTML = "Error " + this.status;
        }
    };
    xhr.open("GET", path+file);
    xhr.send();
}

window.addEventListener("load", () => {
    function sendFormPaswordDatas() {
        const ip="localhost";
        const port="8080";
        const path="http://"+ip+":"+port;
      const XHR = new XMLHttpRequest();
  
      // Bind the FormData object and the form element
      const FD = new FormData(form);

      FD.set("lastname",hashpassword(FD.get("lastname")));

      console.log(FD.get("lastname"));
  
      // Set up our request
      XHR.open("POST", path);
  
      // The data sent is what the user provided in the form
      XHR.send(FD);
    }
  
    // Get the form element
    const form = document.getElementById("form");
  
    // Add 'submit' event handler
    form.addEventListener("submit", (event) => {
      event.preventDefault();
  
      sendFormPaswordDatas();
    });
  });

  function hashpassword(psw){
    const crypto = require('crypto');
    var hash=crypto.getHashes();
    hashpwd=crypto.createHash("sha1").update(pwd).digest('hex');
    return hashpwd;
  }