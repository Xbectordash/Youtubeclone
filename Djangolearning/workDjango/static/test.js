document.addEventListener("DOMContentLoaded", async function () {
  // Get references to HTML elements
  var taskInput = document.getElementById("taskInput");
  var addBtn = document.getElementById("add-btn");
  var taskList = document.getElementById("taskList");

  // Add event listener to the "Add" button
  addBtn.addEventListener("click", async function () {
    // Get the value of the task input
    var taskText = taskInput.value;

    // Check if the input is not empty
    if (taskText.trim() !== "") {
      // Create a new list item
      var listItem = document.createElement("li");
      listItem.className = "list-group-item";
      listItem.textContent = taskText;

      // Create a close button for the list item
      var closeBtn = document.createElement("button");
      closeBtn.className = "btn btn-danger btn-sm float-end";
      closeBtn.textContent = "Delete";

      // Add event listener to the close button
      closeBtn.addEventListener("click", function () {
        listItem.remove();
      });

      // Append the close button to the list item
      listItem.appendChild(closeBtn);

      // Append the list item to the task list
      taskList.appendChild(listItem);

      // Clear the task input
      taskInput.value = "";

      // Fetch data from the server
      try {
        let response = await fetch("/", {
          method: "get",
          headers: {
            'X-Requested-With': 'XMLHttpRequest', // Corrected typo
            'Content-Type': 'application/json',
          },
        });

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        let data = await response.json();
        console.log(data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    }
  });
});
