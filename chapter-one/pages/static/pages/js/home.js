console.log("this js file linked with home.html");

let loading = false;

$(document).ready(function () {
  loading = true;

  console.log("home document loaded 1:", loading);

  const fetchData = async () => {
    await $.ajax({
      url: "https://jsonplaceholder.typicode.com/users",
      type: "GET",
      dataType: "json",
      success: function (res, status, xhr) {
        console.log("success res :", res);
        console.log("success status :", status);
        console.log("success xhr :", xhr);

        loading = false;
      },
      error: function (xhr, status, error) {
        console.log("success error :", error);
        console.log("success status :", status);
        console.log("success xhr :", xhr);

        loading = false;
      },
    });

    console.log("home document loaded 1 in:", loading);
  };

  fetchData();

  console.log("home document loaded 2:", loading);
});
