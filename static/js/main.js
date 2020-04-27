function predict(form) {
  data = {
    fields: [
      parseFloat(document.getElementById("age").value),
      parseFloat(document.getElementById("bp").value),
      parseFloat(document.getElementById("sg").value),
      parseFloat(document.getElementById("al").value),
      parseFloat(document.getElementById("su").value),
      parseFloat(
        document.getElementById("rbc").options[
          document.getElementById("rbc").selectedIndex
        ].value
      ),
      parseFloat(
        document.getElementById("pc").options[
          document.getElementById("pc").selectedIndex
        ].value
      ),
      parseFloat(
        document.getElementById("pcc").options[
          document.getElementById("pcc").selectedIndex
        ].value
      ),
      parseFloat(
        document.getElementById("ba").options[
          document.getElementById("ba").selectedIndex
        ].value
      ),
      parseFloat(document.getElementById("bgr").value),
      parseFloat(document.getElementById("bu").value),
      parseFloat(document.getElementById("sc").value),
      parseFloat(document.getElementById("sod").value),
      parseFloat(document.getElementById("pot").value),
      parseFloat(document.getElementById("hemo").value),
      parseFloat(document.getElementById("pcv").value),
      parseFloat(document.getElementById("wc").value),
      parseFloat(document.getElementById("rc").value),
      parseFloat(
        document.getElementById("htn").options[
          document.getElementById("htn").selectedIndex
        ].value
      ),
      parseFloat(
        document.getElementById("dm").options[
          document.getElementById("dm").selectedIndex
        ].value
      ),
      parseFloat(
        document.getElementById("cad").options[
          document.getElementById("cad").selectedIndex
        ].value
      ),
      parseFloat(
        document.getElementById("appet").options[
          document.getElementById("appet").selectedIndex
        ].value
      ),
      parseFloat(
        document.getElementById("pe").options[
          document.getElementById("pe").selectedIndex
        ].value
      ),
      parseFloat(
        document.getElementById("ane").options[
          document.getElementById("ane").selectedIndex
        ].value
      ),
    ],
  };

  var http = new XMLHttpRequest();
  var url = window.location.href.split("static")[0] + "model";
  http.open("POST", url, true);
  http.setRequestHeader("Content-type", "application/json");

  http.onreadystatechange = function () {
    if (http.readyState == 4 && http.status == 200) {

      let result = String(http.responseText).split("[")[1].split("]")[0];
      resut = parseInt(result);
      console.log(result);
      if(result == 1)
        result = "Positive";
      else if(result == 0)
        result = "Negative";
      materialAlert("<p>Result</p>", "<h1>" + result + "</h1>", () => { });
    }
  };
  http.send(JSON.stringify(data));
  console.table(data);
}


function run() {
  let frame = document.getElementById("frame");
  frame.src = "/static/html/content.html";
  frame.style.width = "100%";
  frame.style.height = "100vh";
  document.getElementsByClassName("bt")[0].remove();
}
