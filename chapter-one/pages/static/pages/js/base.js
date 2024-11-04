$(document).ready(function () {
  // console.log("This comes from jquery");

  const title = $("#title");
  title.text("This title comes by jquery selector");
  title.text(`${title.text()}. ${"This title comes by jquery selector 2"}`);

  const content = $("#content");
  // console.log("content html::", content.html());

  // console.log("attr :", content.attr("id"));

  content.append("<div id='new' class='red'>This is appended by jQuery</div>");

  $("#rm_btn").on("click", function () {
    $("#new").remove();
  });
});
