function addDepartment() {
    const deptName = document.getElementById('deptName').value;
    const deptId = document.getElementById('deptId').value;
    const numDoctors = document.getElementById('numDoctors').value;
    const numReceptionists = document.getElementById('numReceptionists').value;

    const departmentData = {
        name: deptName,
        id: deptId,
        doctors: numDoctors,
        nurses: numReceptionists
    };

    // Disable the button to prevent multiple clicks
    const addButton = document.getElementById('addButton');
    addButton.disabled = true;

    fetch('/add_department', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(departmentData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Department added successfully:', data);
        // Update button text and style to indicate success
        addButton.innerHTML = 'Done &#10004;';
        addButton.classList.add('success');

        // Clear the form fields
        document.getElementById('deptName').value = '';
        document.getElementById('deptId').value = '';
        document.getElementById('numDoctors').value = '';
        document.getElementById('numReceptionists').value = '';

        // Enable the button after a brief delay (2 seconds)
        setTimeout(() => {
            addButton.disabled = false;
            addButton.innerHTML = 'Add Department';
            addButton.classList.remove('success');
        }, 2000);
    })
    .catch(error => {
        console.error('Error adding department:', error);
        // Update button text and style to indicate failure
        addButton.innerHTML = 'Error &#10008;';
        addButton.classList.add('error');
    });
}
