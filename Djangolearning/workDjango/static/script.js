document.addEventListener("DOMContentLoaded", async function() {
  // Get references to HTML elements
  var taskInput = document.getElementById("taskInput");
  var addBtn = document.getElementById("add-btn");
  var taskList = document.getElementById("taskList");

  // Add event listener to the "Add" button
  addBtn.addEventListener("click", async function() {
    // Get the value of the task input
    var taskText = taskInput.value;

    // Check if the input is not empty and meets your criteria
    if (taskText && taskText.trim() !== "") {
      // Create a new list item
      var listItem = document.createElement("li");
      listItem.className = "list-group-item";
      listItem.textContent = taskText;

      // Create a close button for the list item
      var closeBtn = document.createElement("button");
      closeBtn.className = "btn btn-danger btn-sm float-end";
      closeBtn.textContent = "Delete";

      // Add event listener to the close button
      closeBtn.addEventListener("click", function() {
        listItem.remove();
      });

      // Append the close button to the list item
      listItem.appendChild(closeBtn);

      // Append the list item to the task list
      taskList.appendChild(listItem);

      // Clear the task input
      taskInput.value = "";

      // Ajax
$.ajax({
  url: '/js/',  // Adjust the URL based on your project structure
  type: 'POST',
  headers: {
    'X-CSRFToken': csrfToken,
  },
  contentType: 'application/json',
  data: JSON.stringify({ taskText: taskText }),
  success: function (response) {
    console.log('Data posted successfully:', response);
  },
  error: function (xhr, status, error) {
    console.error('Error posting data:');
    console.log('Status:', status);
    console.log('Error:', error);
    console.log('Response Text:', xhr.responseText);
  }
});
    } else {
      console.log('Invalid task text. Please enter a valid task.');
    }
  });
});
