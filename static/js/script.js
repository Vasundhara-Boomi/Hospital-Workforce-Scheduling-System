document.addEventListener("DOMContentLoaded", function() {
    
  // const friendRequests = {
  //     "D1": ["Dr. Rajesh Gupta", "2023-11-27,2023-11-29"],
      
  //     "N1": ["Aarti Gupta", "2023-11-24"],
  //     'D14':['Dr. Deepak M','2023-11-26']
  //     }
      
// ;

  // const friendRequests = pendingInfo;
  


  const requestsList = document.getElementById("requests-list");

  for (const userInfo of pendingInfo) {
      const { ID: userId, Name: name, Dates: dates } = userInfo;
      const listItem = document.createElement("li");
      listItem.innerHTML = `
          <span>ID: ${userId}</span>
          <span>Name: ${name}</span>
          <span>Dates: ${dates}</span>
          <button data-email="${dates}" data-userid="${userId}" class="accept-button">Accept</button>
          <button data-email="${dates}" data-userid="${userId}" class="deny-button">Deny</button>
      `;

      // Add event listener for "accept" button
      const acceptButton = listItem.querySelector(".accept-button");
      acceptButton.addEventListener("click", () => {
          // Remove the current request from the list
          requestsList.removeChild(listItem);

          // Store the accepted request
          const acceptedRequest = { userId: userId, action: "accept" ,Dates:dates};

          // Send the accepted request to the server
          sendRequestToServer(acceptedRequest);
      });

      // Add event listener for "deny" button
      const denyButton = listItem.querySelector(".deny-button");
      denyButton.addEventListener("click", () => {
          // Remove the current request from the list
          requestsList.removeChild(listItem);

          // Store the rejected request
          const rejectedRequest = { userId: userId, action: "deny",Dates:dates };

          // Send the rejected request to the server
          sendRequestToServer(rejectedRequest);
      });

      requestsList.appendChild(listItem);
  }

  function sendRequestToServer(requestData) {
      fetch('/process_request', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify(requestData),
      })
      .then(response => response.json())
      .then(data => {
          console.log('Server response:', data);
      })
      .catch(error => {
          console.error('Error sending request to server:', error);
      });
  }
});
