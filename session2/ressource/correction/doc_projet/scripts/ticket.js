function addTicketToTable(ticket) {

    const newRow = document.createElement('tr');

    for (let ticketAttribute in ticket) {
        const ticketCell = document.createElement('td');
        // ticketCell.innerHTML = ticket[ticketAttribute];
        ticketCell.innerText = ticket[ticketAttribute];
        newRow.appendChild(ticketCell)
    }

    document.getElementById('ticket-table').appendChild(newRow);
}

document.getElementById('ticket-form').addEventListener('submit', function(event) {
    
    event.preventDefault();

    const newTicket = {
        lastName: document.getElementById("frmLastName").value,
        firstName: document.getElementById("frmFirstName").value,
        email: document.getElementById("frmEmail").value,
        nature: document.getElementById("frmNature").options[document.getElementById("frmNature").selectedIndex].text,
        priority: document.getElementById("frmPriority").options[document.getElementById("frmPriority").selectedIndex].text,
        description: document.getElementById("frmDescription").value,
    }

    ticketList.push(newTicket);
    localStorage.setItem('ticketList', JSON.stringify(ticketList));

    console.log(newTicket);
    addTicketToTable(newTicket);
    
});


// Ticket list in local storage
var ticketList = [];

if (localStorage.getItem('ticketList') != null) {
    ticketList = JSON.parse(localStorage.getItem('ticketList'));
}

console.log(ticketList);
for (ticket of ticketList) {
    console.log(ticket)
    addTicketToTable(ticket);
}